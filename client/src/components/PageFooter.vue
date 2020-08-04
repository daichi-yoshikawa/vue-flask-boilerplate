<template>
  <div>
    <b-navbar type="dark" variant="info">
      <footer class="py-5 text-small text-center mx-auto w-100">
        <div class="row">
          <div class="col-12">
            <h5>Contact Us</h5>
            <hr>
            <ul>
              <li>
                <font-awesome-icon :icon="['fas', 'envelope']" class="mr-2"/>xxx@yyy.zzz
              </li>
            </ul>
          </div>
        </div>
        <div>
          <p>Copyright &copy; XXXX All Rights Reserved.</p>
        </div>
      </footer>
    </b-navbar>
  </div>
</template>

<script>
  export default {
    name: 'page-footer',
  };
</script>

<style scoped>
  hr {
    max-width: 50%;
  }
</style>
