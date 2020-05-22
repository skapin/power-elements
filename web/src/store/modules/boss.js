
const boss = {
  state: {
    bossTimer: 0,
  },

  mutations: {
    increaseTimer (state) {
      if ( state.bossTimer <= 0) {
        return
      }
      state.bossTimer = state.bossTimer - 1
      window.localStorage.setItem('bossTimer', state.bossTimer)
    },
    startBossTimer (state) {
      let storedTimer = window.localStorage['bossTimer']
      if (storedTimer) {
        state.bossTimer = storedTimer
      } else {
        state.bossTimer = 60 * 60
        window.localStorage.setItem('bossTimer', state.bossTimer)
      }
    }
  },
  getters: {
    getBossTimer: (state) => { return state.bossTimer },
  },

  actions: {
  }
}

export default boss
