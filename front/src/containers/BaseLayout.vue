<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <side-menu :items=items></side-menu>
    </v-navigation-drawer>

    <v-app-bar height="66px" app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Application</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <slot name="content"></slot>
    </v-main>
  </v-app>
</template>

<script>
  import SideMenu from '@/components/SideMenu.vue'
  import {routes} from '@/router'
  export default {
    components: {
      SideMenu
    },
    data: () => ({ 
      items: routes.map(route => ({
        title: route.name, 
        icon: route.icon,
        path: route.path
      })),
      drawer: null 
    }),
    mounted() {

    }
  }
</script>