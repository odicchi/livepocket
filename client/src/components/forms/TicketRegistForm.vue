<template>
  <form novalidate>
    <h3>チケット情報の入力</h3>
    <br><br>
    <div class="inputForm">
      <p v-if="error" class="login-error"> {{ error }}</p>
      <table border="2">
        <tr>
          <td>
              <label for="eventName">イベント名</label>
          </td>
          <td>
            <input
              v-model="eventName"
              autocomplete="off"
              placeholder="例：東名阪ツアー"
            >
          </td>
        </tr>
        <tr>
          <td>
            <label for="eventDate">開催日</label>
          </td>
          <td>
            <v-date-picker></v-date-picker>
          </td>
        </tr>
        <tr>
          <td>
            <label for="description">説明文</label>
          </td>
          <td>
            <textarea rows="10" cols="50"></textarea>
          </td>
        </tr>
      </table>
    </div>
    <br>
    <h3>チケット種別の入力</h3>
    <div class="inputForm">
      <table>
        <tr>
          <td><label for="ticketType">チケット種別</label></td>
          <td><label for="ticketQuantity">数量</label></td>
          <td><label for="ticketPrice">価格</label></td>
        </tr>
        <tr>
          <td>
            <input
              v-model="ticketType"
              autocomplete="off"
              placeholder="例：Aチケット"
            >
          </td>
          <td>
            <input
              v-model="ticketQuantity"
              type="number"
              autocomplete="off"
              placeholder="例：1000"
            >
          </td>
          <td>
            <input
              v-model="ticketPrice"
              type="number"
              autocomplete="off"
              placeholder="例：3500"
            >
          </td>
        </tr>
      </table>
    </div>
    <br><br>
    <div class="form-actions">
      <TicketRegistBtn
        @click="ticketRegist"
      >
      チケット登録
      </TicketRegistBtn>
    </div>
    <br><br>
  </form>
</template>

<script>
import TicketRegistBtn from '@/components/parts/TicketRegistBtn'

const required = val => !!val.trim()

export default {
  name: 'RegistTicketForm',

  props: {
    onticketregist: {
      type: Function,
      required: true
    }
  },

  data () {
    return {
      eventName: '',
      eventDate: '',
      description: '',
      ticketType: '',
      ticketQuantity: '',
      ticketPrice: '',
      error: ''
    }
  },

  computed: {
    validation () {
      return {
        eventName: {
          required: required(this.eventName)
        },
        eventDate: {
          required: required(this.eventDate)
        },
        description: {
          required: required(this.description)
        },
        ticketType: {
          required: required(this.ticketType)
        },
        ticketQuantity: {
          required: required(this.ticketQuantity)
        },
        ticketPrice: {
          required: required(this.ticketPrice)
        }
      }
    },
    disableTicketRegist () {
      console.log('[TiketRegistForm] [computed] disableTicketRegist start...')
      console.log('!this.eventName  :' + !this.eventName)
      console.log('!this.eventDate  :' + this.eventDate)
      console.log('!this.description:' + this.description)
      return !this.eventName || this.eventDate || this.description
    }
  },

  components: {
    TicketRegistBtn
  },

  methods: {
    ticketRegist () {
      console.log('[TiketRegistForm] [methods] ticketRegist start...')
      if (this.disableTicketRegist) { return }
      console.log('[TiketRegistForm] [computed] disableTicketRegist end...')

      this.error = ''

      this.$nextTick(() => {
        console.log('[TiketRegistForm] [methods] ticketRegist $nextTick start...')
        this.onticketregist({ eventName: this.eventName, eventDate: this.eventDate, description: this.description,
          ticketType: this.ticketType, ticketQuantity: this.ticketQuantity, ticketPrice: this.ticketPrice})
        .catch(err => {
          console.error(err.message)
          this.error = err.message
        })
      })
      console.log('[TiketRegistForm] [methods] ticketRegist end...')
    }
  }
}
</script>
<style scoped>
.inputForm {
  left:40%;
  padding-left:8px;
  padding-right:8px;
  padding-top:8px;
  border:5px solid #E0E0E0;
  background-color:#FFFFFF;
  z-index:2;
}

.inputForm table {
  position: relative;
  left: 40%;
}
</style>