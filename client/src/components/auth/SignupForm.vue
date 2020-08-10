<template>
  <div>
    <div class="form-group">
      <div class="form-group">
        <label>Username*</label>
        <input type="text"
               class="form-control"
               v-model="username"
               autocomplete="off"
               placeholder="Enter username">
      </div>
      <div class="form-group">
        <label>Email Address*</label>
        <input type="email"
               class="form-control"
               v-model="email"
               autocomplete="off"
               placeholder="Enter your email address">
      </div>
      <div class="form-group">
        <label>Password*</label>
        <input type="password"
               class="form-control"
               v-model="password"
               autocomplete="off"
               placeholder="Create a password">
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
  import client from '@/api/client'

  export default {
    name: 'signup-form',
    data: function() {
      return {
        url: 'http://localhost:5000/api/auth/signup',
        username: '',
        email: '',
        password: '',
        progress: false,
        error: '',
      };
    },
    methods: {
      onSubmit: async function() {
        const form = {
          username: this.username,
          email: this.email,
          password: this.password,
        };

        try {
          const res = await client.post(this.url);
          await console.log(res);
        } catch(err) {
          console.log(err);
        }
      },
    },
    computed: {

    }
  }
</script>
