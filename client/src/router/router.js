import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '@/components/Index'
import NotFound from '@/components/NotFound'

import PrivacyPolicy from '@/components/legal/PrivacyPolicy'
import TermsOfService from '@/components/legal/TermsOfService'

import Login from '@/components/auth/Login'
import Signup from '@/components/auth/Signup'

import AppIndex from '@/components/app/Index'

Vue.use(VueRouter);

const appName = 'WebApp'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Index,
    meta: {
      title: appName,
      requireAuth: false,
    },
  },
  {
    path: '/legal/privacy-policy',
    name: 'privacy-policy',
    component: PrivacyPolicy,
    meta: {
      title: appName + ' | Privacy Policy',
      requireAuth: false,
    },
  },
  {
    path: '/legal/terms-of-service',
    name: 'terms-of-service',
    component: TermsOfService,
    meta: {
      title: appName + ' | Terms of Service',
      requireAuth: false,
    },
  },
  {
    path: '/auth/signup',
    name: 'signup',
    component: Signup,
    meta: {
      title: appName + ' | Signup',
      requireAuth: false,
    },
  },
  {
    path: '/auth/login',
    name: 'login',
    component: Login,
    meta: {
      title: appName + ' | Login',
      requireAuth: false,
    },
  },
  {
    path: '/app',
    name: 'app-index',
    component: AppIndex,
    meta: {
      title: appName + ' | App',
      requireAuth: true,
    },
  },
  {
    path: '/404',
    name: 'not-found',
    component: NotFound,
    meta: {
      title: appName + ' | Page Not Found',
      requireAuth: false,
    },
  },
  {
    path: '*',
    redirect: '/404',
  },
];

const router = new VueRouter({
  routes: routes,
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  next();
});

export default router;
