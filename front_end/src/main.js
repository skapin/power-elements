import Element from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import locale from 'element-ui/lib/locale/lang/ja';

import Vue from 'vue';
import VueOnsen from 'vue-onsenui';
import VueRouter from 'vue-router';
import axios from 'axios';
import VueAxios from 'vue-axios';
import 'onsenui/css/onsenui.css';
import App from './App';
import routes from './routes';
import store from './store';
import Toasted from 'vue-toasted'

import 'onsenui/css/onsen-css-components.css';
// import '../static/css/onsen-css-components-pink.min.css';

Vue.config.productionTip = false;

require('lodash')
Vue.use(Element, { locale });
Vue.use(VueOnsen);
Vue.use(VueRouter);
Vue.use(VueAxios, axios);
Vue.use(Toasted)

const router = new VueRouter({
  mode: 'hash',
  base: window.location.href,
  routes, // short for `routes: routes`
});

Vue.mixin({
  data () {
    return {
      alphabet: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    }
  },
  methods: {
    goTo(routeName) {
      this.$router.push({ name: routeName });
      store.commit('toggleMenu', false);
    },
  }
})

new Vue({
  components: {
    App,
  },
  template: '<App/>',
  router,
}).$mount('#app');


/* eslint-disable no-new */
// new Vue({
//   el: '#app',
//   template: '<App/>',
//   router,
//   components: { App },
// });
