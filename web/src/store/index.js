import Vue from 'vue';
import Vuex from 'vuex';
import userInfo from './modules/userInfo';
import user from './modules/user';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    userInfo,
    user,
  },
  state: {
    menuIsOpen: false,
    currentArea: { id: 1, name: 'top!' },
    username:''
  },

  getters: {
    getMenuIsOpen: (state) => state.menuIsOpen,
    token: (state) => state.user.token
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
