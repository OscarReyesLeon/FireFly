from datetime import datetime
from django.utils import timezone
from django.db.models import Q
from apps.external.models import LecturaModel, MaquinaModel
import pandas as pd
from time import time
from dateutil.relativedelta import relativedelta

shifts_options = {
    "22:00-05:59": ["22:00:00", "05:59:59"],
    "06:00-12:59": ["06:00:00", "12:59:59"],
    "13:00-17:59": ["13:00:00", "17:59:59"],
    "18:00-21:59": ["18:00:00", "21:59:59"],
}
# shifts_options = {
#     "T1": ["22:00:00", "05:59:59"],
#     "T2": ["06:00:00", "12:59:59"],
#     "T3": ["13:00:00", "17:59:59"],
#     "T4": ["18:00:00", "21:59:59"],
# }


class DashboardService:
    def __init__(self, hours: int) -> None:
        self.final_date: datetime = timezone.now()
        self.hours: int = hours  # hours
        self.initial_date: datetime = self.get_shifts()
        self.df: pd.DataFrame = pd.DataFrame()
        self.result_df: pd.DataFrame = pd.DataFrame()
        self.machine_df: pd.DataFrame = pd.DataFrame()
        self.columns: list[dict] = []

    def get_shifts(self) -> datetime:
        """
        Filtra la fecha inicial para que el turno actual no tenga datos de su último
        turno (ejemplo: si son las 3:00 PM, el turno 3 no debe tener datos de 1:00 PM a 3:00 PM
        de hoy, pero no debe tener datos del turno de ayer
        )
        """
        SHIFT_FORMAT = "%H:%M:%S"
        initial_date: datetime = self.final_date - timezone.timedelta(hours=self.hours)
        initial_date_time = initial_date.time()

        # Si la fecha inicial está entre las 10 PM y las 6 AM, se debe cambiar la fecha
        # El reporte debe comenzar con los datos de las 6 AM del día
        # anterior si está entre las 00:00:00 y las 5:59:59 AM o actual si está entre las
        # 22:00:00 y las 23:59:59
        morning = bool(
            initial_date_time
            <= timezone.datetime.strptime("05:59:59", SHIFT_FORMAT).time()
        )
        if morning or (
            initial_date_time
            >= timezone.datetime.strptime("22:00:00", SHIFT_FORMAT).time()
        ):
            return initial_date.replace(
                hour=6,
                minute=0,
                second=0,
                microsecond=0,
                day=self.final_date.day - int(morning),
            )
        for shift in shifts_options:
            start, end = shifts_options[shift]
            start = timezone.datetime.strptime(start, SHIFT_FORMAT).time()
            end = timezone.datetime.strptime(end, SHIFT_FORMAT).time()

            if start <= initial_date_time <= end:
                current = initial_date.replace(
                    hour=end.hour + 1, minute=0, second=0, microsecond=0
                )
                return initial_date if current > self.final_date else current

        return initial_date

    def create_df(self):
        """
        Crea el dataframe con los datos de la fecha inicial a la fecha final
        """
        queryset = (
            LecturaModel.objects.using("sensor")
            .filter(Q(fecha__range=[self.initial_date, self.final_date]))
            .values("valor", "fecha", "maquina")
        )
        self.df = pd.DataFrame(list(queryset))
        # Save
        # self.df.to_csv("data_nueva.csv")
        self.df["fecha"] = pd.to_datetime(self.df["fecha"])
        self.df["hora"] = self.df["fecha"].dt.hour
        self.df["minutos"] = self.df["fecha"].dt.minute
        self.df["segundos"] = self.df["fecha"].dt.second
        self.df = self.df.sort_values(by=["fecha"]).reset_index(drop=True)

        # Convertir 'hora', 'minutos', 'segundos' a formato numérico
        self.df["hora_num"] = (
            self.df["hora"] * 10000 + self.df["minutos"] * 100 + self.df["segundos"]
        )

        # Asignar el turno correspondiente utilizando operaciones vectorizadas
        shifts_df = pd.DataFrame.from_dict(
            shifts_options, orient="index", columns=["inicio", "fin"]
        )
        shifts_df[["inicio", "fin"]] = shifts_df[["inicio", "fin"]].applymap(
            lambda x: int(x.replace(":", ""))
        )

        self.df["turno"] = (
            pd.cut(
                self.df["hora_num"],
                bins=[-float("inf")] + shifts_df["fin"].tolist(),
                labels=shifts_df.index,
            )
            .fillna(method="bfill")
            .astype(str)
        )

        self.df["estado"] = (self.df["valor"] > 10).astype(int)
        self.df.drop(["hora_num"], axis=1, inplace=True)

    def process_df_by_dashboard(self, df, state) -> pd.DataFrame:
        df_state = df[df["estado"] == state].reset_index(drop=True)

        if df_state.empty:
            return None

        # Calcular la suma del tiempo encendido y mostrar el resultado
        df_state["delta_tiempo"] = df_state["delta_tiempo"].dt.total_seconds()
        result_df = df_state.groupby("estado")
        result_df = result_df.agg(
            {
                "delta_tiempo": ["sum", "mean", "min", "max"],
                "valor": ["mean", "min", "max", "median"],
            }
        ).reset_index(drop=True)

        # Desagrupar las columnas 'delta_time' y 'valor'
        result_df.columns = [f"{col[0]}_{col[1]}" for col in result_df.columns]
        # Delta time sum a horas, minutos, segundos (quitar días)
        result_df["delta_tiempo_sum"] = pd.to_timedelta(
            result_df["delta_tiempo_sum"], unit="s"
        )

        # Redefinir el índice para mayor claridad
        result_df.reset_index(inplace=True)

        result_df["valor_mean"] = result_df["valor_mean"].round(3)
        return result_df

    def get_machines(self):
        """
        Obtiene las máquinas que están en el dashboard
        """
        machine_queryset = (
            MaquinaModel.objects.all()
            .values("nombre", "id")
            .using("sensor")
            .order_by("nombre")
        )
        self.machine_df = pd.DataFrame(list(machine_queryset))
        self.machine_df = self.machine_df.sort_values(by=["nombre"]).reset_index(
            drop=True
        )

    def process_dashboard(self):
        """
        Procesa los datos de la fecha inicial a la fecha final
        """
        initial_time = time()
        self.create_df()
        self.get_machines()

        self.columns = [{"title": "Turno", "data": "shift"}]

        machines = self.df["maquina"].unique().tolist()
        machines.sort()
        shifts = self.df["turno"].unique().tolist()

        for index, row in self.machine_df.iterrows():
            name = row["nombre"]
            self.columns.append({"title": name, "data": name})
        table_value, table_time, table_io = [], [], []
        for shift in shifts:
            initial_data = {"shift": shifts_options.get(shift)}
            data_value, data_time, data_io = (
                initial_data.copy(),
                initial_data.copy(),
                initial_data.copy(),
            )
            for index, row in self.machine_df.iterrows():
                name = row["nombre"]
                machine = row["id"]

                result_df = self.df[
                    (self.df["maquina"] == machine) & (self.df["turno"] == shift)
                ].copy()
                result_df.loc[:, "cambio_estado"] = (
                    result_df["estado"] != result_df["estado"].shift()
                ).cumsum()
                result_df.loc[:, "delta_tiempo"] = result_df.groupby("cambio_estado")[
                    "fecha"
                ].diff()
                count = result_df["cambio_estado"].max() - 1
                result_df = self.process_df_by_dashboard(result_df, 1)
                if result_df is None:
                    data_value[name] = 0
                    data_time[name] = "00:00:00"
                    data_io[name] = 0
                    continue
                result_df["io"] = count
                first_item = result_df.iloc[0]

                data_value[name] = first_item["valor_mean"]
                data_time[name] = str(first_item["delta_tiempo_sum"]).split(" ")[-1]
                data_io[name] = str(first_item["io"])
            table_value.append(data_value)
            table_time.append(data_time)
            table_io.append(data_io)

        # Horas entre self.final_date e initial_date
        total_time = relativedelta(self.final_date, self.initial_date)
        time_report = (total_time.days * 24) + total_time.hours
        string_time = f"{time_report} horas {total_time.minutes} minutos"
        return {
            "columns": self.columns,
            "table_value": table_value,
            "table_time": table_time,
            "table_io": table_io,
            "initial_date": self.initial_date.strftime("%Y-%m-%d %H:%M:%S"),
            "final_date": self.final_date.strftime("%Y-%m-%d %H:%M:%S"),
            "total_records": self.df.shape[0],
            "total_time": time() - initial_time,
            "horas": string_time,
        }


RESPUESTA_EJEMPLO = {
    "columns": [
        {"title": "Turno", "data": "shift"},
        {"title": "P4-M01", "data": "P4-M01"},
        {"title": "P4-M02", "data": "P4-M02"},
        {"title": "P4-M03", "data": "P4-M03"},
        {"title": "P2-M06", "data": "P2-M06"},
        {"title": "P2-M01", "data": "P2-M01"},
        {"title": "P2-M04", "data": "P2-M04"},
        {"title": "P2-M03", "data": "P2-M03"},
        {"title": "P2-M02", "data": "P2-M02"},
        {"title": "P2-M05", "data": "P2-M05"},
        {"title": "P3-M01", "data": "P3-M01"},
        {"title": "P3-M02", "data": "P3-M02"},
        {"title": "P1-M01", "data": "P1-M01"},
        {"title": "P5-M01", "data": "P5-M01"},
        {"title": "P5-M02", "data": "P5-M02"},
    ],
    "table_value": [
        {
            "shift": ["18:00:00", "21:59:59"],
            "P4-M01": 41.05,
            "P4-M02": 44.386,
            "P4-M03": 57.545,
            "P2-M06": 82.334,
            "P2-M01": 34.013,
            "P2-M04": 55.603,
            "P2-M03": 49.622,
            "P2-M02": 0,
            "P2-M05": 45.88,
            "P3-M01": 38.984,
            "P3-M02": 121.324,
            "P1-M01": 42.288,
            "P5-M01": 101.28,
            "P5-M02": 116.679,
        },
        {
            "shift": ["22:00:00", "05:59:59"],
            "P4-M01": 49.635,
            "P4-M02": 52.62,
            "P4-M03": 62.227,
            "P2-M06": 85.123,
            "P2-M01": 38.475,
            "P2-M04": 63.554,
            "P2-M03": 51.594,
            "P2-M02": 0,
            "P2-M05": 49.627,
            "P3-M01": 44.232,
            "P3-M02": 135.766,
            "P1-M01": 47.874,
            "P5-M01": 108.02,
            "P5-M02": 114.546,
        },
        {
            "shift": ["06:00:00", "12:59:59"],
            "P4-M01": 50.316,
            "P4-M02": 52.903,
            "P4-M03": 58.488,
            "P2-M06": 83.792,
            "P2-M01": 34.068,
            "P2-M04": 57.981,
            "P2-M03": 32.361,
            "P2-M02": 0,
            "P2-M05": 46.454,
            "P3-M01": 43.131,
            "P3-M02": 130.491,
            "P1-M01": 47.603,
            "P5-M01": 118.35,
            "P5-M02": 127.758,
        },
        {
            "shift": ["13:00:00", "17:59:59"],
            "P4-M01": 0,
            "P4-M02": 0,
            "P4-M03": 0,
            "P2-M06": 0,
            "P2-M01": 0,
            "P2-M04": 0,
            "P2-M03": 0,
            "P2-M02": 0,
            "P2-M05": 0,
            "P3-M01": 0,
            "P3-M02": 0,
            "P1-M01": 0,
            "P5-M01": 0,
            "P5-M02": 0,
        },
    ],
    "table_time": [
        {
            "shift": ["18:00:00", "21:59:59"],
            "P4-M01": "00:38:31",
            "P4-M02": "00:41:24",
            "P4-M03": "00:44:18",
            "P2-M06": "00:46:15",
            "P2-M01": "00:42:57",
            "P2-M04": "00:38:46",
            "P2-M03": "00:34:51",
            "P2-M02": "00:00:00",
            "P2-M05": "00:36:43",
            "P3-M01": "00:48:45",
            "P3-M02": "00:58:56",
            "P1-M01": "00:38:19",
            "P5-M01": "00:46:25",
            "P5-M02": "00:46:23",
        },
        {
            "shift": ["22:00:00", "05:59:59"],
            "P4-M01": "06:59:54",
            "P4-M02": "06:59:43",
            "P4-M03": "06:59:54",
            "P2-M06": "06:59:59",
            "P2-M01": "06:59:59",
            "P2-M04": "06:59:59",
            "P2-M03": "06:59:59",
            "P2-M02": "00:00:00",
            "P2-M05": "06:59:59",
            "P3-M01": "06:59:59",
            "P3-M02": "06:59:59",
            "P1-M01": "06:59:44",
            "P5-M01": "06:59:41",
            "P5-M02": "06:59:56",
        },
        {
            "shift": ["06:00:00", "12:59:59"],
            "P4-M01": "06:47:36",
            "P4-M02": "06:47:46",
            "P4-M03": "06:47:46",
            "P2-M06": "06:50:25",
            "P2-M01": "06:48:14",
            "P2-M04": "06:49:58",
            "P2-M03": "01:08:46",
            "P2-M02": "00:00:00",
            "P2-M05": "06:49:57",
            "P3-M01": "06:45:01",
            "P3-M02": "06:45:02",
            "P1-M01": "05:13:09",
            "P5-M01": "06:46:37",
            "P5-M02": "06:46:38",
        },
        {
            "shift": ["13:00:00", "17:59:59"],
            "P4-M01": "00:00:00",
            "P4-M02": "00:00:00",
            "P4-M03": "00:00:00",
            "P2-M06": "00:00:00",
            "P2-M01": "00:00:00",
            "P2-M04": "00:00:00",
            "P2-M03": "00:00:00",
            "P2-M02": "00:00:00",
            "P2-M05": "00:00:00",
            "P3-M01": "00:00:00",
            "P3-M02": "00:00:00",
            "P1-M01": "00:00:00",
            "P5-M01": "00:00:00",
            "P5-M02": "00:00:00",
        },
    ],
    "table_io": [
        {
            "shift": ["18:00:00", "21:59:59"],
            "P4-M01": "3",
            "P4-M02": "3",
            "P4-M03": "3",
            "P2-M06": "2",
            "P2-M01": "4",
            "P2-M04": "4",
            "P2-M03": "2",
            "P2-M02": 0,
            "P2-M05": "4",
            "P3-M01": "3",
            "P3-M02": "7",
            "P1-M01": "2",
            "P5-M01": "3",
            "P5-M02": "3",
        },
        {
            "shift": ["22:00:00", "05:59:59"],
            "P4-M01": "0",
            "P4-M02": "0",
            "P4-M03": "0",
            "P2-M06": "0",
            "P2-M01": "0",
            "P2-M04": "0",
            "P2-M03": "0",
            "P2-M02": 0,
            "P2-M05": "0",
            "P3-M01": "0",
            "P3-M02": "0",
            "P1-M01": "0",
            "P5-M01": "0",
            "P5-M02": "0",
        },
        {
            "shift": ["06:00:00", "12:59:59"],
            "P4-M01": "1",
            "P4-M02": "1",
            "P4-M03": "1",
            "P2-M06": "1",
            "P2-M01": "1",
            "P2-M04": "1",
            "P2-M03": "3",
            "P2-M02": 0,
            "P2-M05": "1",
            "P3-M01": "3",
            "P3-M02": "1",
            "P1-M01": "1",
            "P5-M01": "1",
            "P5-M02": "1",
        },
        {
            "shift": ["13:00:00", "17:59:59"],
            "P4-M01": 0,
            "P4-M02": 0,
            "P4-M03": 0,
            "P2-M06": 0,
            "P2-M01": 0,
            "P2-M04": 0,
            "P2-M03": 0,
            "P2-M02": 0,
            "P2-M05": 0,
            "P3-M01": 0,
            "P3-M02": 0,
            "P1-M01": 0,
            "P5-M01": 0,
            "P5-M02": 0,
        },
    ],
    "initial_date": "2023-11-24 17:16:08",
    "final_date": "2023-11-25 17:16:08",
    "total_records": 1952429,
    "total_time": 43.84835481643677,
    "horas": "24 horas 0 minutos",
}
