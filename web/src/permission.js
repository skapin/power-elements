import router from './router'
import store from './store'
// import { Auth } from '@/utils/auth'
// import lazyLoading from './store/modules/menu/lazyLoading'
import { whiteList } from '@/router/index'

router.beforeEach((to, from, next) => {
  if (store.getters.isLogged) {
    if (to.path === '/auth/login') {
      next({ path: '/' })
    } else {
      /* if (store.getters.roles.length === 0) {
        store.dispatch('GetInfo').then(res => {
          const roles = res.data.role
          store.dispatch('GenerateRoutes', { roles }).then(() => {
            router.addRoutes(store.getters.addRouters)
            next({ ...to })
          })
        })
      } else {
        next()
      }
      */
      next()
    }
  } else {
    if (whiteList.indexOf(to.path) !== -1) {
      next()
    } else {
      // lazyLoading('auth/login/Login')
      next('/auth/login')
    }
  }
})
