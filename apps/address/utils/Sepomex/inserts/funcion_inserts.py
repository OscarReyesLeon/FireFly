from apps.address.models import StateModel, MunicipalityModel, NeighborhoodModel
from app.settings import BASE_DIR
import csv

def insert_data():
    
    location_files = f'{BASE_DIR}/apps/address/utils/Sepomex/inserts/'

    #Si se desea agregar más estados, se debe agregar el nombre del estado y el nombre del archivo
    name_files = {
        'Guanajuato': '11-Guanajuato.csv',
        'Hidalgo': '13-Hidalgo.csv',
        'Jalisco': '14-Jalisco.csv',
        'México': '15-Mexico.csv',
        'Michoacán': '16-Michoacan.csv',
        'San Luis Potosí': '24-San_Luis_Potosi.csv'
    }

    list_states = []
    list_municipalities = []
    list_neighborhoods = []
    for key, value in name_files.items():
        with open(f'{location_files}{value}', 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            state_current = StateModel(name=key, code=value.split('-')[0])
            list_states.append(state_current)
            last_municipality = ''
            for row in reader:
                if last_municipality != row['D_mnpio']:
                    municipality = MunicipalityModel(name=row['D_mnpio'], code=row['c_mnpio'], state=state_current)
                    list_municipalities.append(municipality)
                list_neighborhoods.append(NeighborhoodModel(
                    name=row['d_asenta'],
                    code=row['id_asenta_cpcons'],
                    type_neighborhood=row['d_tipo_asenta'],
                    type_zone=row['d_zona'],
                    municipality=municipality,
                    postal_code=row['d_codigo']
                ))
                last_municipality = row['D_mnpio']

    StateModel.objects.bulk_create(list_states)
    MunicipalityModel.objects.bulk_create(list_municipalities)
    NeighborhoodModel.objects.bulk_create(list_neighborhoods)