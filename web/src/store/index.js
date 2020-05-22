import Vue from 'vue';
import Vuex from 'vuex';
import userInfo from './modules/userInfo';
import user from './modules/user';
import app from './modules/app'
import boss from './modules/boss'

Vue.use(Vuex);

const store = new Vuex.Store({
  modules: {
    userInfo,
    user,
    boss,
    app,
  },
  state: {
    menuIsOpen: false,
  },

  getters: {
    getMenuIsOpen: (state) => state.menuIsOpen,
    token: (state) => state.user.token,
    user: (state) => state.user.payload
  },

  mutations: {
    toggleMenu(state, isToggle) {
      if (typeof isToggle !== 'undefined') {
        state.menuIsOpen = isToggle;
      } else {
        state.menuIsOpen = !state.menuIsOpen;
      }
    },
  },
});

export default store