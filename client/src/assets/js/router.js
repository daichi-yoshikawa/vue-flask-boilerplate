import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '@/components/Index.vue'

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    meta: {
      title: 'App Title',
    },
    component: Index,
  },
];

const router = new VueRouter({
  routes: routes,
});

export default router;
