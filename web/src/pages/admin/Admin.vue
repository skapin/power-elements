<template>
  <v-ons-page>
    <navbar enabled="false" navType="menu"></navbar>
    <div class="home-page" v-if="stats">
      <div v-for="(row, indexRow) in stats" v-bind:key="indexRow">
        <!-- chart vmodel stats -->
      </div>
    </div>
  </v-ons-page>
</template>

<script>
import Navbar from '../../components/navbar/Navbar';
import server from './../../api/server.vue'

export default {
  name: 'admin',
  components: {
    Navbar
  },
  data() {
    return {
      stats: []
    }
  },
  methods: {
    getStats () {
      server.getStats().then((result) => {
        this.stats = result.data
      })
    },
  },
  mounted: function () {
   this.getStats()
  },
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
</style>
