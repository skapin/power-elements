<template>
      <transition name="slide-fade">
        <router-view></router-view>
      </transition>
</template>

<script>

export default {
  name: 'app',
  methods: {
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
