<template>
  <v-app>
    <router-view/>
  </v-app>
</template>

<script>
console.log('App loading...')
export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>

<style scoped>
@import 'css/bootstrap.css';
</style>