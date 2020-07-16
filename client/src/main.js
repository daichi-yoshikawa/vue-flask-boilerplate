import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue/dist/bootstrap-vue.esm'

import App from '@/components/App.vue'
import router from '@/assets/js/router.js'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue);
Vue.config.productionTip = false;

new Vue({
  el: '#app',
  router: router,
  render: h => h(App),
});
