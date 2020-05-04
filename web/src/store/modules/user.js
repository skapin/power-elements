import { login, logout } from '@/api/login'
import { Auth } from '@/utils/auth'

const user = {
  state: {
    token: Auth.getToken(),
    payload: Auth.parseJwt(Auth.getToken()),
    name: '',
    avatar: '',
    isLogged: false,
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

  actions: {
    Login ({ commit }, userInfo) {
      const username = userInfo.username.trim()
      return new Promise((resolve, reject) => {
        login(username, userInfo.password).then((response) => {
          const data = response
          Auth.saveToken(data.token)
          commit('SET_TOKEN', data.token)
          let payload = Auth.parseJwt(data.token)
          commit('SET_PAYLOAD', payload)
          console.log(payload)
          commit('SET_NAME', payload.name)
          commit('SET_LOGGED', data.login)
          if (data.login) {
            resolve()
          } else {
            reject(new Error('bad login'))
          }
        }).catch(error => {
          reject(error)
        })
      })
    },

    Initialize ({ commit, state }) {
      if (state.payload && Auth.isTokenFresh(state.payload)) {
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
