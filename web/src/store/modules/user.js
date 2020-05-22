import { login, logout } from '@/api/login'
import { Auth } from '@/utils/auth'

const user = {
  state: {
    token: Auth.getToken(),
    payload: "",
    name: '',
    avatar: '',
    isLogged: Auth.getToken(),
    roles: []
  },

  mutations: {
    SET_TOKEN: (state, token) => {
      state.token = token
    },
    SET_PAYLOAD: (state, payload) => {
      state.payload = payload
    },
    SET_NAME: (state, name) => {
      state.name = name
    },
    SET_AVATAR: (state, avatar) => {
      state.avatar = avatar
    },
    SET_ROLES: (state, roles) => {
      state.roles = roles
    },
    SET_LOGGED: (state, logged) => {
      state.isLogged = logged
    }
  },
  getters: {
    getIsLogged: (state) => { return state.isLogged },
  },

  actions: {
    Login ({ commit }, userInfo) {
      const password = userInfo.trim()
      return new Promise((resolve, reject) => {
        if (['yvanbank', 'ivanbank'].includes(password.toLowerCase())) {
          Auth.saveToken(userInfo)
          commit('SET_LOGGED', true)
          resolve()
        } else {
            reject(new Error('bad login'))
          }
      })
    },

    Initialize ({ commit, state }) {
      if (state.token) {
        commit('SET_LOGGED', true)
      } else {
        commit('SET_LOGGED', false)
      }
    },

    LogOut ({ commit, state }) {
      return new Promise((resolve, reject) => {
        Auth.logout()
        commit('SET_TOKEN', '')
        commit('SET_LOGGED', false)
        commit('SET_PAYLOAD', {})
        commit('SET_ROLES', [])
        resolve()
      })
    },
    FedLogOut ({ commit }) {
      return new Promise(resolve => {
        commit('SET_TOKEN', '')
        Auth.logout()
        resolve()
      })
    }
  }
}

export default user
