<template>
  <div>
    <OrganizerMenuTemplate></OrganizerMenuTemplate>
    <div>
      <h2>オーガナイザーメニュー</h2>
    </div>
  </div>
</template>

<script>
import router from "../../../router";
import OrganizerMenuTemplate from "../OrganizerMenuTemplate"
export default {
  name: "Organizer",
  mounted() {
    this.checkLoggedIn();
  },
  components: {
    OrganizerMenuTemplate
  },
  methods: {
    checkLoggedIn() {
      console.log('オーガナイザーメニュー')
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push('/auth');
      }
    },
  }
};
</script>