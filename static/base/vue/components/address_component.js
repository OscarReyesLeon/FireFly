const AddressComponent = defineComponent({
    props: {
        address_array: {
            type: Array,
            required: true
        },
        title_table: {
            type: String,
            required: true
        },
    },
    data() {
        const form_select_initial = {
            show: false,
            options_state: [],
            options_municipality: [],
            options_neighborhood: [],
            state_selected: '',
            municipality_selected: '',
            neighborhood_selected: '',
            accept: false,
            instance: null,
            index: null,
        }

        const initialAddress = {
            street: '',
            number_ext: '',
            number_int: '',
            neighborhood: '',
            reference: '',
        }

        return {
            initialAddress,
            text_button_add: "Agregar dirección",
            headers_table: ['Calle', 'Número exterior', 'Número interior', 'Colonia', 'Referencia'],
            form_select_initial,
            form_select: ref({ ...form_select_initial }),
            url_address: '/api/v1/address/'
        }
    },
    computed: {
        label_empty() {
            return this.address_array.length == 0 ? true : false
        },
    },
    methods: {
        delete_address(index) {
            this.address_array.splice(index, 1)
        },
        change_neighborhood(current_value, index) {
            this.instance = current_value
            this.form_select.show = true
            this.form_select.index = index
            if (current_value.neighborhood)
                this.form_select.state_selected = this.search_value_select(this.form_select.options_state, current_value.neighborhood.state_id)

        },
        search_value_select(array, value) {
            return array.find((element) => {
                return element.id == value
            })

        },
        async get_values_by_select(value_select, extra_url) {
            let options_select = []
            if (!value_select) return options_select
            await getDataAsync(this.url_address + extra_url + value_select.id, (data) => {
                options_select = data
            })
            return options_select
        },
        confirm_neighborhood(confirm_value) {
            if (confirm_value == true)
                this.address_array[this.form_select.index].neighborhood = this.form_select.neighborhood_selected;
            Object.assign(this.form_select, this.form_select_initial, {
                'options_state': this.form_select.options_state,
            });
        },
    },
    watch: {
        "form_select.state_selected": async function (value) {
            this.form_select.municipality_selected = ''
            this.form_select.neighborhood_selected = ''
            this.form_select.options_municipality = await this.get_values_by_select(value, 'municipality/?state_id=')

            if (this.instance.neighborhood && this.instance.neighborhood.municipality_id)
                this.form_select.municipality_selected = this.search_value_select(this.form_select.options_municipality, this.instance.neighborhood.municipality_id)
        },
        "form_select.municipality_selected": async function (value) {
            this.form_select.neighborhood_selected = ''
            this.form_select.options_neighborhood = await this.get_values_by_select(value, 'neighborhood/?municipality_id=')
            if (this.instance.neighborhood && this.instance.neighborhood.id)
                this.form_select.neighborhood_selected = this.search_value_select(this.form_select.options_neighborhood, this.instance.neighborhood.id)
        },
    },
    delimiters: ['{$', '$}'],
    template: `
    <div v-show="!form_select.show">
        <table-component 
            :array_data=address_array 
            :initial_data=initialAddress 
            :text_button_add=text_button_add :headers_table=headers_table
            :title_table=title_table
            >
                <template #body_table  >
                
                    <tr v-for="(address_current, index) in address_array">
                        <td>
                            <input type="text" class="form-control" v-model="address_current.street" required>
                        </td>
                        <td>
                            <input type="text" class="form-control" v-model="address_current.number_ext" required>
                        </td>
                        <td>
                            <input type="text" class="form-control" v-model="address_current.number_int">
                        </td>
                        <td>
                            <div class="input-group mb-3">
                                <input type="text" class="form-control" 
                                    placeholder="Colonia" :value="address_current.neighborhood.name" readonly required>
                                <div class="input-group-prepend">
                                    <button class="btn btn-outline-secondary" type="button" @click="change_neighborhood(address_current, index)">
                                        <i class="fas fa-search"></i>
                                        {$ !address_current.neighborhood.name ? 'Agregar' : 'Cambiar' $}
                                    </button>
                                </div>
                            </div>
                        </td>
                        <td>
                            <input type="text" class="form-control" v-model="address_current.reference">
                        </td>
                        <td>
                            <a type="button" class="btn btn-danger text-white" @click="address_array.splice(index,1)">Eliminar</a>
                        </td>
                    </tr>
                </template>
        
        </table-component>
    </div>

    <div class="row" v-show="form_select.show">
        <div class="col-12">
            <div class="card">
                <div class="card-title">
                    <h4 class="text-center">Encontrar colonia</h4>
                </div>
                <div class="card-body">
                    <div class="row">
                    <div class="col-4">
                        <label for="state">Estado de la republica</label> 
                        <v-select :options="form_select.options_state" label="name" 
                            placeholder="Selecciona un estado"
                            v-model="form_select.state_selected"></v-select>
                        </div>
                        <div class="col-4">
                            <label for="municipality">Municipio</label> 
                            <v-select :options="form_select.options_municipality" 
                            placeholder="Selecciona un municipio"
                            label="name" v-model="form_select.municipality_selected"></v-select>
                        </div>
                        <div class="col-4">
                            <label for="neighborhood">Colonia</label> 
                            <v-select :options="form_select.options_neighborhood" 
                            placeholder="Selecciona una colonia"
                            label="name" v-model="form_select.neighborhood_selected"></v-select>
                        </div>
                    </div>
                </div>
                <div class="card-footer">
                    <div class="row">
                        <div class="col-6">
                            <a type="button" class="btn btn-primary btn-block text-white float-right mt-3 align-center float-right"
                                v-show="form_select.neighborhood_selected"
                            @click="confirm_neighborhood(true)"
                            >Confirmar colonia</a>
                        </div>
                        <div class="col-6">
                            <a type="button" class="btn btn-danger btn-block text-white float-right mt-3 align-center float-right"
                            @click="confirm_neighborhood(false)"
                            >Cancelar</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    `,
    components: {
        'table-component': tableComponent,
        'v-select': window["vue-select"],
    },
    mounted() {
        let self = this
        getDataAsync(this.url_address + 'state/', function(data){
            self.form_select.options_state = data
        })
    }
})