<template>
<v-app>
  <div id="app">
    <UserMenuTemplate></UserMenuTemplate>
    <div>
      <h2>ユーザーメニュー</h2>
    </div>
    <router-view />
  </div>
</v-app>
</template>

<script>
console.log('users index loading...')
import router from "../../../router";
import UserMenuTemplate from '../UserMenuTemplate'

export default {
  name: "UserMenuIndex",
  mounted() {
    this.checkLoggedIn();
  },
  components: {
    UserMenuTemplate
  },
  methods: {
    checkLoggedIn() {
      this.$session.start();
      if (!this.$session.has("token")) {
        console.log('ユーザーメニュー')
        router.push('/auth');
      }
    }
  }
};
</script>