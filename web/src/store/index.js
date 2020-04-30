import Vue from 'vue';
import Vuex from 'vuex';
import userInfo from './modules/userInfo';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    userInfo,
  },
  state: {
    menuIsOpen: false,
    currentArea: { id: 1, name: 'top!' },
    username:''
  },

  getters: {
    getMenuIsOpen: (state) => state.menuIsOpen,
  },

  mutations: {
    toggleMenu(state, isToggle) {
      if (typeof isToggle !== 'undefined') {
        state.menuIsOpen = isToggle;
      } else {
        state.menuIsOpen = !state.menuIsOpen;
      }
    },
    setArea(state, data) {
      state.currentArea = data;
    },
    setUsernameArea(state, data) {
      state.username = data;
    },
  },
});
