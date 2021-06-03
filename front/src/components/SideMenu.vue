<template>
  <div>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="text-h6">
          PWD
        </v-list-item-title>
        <v-list-item-subtitle>
          api: {{API_BASE_URL}}
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>

    <v-divider></v-divider>

    <v-list
      dense
      nav
    >
      <v-list-item
        v-for="item in items"
        :key="item.title"
        link
        :to="item.path"
      >
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </div>
</template>

<script>
  import {API_URL} from '@/services/endpoints' 
  export default {
    props: ['items'],
    data () {
      return {
        right: null,
        API_BASE_URL: API_URL
      }
    },
  }
</script>