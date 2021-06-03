<template>
    <base-layout>
        <template v-slot:content>
            <new-phrase-form></new-phrase-form>
        </template>
    </base-layout>
  
</template>

<script>
    import BaseLayout from '@/containers/BaseLayout.vue'
    import NewPhraseForm from '../components/NewPhraseForm.vue'

    export default {
        name: 'NewPhrase',
        components: {
            BaseLayout,
            NewPhraseForm,
        },
        data: () => ({
        }),
       
    }
</script>
