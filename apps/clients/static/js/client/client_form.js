$(document).ready(function () {
    const { createApp, ref } = Vue
    createApp({
        delimiters: ['{$', '$}'],
        data() {
            const initialCredit = {
                'id': '',
                'description': '',
                'amount': '',
                'limit_date': '',
            }
            const initialForm = {
                'id': '',
                'business_name': '',
                'rfc': '',
                'email': '',
                'phone': '',
                'first_name': '',
                'last_name': '',
                'last_name_mother': ''
            }
            return {
                initialCredit,
                initialForm,
                form: ref(initialForm),
                credit_array: ref([]),
                address: ref([]),
            }
        },
        computed: {
            url_endpoint_save_data(){
                url = '/api/v1/clients/'
                if(this.form.id)
                    url += `${this.form.id}/`
                url += 'complete/'
                return url
            }
        },
        methods: {
            only_number_input(event) {
                if (event.keyCode < 48 || event.keyCode > 57) {
                    event.preventDefault();
                }
            },
            submit_form(){
                if (!this.$refs.formGeneral.checkValidity()) {
                    NotificationToast.fire({
                        icon: 'error',
                        title: 'Por favor llena todos los campos requeridos'
                    })
                }
                let text = ''
                for (let i = 0; i < this.address.length; i++) {
                    let current = this.address[i]
                    if (!current.neighborhood.name) {
                        NotificationToast.fire({
                            icon: 'error',
                            title: `La dirección ${current.street} ${current.number_ext} ${current.number_int} no tiene colonia, por favor selecciona una colonia.`
                        })
                        return false
                    }
                }
                NotificationToast.fire({
                    icon: 'success',
                    title: 'Formulario enviado correctamente'
                })
                
                let data_send = {
                    ...this.form,
                    'credit': this.credit_array,
                    'address': this.address,
                }
                if(!data_send.id)//remove key
                    delete data_send.id
                    
                let self = this
                method = this.form.id ? 'PATCH' : 'POST'
                saveFormAsync(this.url_endpoint_save_data, method, {
                    'data': JSON.stringify(data_send)
                }, function(data){
                    
                }, function(data){
                    const error = data.responseJSON;
                if (error) {
                let text = '';
                if (!error.address && !error.credit) {
                    text += '<b>Información del cliente</b><br>';
                    for (const key in error) {
                    text += `${error[key]}<br>`;
                    }
                } else if (error.address) {
                    text += '<b>Errores en direcciones:</b><br>';
                    error.address.forEach((current, i) => {
                    for (const key in current) {
                        text += `<b>Dirección ${i + 1}:</b>  ${current[key]}<br>`;
                    }
                    });
                } else if (error.credit) {
                    text += '<b>Errores en créditos:</b><br>';
                    error.credit.forEach((current, i) => {
                    for (const key in current) {
                        text += `<b>Crédito ${i + 1}:</b>  ${current[key]}<br>`;
                    }
                    });
                }

                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    html: text,
                });
                } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Algo salió mal, por favor intenta de nuevo',
                });
                }

                })
            }
        },
        components: {
            'address-component': AddressComponent,
            'table-component': tableComponent,
        },
        mounted(){
            if(this.$refs.formGeneral.action.includes('update')){
                let url = this.$refs.formGeneral.action
                let pk = url.split('/')[url.split('/').length - 2]
                let url_get = `/api/v1/clients/${pk}/complete/`
                let self = this
                getDataAsync(url_get,function(data){
                    address = data.address
                    credit = data.credit
                    delete data.address
                    delete data.credit
                    self.form = data
                    if (address && address.length > 0)
                        self.address = address
                    if (credit && credit.length > 0)
                        self.credit_array = credit
                })
            }
        }
    }).mount('#appVue')
})