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
    },
  },
  {
    path: '/legal/privacy-policy',
    name: 'privacy-policy',
    component: PrivacyPolicy,
    meta: {
      title: appName + ' | Privacy Policy',
    },
  },
  {
    path: '/legal/terms-of-service',
    name: 'terms-of-service',
    component: TermsOfService,
    meta: {
      title: appName + ' | Terms of Service',
    },
  },
  {
    path: '/auth/signup',
    name: 'signup',
    component: Signup,
    meta: {
      title: appName + ' | Signup',
    },
  },
  {
    path: '/auth/login',
    name: 'login',
    component: Login,
    meta: {
      title: appName + ' | Login',
    },
  },
  {
    path: '/app',
    name: 'app-index',
    component: AppIndex,
  },
  {
    path: '/404',
    name: 'not-found',
    component: NotFound,
    meta: {
      title: appName + ' | Page Not Found',
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

export default router;
