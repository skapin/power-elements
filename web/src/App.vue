<template>
<v-ons-page class="ma_page_app">
  <v-ons-splitter>
    <v-ons-splitter-side swipeable collapse width="250px" :open.sync="menuIsOpen">
      <side-menu></side-menu>
    </v-ons-splitter-side>
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
  computed: {
    menuIsOpen: {
        // getter
      get: function () {
        return store.state.menuIsOpen
      },
        // setter
      set: function (newValue) {
        store.commit('toggleMenu');
      }
    }
  },
  components: {
    SideMenu,
  },
  methods: {
    onUserInteraction(event) {   // on click ons-splitter-side-mask, event always false(?)
      store.commit('toggleMenu', event);
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

<style>



.header {
  text-align: center;

}
ons-list-item {
  cursor: pointer;
}
ons-list-item {
  cursor: pointer;
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

.ma_page_app {
  background-color: red !important;
  /* background: linear-gradient(#61d7ff, #2667a8) !important; */

}
</style>
