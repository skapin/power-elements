const state = {
  info: {
    name: 'ehama',
    ID: 'hoshinari',
  },
};

const getters = {
  getInfo: () => state.info,
};

const actions = {

};

const mutations = {
    setInfo (state, params) {
        console.log(params)
        state.info = {'name': params.Username, 'ID': params.Username}
    }

};

export default {
  state,
  getters,
  actions,
  mutations,
};
