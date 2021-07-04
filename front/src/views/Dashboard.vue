<template>
    <base-layout>
        <template v-slot:content>
            <v-container>
                <v-data-table
                    :headers="headers"
                    :items="phrases"
                    :items-per-page="10"
                    class="elevation-1"
                >
                <template v-slot:item.title={item}>
                    <phrase-detail :item="item"></phrase-detail>
                </template>
                <template v-slot:item.secrets={item}>
                    {{item.secrets}}
                </template>
                <template v-slot:item.actions={item}>
                    <remove-phrase-modal :item="item"></remove-phrase-modal>
                </template>
                </v-data-table>
            </v-container>
        </template>
    </base-layout>
  
</template>

<script>
    import BaseLayout from '@/containers/BaseLayout.vue'
    import {parseUrl} from '@/services/endpoints'
    import axios from 'axios'
    import * as moment from 'moment'
    import PhraseDetail from '../components/PhraseDetail.vue'
    import RemovePhraseModal from '../components/RemovePhraseModal.vue'

    export default {
        name: 'Dashboard',
        components: {
            BaseLayout,
            PhraseDetail,
            RemovePhraseModal
        },
        data: () => ({
            headers: [
                {
                    text: 'Title',
                    align: 'start',
                    sortable: false,
                    value: 'title',
                },
                { text: 'secrets', value: 'secrets' },
                { text: 'Created at', value: 'created_at' },
                { text: 'Actions', value: 'actions' },
            ],
            phrases: []
        }),
        mounted() {
            axios.get(parseUrl('phrase-list'))
                .then(res => this.phrases = res.data.map(p => {
                        p.created_at = moment(p.created_at).format('DD/MM/yyyy HH:mm:ss')
                        p.actions = null
                        return p
                    }))
                .catch(error => console.log(error))
        }
    }
</script>
