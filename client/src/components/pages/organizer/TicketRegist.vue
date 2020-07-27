<template>
  <div>
    <OrganizerMenuTemplate></OrganizerMenuTemplate>
    <div>
      <h2>チケット作成</h2>
    </div>
    <div>
      <TickerRegistForm :onticketregist="ticketRegist"></TickerRegistForm>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2';

import router from "../../../router";
import OrganizerMenuTemplate from "../OrganizerMenuTemplate"
import TickerRegistForm from "../../forms/TicketRegistForm"

export default {
  name: "Organizer",
  mounted() {
    this.checkLoggedIn();
  },
  components: {
    OrganizerMenuTemplate,
    TickerRegistForm
  },
  methods: {
    ticketRegist() {
      console.log('tiketRegist start...');
      var session_storage = JSON.parse(sessionStorage.getItem('vue-session-key'))

      //if (this.$refs.form.validate()) {
        this.loading = true;
        let config = {
          headers: {
            'Authorization': ' JWT ' + session_storage['token']
          }
        }
        console.log(config)

        axios.post('http://localhost:8000/api/ticket/', {'event_name': '東名阪ツアー', 'event_date': '2020-07-31', 'description': 'ネコプラ', 'ticket_type': 'VIP', 'ticket_quantity': 10, 'ticket_price': 10000}, config).then(res => {
          // this.$session.start();
          // this.$session.set('token', res.data.token);
          console.log(res)
          router.push('/');
        // eslint-disable-next-line
        }).catch(e => {
          this.loading = false;
          console.log(e);
          Swal.fire({
            type: 'warning',
            title: 'Error',
            text: 'チケットの登録情報に不備があります',
            showConfirmButton: true,
            showCloseButton: false,
            timer: 3000
          })
        })
      //}
      console.log('tiketRegist end...');
    },
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