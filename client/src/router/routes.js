import Auth from '@/components/pages/Auth.vue'
import Users from '@/components/pages/users/IndexView.vue'
import UsersReserveTicket from '@/components/pages/users/ReserveTicketView.vue'
import Organizer from '@/components/pages/organizer/IndexView.vue'
import TicketRegist from '@/components/pages/organizer/TicketRegist.vue'

export default [
    {
      path: '/users/reserve_ticket',
      name: 'UsersReserveTicket',
      component: UsersReserveTicket
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    },
    {
      path: '/organizer/',
      name: 'Organizer',
      component: Organizer
    },
    {
      path: '/organizer/ticker-regist',
      name: 'Ticker-Regist',
      component: TicketRegist
    },
    {
      path: '/',
      name: 'Users',
      component: Users
    },
]