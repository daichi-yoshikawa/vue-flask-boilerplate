import Vue from 'vue'
11;rgb:3030/0a0a/2424import VueRouter from 'vue-router'
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
