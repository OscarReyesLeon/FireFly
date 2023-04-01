$(function(){
    createApp({
        delimiters: ['{$', '$}'],
        data() {
            const initial_form_order = {
                id: null,
                key_order: null,
                status: null,
                invoice_status: false,
                autorization: false,
                delivery_date_estimated: null,
                delivery_date: null,
                client: null,
                address: null,
                vehicle: null,
                driver: null,
                liters: null,
                pump: null,
                errors: {},
                initial_status: null,
            }

            const initial_form_product = {
                id: null,
                product: null,
                quantity_order: null,
                quantity_transfer: null,
                truck: null,
                ton_out: null,
                ton_receiver: null,
                errors: {}
            }
            
            return {
                options_invoice_status: ref([]),
                options_order_status: ref([]),
                options_clients: ref([]),
                options_address: ref([]),
                disabled_force: true,
                options_status_filter: ref([]),
                form_order: ref({ ...initial_form_order }),

                initial_form_order,
                url_order: '/api/v1/orders/',
                url_client: '/api/v1/clients/',

                options_vehicles: ref([]),
                options_drivers: ref([]),
                options_fuel_pump: ref([]),
                url_administration: '/api/v1/administration/',
                //details
                options_products: ref([]),
                options_trucks: ref([]),
                form_product: ref({ ...initial_form_product }),
                initial_form_product,
                array_products: ref([]),
                perms: ref({}),

                url_users: '/api/v1/users/',
            }
        },
        methods: {
            submit_form(){
                let with_error = false
                if (!this.$refs.formGeneralVue.checkValidity()) {
                    NotificationToast.fire({
                        icon: 'error',
                        title: 'Por favor llena todos los campos requeridos'
                    })
                    with_error = true
                }
                this.form_order.errors.client = null
                this.form_order.errors.address = null
                if (!this.form_order.client){
                    this.form_order.errors.client = "Selecciona un cliente"
                    with_error = true
                }
                if (!this.form_order.address){
                    this.form_order.errors.address = "Selecciona una dirección"
                    with_error = true
                }

                for(let prod of this.array_products){
                    if(!prod.product){
                        NotificationToast.fire({
                            icon: 'error',
                            title: 'Selecciona un producto'
                        })
                        with_error = true
                    }
                }

                if(this.form_order.autorization == false && this.form_order.status.id  > 2){
                    NotificationToast.fire({
                        icon: 'error',
                        title: 'No puedes cambiar el estatus de la orden si no esta autorizada'
                    })
                    with_error = true
                }

                if(with_error) return
                
                let data_send = {
                    ...this.form_order,
                    products: []
                }
                delete data_send.errors

                for(let key in data_send){
                    if(!data_send[key])
                        delete data_send[key]
                    else if(data_send[key].id != null)
                        data_send[key] = data_send[key].id
                }
                
                for(let i in this.array_products){
                    let product = {...this.array_products[i]}
                    this.array_products[i].errors = {}
                    for(let key in product){
                        if(!product[key])delete product[key]
                        else if(product[key].id != null) product[key] = product[key].id
                    }
                    data_send.products.push(product)
                }

                let self = this
                if(this.form_order.id){
                    method = 'PATCH'
                    url = this.url_order + this.form_order.id + '/'
                }else{
                    method = 'POST'
                    url = this.url_order
                }
                saveFormAsync(url, method, {
                        'data': JSON.stringify(data_send)
                    }, (data)=>{
                    },(error)=>{
                        error = error.responseJSON
                        if(error.products){
                            for(let i in error.products){
                                let product = error.products[i]
                                for(let key in product){
                                    self.array_products[i].errors[key] = product[key][0]
                                }
                            }
                            delete error.products
                        }
                        this.form_order.errors = error
                    })
                },
            asign_value_select(value, options){
                for(let option of options){
                    if(option.id == value){
                        return option
                    }
                }
                return null
            },
        },
        watch: {
            'form_order.client': function (new_value, old_value) {
                this.form_order.address = null
                if (!new_value) {
                    this.options_address = []
                    this.form_order.client.error = "Selecciona un cliente"
                    return
                }
                
                this.form_order.client.error = null
                getDataAsync(this.url_client + this.form_order.client.id + "/address/options/", (data) => {
                    this.options_address = data
                    if(this.form_order.address_initial){
                        this.form_order.address = this.asign_value_select(this.form_order.address_initial, this.options_address)
                        delete this.form_order.address_initial
                    }
                })
            },
        },
        computed: {
            header_table_products(){
                let array_header = ["Producto"]
                if(this.perms.asign_truck) array_header.push("Remolque")
                array_header.push("Cantidad pedido")
                if (this.perms.quantity_transfer) array_header.push("Cantidad traslado")
                if (this.perms.ton_out) array_header.push("Toneladas")
                return array_header
            },
            options_invoice_filter(){
                if(!this.perms.super_user || this.form_order.status < 3)
                    return this.options_invoice_status.filter((item) => item.id < 2)
                return this.options_invoice_status
            },
            disabled_fields(){
                if(this.perms.detail_view) return true
                if(this.perms.super_user) return false
                if(this.form_order.status){
                    if(this.form_order.status.id >= 5 && this.form_order.initial_status != 4)
                        return true
                }
                return false
            }
        },
        async mounted() {
            await getDataAsync(this.url_users + "permissions/order_view/", (data) => {
                this.perms = data
            })

            await getDataAsync(this.url_order + "options/", (data) => {
                this.options_invoice_status = data.invoice_status
                this.options_order_status = data.order_status
                this.form_order.status = data.order_status[0]
                this.form_order.invoice_status = data.invoice_status[0]
                this.form_order.key_order = data.current_key_order
                this.form_order.initial_status = 1
            })

            await getDataAsync(this.url_client + "options/", (data) => {
                this.options_clients = data
            })

            await getDataAsync(this.url_administration + "options/", (data) => {
                this.options_vehicles = data.options_vehicles
                this.options_drivers = data.options_drivers
                this.options_fuel_pump = data.options_fuel_pump
                this.options_products = data.options_products
                this.options_trucks = data.options_trucks
            })

            if(this.$refs.formGeneralVue.action.includes('update')){
                let url = this.$refs.formGeneralVue.action
                let pk = url.split('/')[url.split('/').length - 2]
                let url_get = `${this.url_order}${pk}/`
                let self = this

                await getDataAsync(url_get,(data)=>{
                    let products = data.detail
                    delete data.detail
                    for(let prod of products){
                        self.array_products.push({
                            id: prod.id,
                            product: self.asign_value_select(prod.product, self.options_products),
                            truck: self.asign_value_select(prod.truck, self.options_trucks),
                            quantity_order: prod.quantity_order,
                            quantity_transfer: prod.quantity_transfer,
                            ton_out: prod.ton_out,
                            errors: {},
                        })
                    }

                    self.form_order = {
                        ...data,
                        errors: {},
                        invoice_status: self.asign_value_select(data.invoice_status, self.options_invoice_status),
                        status: self.asign_value_select(data.status, self.options_order_status),
                        client: self.asign_value_select(data.client, self.options_clients),
                        address: self.asign_value_select(data.address, self.options_address),
                        vehicle: self.asign_value_select(data.vehicle, self.options_vehicles),
                        driver: self.asign_value_select(data.driver, self.options_drivers),
                        fuel_pump: self.asign_value_select(data.fuel_pump, self.options_fuel_pump),
                        truck: self.asign_value_select(data.truck, self.options_trucks),
                        address_initial: data.address,
                        initial_status: data.status,
                    }
                })
            }

            if(this.perms.super_user)
                    this.options_status_filter = this.options_order_status
            else{
                let next_status = this.form_order.status ? this.form_order.status.id : 1
                this.options_status_filter = this.options_order_status.filter((item) => [next_status, next_status+1].includes(item.id))
            }
        },
        components: {
            'v-select': window["vue-select"],
            'table-component': tableComponent,
        },
    }).mount('#appVue')
});