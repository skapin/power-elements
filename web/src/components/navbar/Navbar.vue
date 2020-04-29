<template>
  <v-ons-toolbar class="home-toolbar">
    <div v-if="navType=='menu'" class="left">
      <v-ons-toolbar-button @click="toggleMenu()" class="btn">
        <v-ons-icon icon="ion-navicon, material:md-menu"></v-ons-icon>
      </v-ons-toolbar-button>
    </div>
    <div v-else-if="navType=='back'" class="left">
      <v-ons-button v-if="enabled == 'true'"
                    @click="goTo(returnPath)"
                    modifier="quiet"
                    class="btn"
                    style="margin: 3px 0">
        <v-ons-icon size="50px" icon="md-caret-left"></v-ons-icon>
      </v-ons-button>
    </div>
    <div class="center" style="color: white; font-size: 15px;font-weight:800;">{{ msg }}</div>
  </v-ons-toolbar>
</template>

<script>
export default {
  name: 'navbar',
  props: {
    msg: {
      default: 'Covid-19 AIO',
    },
    navType: {
      default: 'back',
    },
    returnPath: {
      default: 'home',
    },
    enabled: {
      default: 'true'
    }
  },
  methods: {
    toggleMenu() {
      this.$store.commit('toggleMenu');
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
.home-toolbar {
  background-color: #2667a8;
}

.btn {
  color: white !important;
}

.btn:hover {
  cursor: pointer;
}

  .header {
    text-align: center;
   
  }
 
  ons-list-item {
    cursor: pointer;
  }
</style>