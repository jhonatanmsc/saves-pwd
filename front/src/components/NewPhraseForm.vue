<template>
    <v-container class="pr-md-15 pl-md-15">
        <h1>New phrase</h1>
        <validation-observer
            ref="observer"
            v-slot="{ invalid }"
        >
            <form @submit.prevent="submit">
            <validation-provider
                v-slot="{ errors }"
                name="key"
                rules="required|max:30"
            >
                <v-text-field
                v-model="key"
                :counter="30"
                :error-messages="errors"
                label="Key"
                required
                ></v-text-field>
            </validation-provider>
            <validation-provider
                v-slot="{ errors }"
                name="message"
                rules="required"
            >
                <v-text-field
                v-model="message"
                :error-messages="errors"
                label="Message"
                required
                ></v-text-field>
            </validation-provider>

            <v-combobox
            clearable
            filled
            hide-selected
            multiple
            small-chips
            v-model="select"
            :items="tags"
            label="Tags"
            ></v-combobox>

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
            key: '',
            message: '',
            tags: [],
            select: []
        }),
        mounted() {
            if (this.$route.query.id !== undefined)
                axios.get(parseUrl('phrase-detail', [this.$route.query.id]))
                    .then(res => {
                        this.key = res.data.key
                        this.message = res.data.message
                        this.select = res.data.tags
                    })
        },
        methods: {
            submit () {
                this.$refs.observer.validate()
                let payload = {
                    key: this.key,
                    message: this.message,
                    tags: this.select
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
            clear () {
                this.key = ''
                this.message = ''
                this.tags = []
                this.$refs.observer.reset()
            },
        },
    }
</script>
