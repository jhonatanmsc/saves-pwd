<template>
    <v-container class="pr-md-15 pl-md-15">
        <h1>New phrase</h1>
        <validation-observer
            ref="observer"
            v-slot="{ invalid }"
        >
            <form @submit.prevent="submit">
                <v-row>
                    <v-col md="12">
                        <validation-provider
                            v-slot="{ errors }"
                            name="title"
                            rules="required|max:30"
                        >
                            <v-text-field
                            v-model="title"
                            :counter="15"
                            :error-messages="errors"
                            label="Title"
                            required
                            ></v-text-field>
                        </validation-provider>
                    </v-col>
                </v-row>
                <v-row v-for="(secret, index) in secrets" :key="index">
                    <v-col md="12">
                        <h4>secret #{{index+1}}</h4>
                    </v-col>
                    <v-col md="3">
                        <validation-provider
                            v-slot="{ errors }"
                            :name="`key_${index}`"
                            rules="required|max:30"
                        >
                            <v-text-field
                            v-model="secret.key"
                            :counter="30"
                            :error-messages="errors"
                            label="Key"
                            required
                            ></v-text-field>
                        </validation-provider>
                    </v-col>
                    <v-col md="6">
                        <validation-provider
                            v-slot="{ errors }"
                            :name="`message_${index}`"
                            rules="required"
                        >
                            <v-text-field
                            v-model="secret.message"
                            :error-messages="errors"
                            label="Message"
                            required
                            ></v-text-field>
                        </validation-provider>
                    </v-col>
                    <v-col md="3">
                        <v-btn
                        icon
                        color="error"
                        :disabled="index === 0"
                        @click="rmSecret(index)"
                        >
                        <v-icon>mdi-trash-can-outline</v-icon>
                        </v-btn>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col md="12">
                        <v-btn
                        icon
                        color="warning"
                        @click="addSecret"
                        >
                        <v-icon>mdi-plus</v-icon>
                        </v-btn>
                    </v-col>
                    <v-col md="12">
                        <v-btn
                            class="mr-4"
                            type="submit"
                            :disabled="invalid"
                        >
                            submit
                        </v-btn>
                        <v-btn @click="clear">
                            clear
                        </v-btn>
                    </v-col>
                </v-row>
            </form>
        </validation-observer>
    </v-container>
  
</template>

<script>
    import {parseUrl} from '@/services/endpoints'
    import axios from 'axios'
    import { required, max } from 'vee-validate/dist/rules'
    import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'

    setInteractionMode('eager')

    extend('required', {
        ...required,
        message: '{_field_} can not be empty',
    })

    extend('max', {
        ...max,
        message: '{_field_} may not be greater than {length} characters',
    })

    export default {
        name: 'NewPhraseForm',
        components: {
            ValidationProvider,
            ValidationObserver,
        },
        data: () => ({
            title: '',
            secrets: [{key: "", message: ""}],
        }),
        mounted() {
            if (this.$route.query.id !== undefined)
                axios.get(parseUrl('phrase-detail', [this.$route.query.id]))
                    .then(res => {
                        this.title = res.data.title
                        this.secrets = res.data.secrets
                    })
        },
        methods: {
            submit () {
                this.$refs.observer.validate()
                let payload = {
                    title: this.title,
                    secrets: this.secrets
                }
                if (this.$route.query.id === undefined)
                    axios.post(parseUrl('phrase-create'), payload)
                        .then(() => this.$router.push('/'))
                        .catch(error => console.log(error))
                else 
                    axios.put(parseUrl('phrase-update', [this.$route.query.id]), payload)
                        .then(() => this.$router.push('/'))
                        .catch(error => console.log(error))
            },
            addSecret () {
                this.secrets.push({key: "", message: ""})
            },
            rmSecret (index) {
                this.secrets.splice(index, 1)
            },
            clear () {
                this.title = ''
                this.secrets = [{key: "", message: ""}]
                this.$refs.observer.reset()
            },
        },
    }
</script>
