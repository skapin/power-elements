<template>
  <v-ons-page>
    <navbar enabled="false" navType="menu"></navbar>
    <div class="home-page">
    </div>
  </v-ons-page>
</template>

<script>
import Navbar from "../../components/navbar/Navbar";

export default {
  name: "posts-page",
  components: {
    Navbar
  },
  data() {
    return {
      qcmAnswers: {},
      questionsList: [],
      validateDisabled: true,
      loading: false
    };
  },
  methods: {
  },
  mounted: function() {
  }
};
</script>

<style lang='scss' scoped>
.page-title {
  text-align: center;
}

.btn:hover {
  cursor: pointer;
}
.home-page {
  max-width: 1200px;
  margin: auto;
  min-height: calc(100vh - 44px);
}
.validation-button {
  width: 50%;
  min-width: 300px;
  margin: 0 auto;
  margin-bottom: 1%;
  margin-top: 3%;
}
</style>
