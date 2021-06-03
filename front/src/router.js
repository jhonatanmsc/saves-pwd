import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/views/Dashboard.vue'
import NewPhrase from '@/views/NewPhrase.vue'

Vue.use(Router)
const routes = [
    {
        name: 'Dashboard',
        path: '/',
        component: Dashboard,
        icon: 'mdi-view-dashboard'
    },
    {
        name: 'New Phrase',
        path: '/new-phrase',
        component: NewPhrase,
        icon: 'mdi-form-textbox-password'
    }
]

const router = new Router({
    mode: 'hash',
    base: '',
    routes: routes
})


export {routes, router}