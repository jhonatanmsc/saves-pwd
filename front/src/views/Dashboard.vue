<template>
    <base-layout>
        <template v-slot:content>
            <v-container>
                <v-data-table
                    :headers="headers"
                    :items="phrases"
                    :items-per-page="5"
                    class="elevation-1"
                ></v-data-table>
            </v-container>
        </template>
    </base-layout>
  
</template>

<script>
    import BaseLayout from '@/containers/BaseLayout.vue'
    import {parseUrl} from '@/services/endpoints'
    import axios from 'axios'
    import * as moment from 'moment'

    export default {
        name: 'Dashboard',
        components: {
            BaseLayout
        },
        data: () => ({
            headers: [
                {
                    text: 'Key',
                    align: 'start',
                    sortable: false,
                    value: 'key',
                },
                { text: 'Message', value: 'message' },
                { text: 'Tags', value: 'tags' },
                { text: 'Created at', value: 'created_at' },
            ],
            phrases: []
        }),
        mounted() {
            axios.get(parseUrl('phrase-list'))
                .then(res => this.phrases = res.data.map(p => {
                        p.created_at = moment(p.created_at).format('DD/MM/yyyy HH:mm:ss')
                        return p
                    }))
                .catch(error => console.log(error))
        }
    }
</script>
