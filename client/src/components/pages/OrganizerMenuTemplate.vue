<template>
  <div class="bs-component">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <router-link class="navbar-brand" to="/">Live Pocket</router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor03" aria-controls="navbarColor03" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarColor03">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <router-link class="nav-link" to="/">トップ <span class="sr-only">(current)</span></router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/organizer/ticker-regist">チケットを作成する</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="#">リンク</router-link>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              サブメニュー
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item" href="#">矢澤にこ</a>
              <a class="dropdown-item" href="#">東條希</a>
              <a class="dropdown-item" href="#">絢瀬絵里</a>
            </div>
          </li>
        </ul>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
console.log('OrganizerMenuTemplate loading...')

export default {
  name: 'OrganizerMenuTemplate',
  components: {
  },
  data: () => ({
    //
  }),
};
</script>
<style>
@import '../../css/bootstrap.css';
</style>