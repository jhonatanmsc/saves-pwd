<template>
  <v-row>
    <v-btn
    icon
    color="red lighten-2"
    @click="openModal"
    >
    <v-icon>mdi-trash-can-outline</v-icon>
    </v-btn>
    <v-dialog
      v-model="dialog"
      max-width="290"
    >
      <v-card>
        <v-card-title class="text-h5">
          You really want delete this phrase?
        </v-card-title>
        <v-card-text class="red--text darken-4">{{item.key}}</v-card-text>
        
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="green darken-1"
            text
            @click="remove"
          >
            remove
          </v-btn>
          <v-btn
            color="green darken-1"
            text
            @click="dialog = false"
          >
            close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
    import axios from 'axios';
    import {parseUrl} from '@/services/endpoints'
    export default {
        props: ['item'],
        data () {
            return {
                dialog: false
            }
        },
        methods: {
            remove() {
                axios.delete(parseUrl('phrase-delete', [this.item.id]))
                    .then(() => window.location.reload(true))
                    .catch(error => console.log(error))
            },
            openModal() {
                this.dialog = true
                axios.get(parseUrl('phrase-decode', [this.item.id]))
                    .then(res => this.decodedMessage = res.data.message)
                    .catch(error => console.log(error))
            }
        }
    }
</script>