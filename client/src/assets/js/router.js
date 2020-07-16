import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '@/components/Index.vue'

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Index,
  },
];

export default new VueRouter({
  routes: routes,
});
