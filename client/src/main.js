import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue/dist/bootstrap-vue.esm'
import { sync } from 'vuex-router-sync'

import App from '@/App.vue'
import router from '@/router/router.js'
import store from '@/store/store.js'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'

Vue.use(BootstrapVue);
Vue.config.productionTip = false;
sync(store, router);

library.add(fas);
library.add(fab);
library.add(far);
Vue.component('font-awesome-icon', FontAwesomeIcon);

new Vue({
  el: '#app',
  router: router,
  store: store,
  render: h => h(App),
});
