import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/views/Dashboard.vue'

Vue.use(Router)
const routes = [
    {
        name: 'Dashboard',
        path: '/',
        component: Dashboard,
        icon: 'mdi-view-dashboard'
    }
]

const router = new Router({
    mode: 'hash',
    base: '',
    routes: routes
})


export {routes, router}