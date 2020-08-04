<template>
  <div>
    <PageHeader/>
    <SignupForm/>
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
