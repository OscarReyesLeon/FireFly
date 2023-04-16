$(function(){
    createApp({
        delimiters: ['{$', '$}'],
        data() {
            return {
                key_order: ref(''),
                url_order: '/api/v1/orders/warehouse/',
                url_options_fuel:'/api/v1/administration/options/?only=fuel',
                headers_table: ref(["Producto", "Remolque", "Cantidad", "Toneladas salida", "Toneladas entregadas"]),
                order: ref({
                    id: null,
                    key_order: '',
                    client: '',
                    address: '',
                    vehicle: '',
                    driver: '',
                    fuel_pump: null,
                    fuel_liters: null
                }),
                products : ref([]),
                disabled: ref(false),
                step: ref(0),
                options_fuel_pump: ref([])
            }
        },
        methods: {
            async search_order(){
                this.order = {}
                await getDataAsync(this.url_order + "?key_order=" +this.key_order + "&step=" + this.step,  (data)=>{
                    this.order = data.order
                    this.order.status_display = data.status
                    this.products = data.order.detail
                    this.disabled = data.disabled
                    if(data.msg){
                        NotificationToast.fire({
                            icon: 'question',
                            title: data.msg
                        })
                    }
                })
            },
            submit_form(sum_step){
                if (!this.$refs.formGeneralVue.checkValidity()) {
                    NotificationToast.fire({
                        icon: 'error',
                        title: 'Por favor llena todos los campos requeridos'
                    })
                    return
                }
                let current_data = []
                for(let product of this.products){
                    current_data.push({
                        id: product.id,
                        ton_out: product.ton_out,
                        ton_receiver: product.ton_receiver,
                    })
                }


                let send_data = {
                    "id": this.order.id,
                    "status": this.order.status + sum_step,
                    "products": current_data
                }

                if(this.order.status == 7){
                    if(!this.order.fuel_pump){
                        NotificationToast.fire({
                            icon: 'error',
                            title: 'Por favor selecciona una bomba de combustible'
                        })
                        return
                    }else{
                        console.log("Hola")
                        send_data.fuel_pump = this.order.fuel_pump.id
                        send_data.fuel_liters = this.order.fuel_liters
                    }
                }

                saveFormAsync(this.url_order, "POST", {
                    "data": JSON.stringify(send_data)
                }, (data)=>{
                    NotificationToast.fire({
                        icon: 'success',
                        title: 'Se ha guardado correctamente'
                    })
                    this.search_order()
                }, (error)=>{
                    console.log(error)
                    NotificationToast.fire({
                        icon: 'error',
                        title: 'Ha ocurrido un error'
                    })
                })
            },
        },
        async mounted() {
            this.step = $('#step_id').val()
            await getDataAsync(this.url_options_fuel, (data)=>{
                this.options_fuel_pump = data.options_fuel_pump
            })
            // await this.search_order()
        },
        components: {
            'v-select': window["vue-select"],
            'table-component': tableComponent,
        },
    }).mount('#appVue')
});