<template>
  <v-ons-page>
    <navbar enabled="false"></navbar>
    <div class="home-page">
      <question></question>
      <question></question>
      <question></question>
      <question></question>
      <question></question>
      <question></question>
      <question></question>
    </div>
  </v-ons-page>
</template>

<script>
import Navbar from '../../components/navbar/Navbar';
import Question from '../../components/Qcm/question'

export default {
  name: 'posts-page',
  components: {
    Navbar,
    Question
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
.home-page {
  height: 100vh;
  overflow: auto;
  background: linear-gradient(#61d7ff, #2667a8);
}
</style>
