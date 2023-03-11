const { createApp, ref, defineComponent } = Vue

const tableComponent = defineComponent({
    props: {
        array_data: {
            type: Array,
            required: true
        },
        initial_data: {
            type: Object,
            required: true
        },
        text_button_add: {
            type: String,
            required: true
        },
        headers_table: {
            type: Array,
            required: true
        },
        title_table: {
            type: String,
            required: true
        }

    },
    computed: {
        len_header_table() {
            return this.headers_table.length
        },
    },
    delimiters: ['{$', '$}'],
    template: `
    <div class="row">
        <div class="col-12">
            <div class="card">
                <div class="card-header">
                    <div class="row">
                        <div class="col-6">
                            <h4 class="text-center">{$ title_table $}</h4>
                        </div>
                        <div class="col-6">
                            <a type="button" class="btn btn-primary text-white float-right" @click="array_data.push({...initial_data})">{$ text_button_add $}</a>
                        </div>
                    </div>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-12">
                            
                            <div class="table-responsive">
                                <table class="table table-striped table-bordered table-hover text-center">
                                    <thead>
                                        <tr>
                                            <th v-for="header in headers_table">{$ header $}</th>
                                            <th>Eliminar</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <slot name="body_table"></slot>
                                        <tr v-show="array_data.length == 0">
                                            <td :colspan="len_header_table + 1" class="text-center">No hay registrados</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>`
})