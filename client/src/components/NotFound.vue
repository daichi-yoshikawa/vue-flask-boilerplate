<template>
  <div>
    <PageHeader/>
    <div class="container text-center">
      <p class="display-3 my-5 py-5"><strong>404</strong> Page Not Found</p>
    </div>
    <PageFooter/>
  </div>
</template>

<script>
  import PageHeader from '@/components/PageHeader'
  import PageFooter from '@/components/PageFooter'

  export default {
    name: 'not-found',
    components: {
      PageHeader,
      PageFooter,
    },
  };
</script>
