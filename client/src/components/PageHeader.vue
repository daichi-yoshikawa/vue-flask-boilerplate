<template>
  <div>
    <b-navbar toggleable="md" type="dark" variant="info">
      <div class="container">
        <b-navbar-brand>
          <router-link to="/" class="navbar-brand mb-0 h1 font-weight-bold">
            <img class="mr-2" :src="require('@/img/logo.png')">VueWebApp
          </router-link>
        </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <ul class="navbar-nav text-right ml-auto">
              <li v-for="(route, i) in $router.options.routes" :key="i" class="nav-item">
                <b-nav-item v-if="route.meta && (route.meta.isNavItem === true)">
                  <router-link :to="{ path: route.path }" :class="{ active: route.path === $router.currentRoute.path }">
                    <span class="navbar-brand">{{ route.name }}</span>
                  </router-link>
                </b-nav-item>
              </li>
            </ul>
          </b-navbar-nav>

          <b-navbar-nav class="ml-auto">
            <b-nav-item>
              <router-link to="/auth/login"><b-button>Sign In</b-button></router-link>
            </b-nav-item>
            <b-nav-item>
              <router-link to="/auth/signup"><b-button>Sign Up</b-button></router-link>
            </b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </div>
    </b-navbar>
  </div>
</template>

<script>
  export default {
    name: 'page-header',
  };
</script>

<style scoped>
  .container {
    max-width: 100%;
  }

  nav img {
    width: 30px;
  }
</style>
