console.log('router.js loading start...')
import Vue from 'vue'
import Router from 'vue-router'
import routes from './router/routes'


Vue.use(Router)

export default new Router({routes})
console.log('router.js loading end...')