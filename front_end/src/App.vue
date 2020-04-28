<template>
<v-ons-page id="app">
  <router-view></router-view>
  <v-ons-splitter>
    

    <v-ons-splitter-content>
      <transition name="slide-fade">
        <router-view></router-view>
      </transition>
    </v-ons-splitter-content>
  </v-ons-splitter>
</v-ons-page>
</template>

<script>
import SideMenu from './components/side-menu/SideMenu';
import store from './store';

export default {
  name: 'app',
  store,
  data() {

  },
  computed: {
    menuIsOpen() {
      return store.state.menuIsOpen;
    },
  },
  components: {
    SideMenu,
  },
  methods: {
    onUserInteraction(event) {
      console.log(event);   // on click ons-splitter-side-mask, event always false(?)
      store.commit('toggleMenu', event);
    },
    toggleMenu() {
      this.$store.commit('toggleMenu', true);
    },
    getIfLoggedIn () {
      return !_.isEmpty(window.localStorage.getItem('jwtToken'))
    },
  },
  mounted: function () {
    if(this.getIfLoggedIn()) {
      this.goTo('home')
    } else {
      this.goTo('loginPage')
    }
  },
};
</script>

<style lang="scss" scoped>
.header {
  text-align: center;
  margin-bottom: 20px;
}
img {
  max-width: 150px;
}
ons-list-item {
  cursor: pointer;
}
ons-list-item {
  cursor: pointer;
}
navbar {
  margin-bottom:100px;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
.slide-fade-enter-active {
  transition: all .3s ease;
}
.slide-fade-leave-active {
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to {
  transform: translateX(10px);
  opacity: 0;
}
</style>
