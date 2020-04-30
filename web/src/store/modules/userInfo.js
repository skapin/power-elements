const state = {
  info: {
    name: 'foo',
    ID: 'barr',
  },
};

const getters = {
  getInfo: () => state.info,
};

const actions = {

};

const mutations = {
    setInfo (state, params) {
        state.info = {'name': params.Username, 'ID': params.Username}
    }

};

export default {
  state,
  getters,
  actions,
  mutations,
};
