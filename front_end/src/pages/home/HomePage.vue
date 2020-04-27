<template>
  <v-ons-page>
    <navbar></navbar>
    <p>HELLO WORLD</p>
  </v-ons-page>
</template>

<script>
import Navbar from '../../components/navbar/Navbar';

export default {
  name: 'posts-page',
  components: {
    Navbar
  },
  data() {
    return {
      striker: {
      }
    }
  },
  methods: {
  },
  computed: {
  }
};
</script>

<style lang='scss' scoped>
.page-title {
  text-align: center;
}
.body {
  margin-top: 50px;
}
</style>
