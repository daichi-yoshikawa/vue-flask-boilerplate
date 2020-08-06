<template>
  <div>
    <PageHeader/>
    <div class="card mx-auto my-5">
      <div class="card-header text-center">
        <h4>Sign Up Today</h4>
      </div>
      <div class="card-body">
        <SignupForm/>
      </div>
    </div>
    <PageFooter/>
  </div>
</template>

<script>
  import PageHeader from '@/components/PageHeader'
  import PageFooter from '@/components/PageFooter'
  import SignupForm from '@/components/auth/SignupForm'

  export default {
    name: 'signup',
    components: {
      PageHeader,
      PageFooter,
      SignupForm,
    },
  };
</script>

<style scoped>
  .card {
    max-width: 640px;
  }
</style>
