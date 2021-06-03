<template>
  <v-row>
    <router-link to="/" class="pl-5" @click.native="openModal">
        {{item.key}}
    </router-link>
    <v-dialog
      v-model="dialog"
      max-width="290"
    >
      <v-card>
        <v-card-title class="text-h5">
          {{item.key}}
        </v-card-title>
        <v-card-text>
            {{decodedMessage ? decodedMessage : item.message}} 
            
            <v-tooltip right v-model="tooltip">
                <template v-slot:activator="{}">
                    <v-btn
                    icon
                    color="blue darken-4"
                    @click="copy"
                    >
                    <v-icon small>mdi-clipboard-multiple-outline</v-icon>
                    </v-btn>
                </template>
                <span>copied!!</span>
            </v-tooltip>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="green darken-1"
            text
            @click="gotoEdit"
          >
            Edit
          </v-btn>
          <v-btn
            color="green darken-1"
            text
            @click="dialog = false"
          >
            Close
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
                dialog: false,
                tooltip: false,
                decodedMessage: null
            }
        },
        methods: {
            gotoEdit() {
                this.$router.push(`/new-phrase/?id=${this.item.id}`)
            },
            openModal() {
                this.dialog = true
                axios.get(parseUrl('phrase-decode', [this.item.id]))
                    .then(res => this.decodedMessage = res.data.message)
                    .catch(error => console.log(error))
            },
            copy() {
                navigator.clipboard.writeText(this.decodedMessage)
                this.tooltip = true
                setTimeout(() => this.tooltip = false, 700);
            }
        }
    }
</script>