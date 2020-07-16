<template>
  <div class="page-header">
    <nav class="navbar navbar-expand-md navbar-dark bg-dark sticky-top">
      <div class="container">
        <router-link to="/" class="navbar-brand mb-0 h1 font-weight-bold">
          <img class="mr-2" src="../assets/img/logo.png">VueWebApp
        </router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="navbar-responsive">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbar-responsive">
          <ul class="nav navbar-nav text-right ml-auto">
            <li v-for="(route, i) in $router.options.routes" :key="i" class="nav-item">
              <router-link :to="{ path: route.path }" :class="{ active: route.path === $router.currentRoute.path }">
                <span class="navbar-brand">{{ route.name }}</span>
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
  export default {
    name: 'PageHeader',
  };
</script>

<style scoped>
  nav img {
    width: 30px;
  }
</style>
