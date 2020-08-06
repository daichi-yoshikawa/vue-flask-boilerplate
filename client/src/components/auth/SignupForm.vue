<template>
  <div>
    <div class="form-group">
      <div class="form-group">
        <label>Username*</label>
        <input type="text" class="form-control" v-model="username" placeholder="Enter username">
      </div>
      <div class="form-group">
        <label>Email Address*</label>
        <input type="email" class="form-control" v-model="email" placeholder="Enter your email address">
      </div>
      <div class="form-group">
        <label>Password*</label>
        <input type="password" class="form-control" v-model="password" placeholder="Create a password">
      </div>
      <div class="row mt-4">
        <div class="col-12">
          <button @click="onSubmit" class="float-right btn btn-primary">Sign Up</button>
        </div>
        <div class="col-12 text-right">
          <small>By signing up you agree to the <router-link to="/legal/terms-of-service">Terms of Service</router-link> and <router-link to="/legal/privacy-policy">Privacy Policy</router-link>.</small>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'signup-form',
    data: function() {
      return {
        username: '',
        email: '',
        password: '',
      };
    },
    methods: {
      onSubmit: function() {
        const form = {
          username: this.username,
          email: this.email,
          password: this.password,
        };
        console.log(JSON.stringify(form));
      },
    },
  }
</script>
