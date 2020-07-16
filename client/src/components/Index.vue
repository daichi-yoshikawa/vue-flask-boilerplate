<template>
  <div class="index">
    <PageHeader/>
    <div class="container">
      <p class="my-5 py-5 lead text-center">This is an index page.</p>
    </div>
    <PageFooter/>
  </div>
</template>

<script>
  import PageHeader from './PageHeader'
  import PageFooter from './PageFooter'

  export default {
    name: 'Index',
    components: {
      PageHeader,
      PageFooter,
    },
  };
</script>
