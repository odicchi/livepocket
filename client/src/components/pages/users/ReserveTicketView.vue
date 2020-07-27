<template>
  <div>
    <UserMenuTemplate></UserMenuTemplate>
    <div>
      <h2>ユーザーメニュー購入済みチケット</h2>
    </div>
    <router-view />
  </div>
</template>

<script>
import router from "../../../router";
import UserMenuTemplate from '../UserMenuTemplate.vue'

console.log('reserve_ticket loading...')
export default {
  name: "UsersReserveTicket",
  mounted() {
    this.checkLoggedIn();
  },
  components: {
    UserMenuTemplate
  },
  methods: {
    checkLoggedIn() {
      console.log('ユーザーメニュー_購入済みチケット')
      this.$session.start();
      if (!this.$session.has("token")) {
        console.log('未ログインのため認証画面へ')
        router.push('/auth');
      }
    }
  }
};
</script>