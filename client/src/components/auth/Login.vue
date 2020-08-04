<template>
  <div>
    <PageHeader/>
    <LoginForm/>
    <PageFooter/>
  </div>
</template>

<script>
  import PageHeader from '@/components/PageHeader'
  import PageFooter from '@/components/PageFooter'
  import LoginForm from '@/components/auth/LoginForm'

  export default {
    name: 'login',
    components: {
      PageHeader,
      PageFooter,
      LoginForm,
    },
  };
</script>
