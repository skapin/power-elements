webpackJsonp([1],{

/***/ 140:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__components_side_menu_SideMenu__ = __webpack_require__(229);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__components_side_menu_SideMenu___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0__components_side_menu_SideMenu__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__store__ = __webpack_require__(32);
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//




/* harmony default export */ __webpack_exports__["default"] = ({
  name: 'app',
  store: __WEBPACK_IMPORTED_MODULE_1__store__["a" /* default */],
  data() {},
  computed: {
    menuIsOpen() {
      return __WEBPACK_IMPORTED_MODULE_1__store__["a" /* default */].state.menuIsOpen;
    }
  },
  components: {
    SideMenu: __WEBPACK_IMPORTED_MODULE_0__components_side_menu_SideMenu___default.a
  },
  methods: {
    onUserInteraction(event) {
      console.log(event); // on click ons-splitter-side-mask, event always false(?)
      __WEBPACK_IMPORTED_MODULE_1__store__["a" /* default */].commit('toggleMenu', event);
    },
    toggleMenu() {
      this.$store.commit('toggleMenu', true);
    },
    getIfLoggedIn() {
      return !_.isEmpty(window.localStorage.getItem('jwtToken'));
    }
  },
  mounted: function () {
    if (this.getIfLoggedIn()) {
      this.goTo('home');
    } else {
      this.goTo('loginPage');
    }
  }
});

/***/ }),

/***/ 141:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__http_js__ = __webpack_require__(151);




function getAllQuestions() {
  return __WEBPACK_IMPORTED_MODULE_0__http_js__["a" /* http */].get('/api/questions');
}

function createAccount(password) {
  return __WEBPACK_IMPORTED_MODULE_0__http_js__["a" /* http */].post('/api/users/signup', { 'password': password });
}

function login(username, password) {
  return __WEBPACK_IMPORTED_MODULE_0__http_js__["a" /* http */].post('/api/users/login', { 'username': username, 'password': password });
}

function sendResponsesApi(jwt, responses) {
  return __WEBPACK_IMPORTED_MODULE_0__http_js__["a" /* http */].post('/api/responses', { 'jwt': jwt, 'responses': JSON.stringify(responses) });
}

/* harmony default export */ __webpack_exports__["default"] = ({
  getAllQuestions,
  createAccount,
  login,
  sendResponsesApi
});

/***/ }),

/***/ 142:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//


/* harmony default export */ __webpack_exports__["default"] = ({
  props: {
    id: {
      default: ''
    },
    question: {
      default: 'covid AIO'
    },
    questionId: {
      default: ''
    }
  },
  data() {
    return {
      volume: ''
    };
  },
  methods: {
    clickAnswer() {
      this.$emit('clicked', { 'id': this.questionId, 'answer': this.volume, 'question': this.question });
    }
  }
  // eslint-disable-next-line
});

/***/ }),

/***/ 143:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//

/* harmony default export */ __webpack_exports__["default"] = ({
  name: 'CardPrivateInfos'
});

/***/ }),

/***/ 144:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//

/* harmony default export */ __webpack_exports__["default"] = ({
  name: 'loading-indicator',
  props: {
    isLoading: Boolean
  }
});

/***/ }),

/***/ 145:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//

/* harmony default export */ __webpack_exports__["default"] = ({
  name: 'navbar',
  props: {
    msg: {
      default: 'Covid-19 AIO'
    },
    navType: {
      default: 'back'
    },
    returnPath: {
      default: 'home'
    },
    enabled: {
      default: 'true'
    }
  },
  methods: {
    toggleMenu() {
      this.$store.commit('toggleMenu', true);
    }
  }
});

/***/ }),

/***/ 146:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_vuex__ = __webpack_require__(58);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__store__ = __webpack_require__(32);
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//




/* harmony default export */ __webpack_exports__["default"] = ({
  name: 'side-menu',
  store: __WEBPACK_IMPORTED_MODULE_1__store__["a" /* default */],
  data() {
    return {
      msg: 'OpenWeatherMap',
      essentialLinks: [{
        label: 'Home',
        routeName: 'home',
        icon: 'fa-home'
      }, {
        label: 'About',
        routeName: 'posts',
        icon: 'fa-info'
      }, {
        label: 'Test',
        routeName: 'test',
        icon: 'fa-info'
      }]
    };
  },
  computed: __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0_vuex__["a" /* mapGetters */])({
    info: 'getInfo'
  }),
  methods: {
    goTo(routeName) {
      this.$router.push({ name: routeName });
      __WEBPACK_IMPORTED_MODULE_1__store__["a" /* default */].commit('toggleMenu', false);
    }
  }
});

/***/ }),

/***/ 147:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__components_navbar_Navbar__ = __webpack_require__(31);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__components_navbar_Navbar___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0__components_navbar_Navbar__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__components_Qcm_question__ = __webpack_require__(226);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__components_Qcm_question___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1__components_Qcm_question__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__api_server_vue__ = __webpack_require__(57);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__api_server_vue___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_2__api_server_vue__);
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//





/* harmony default export */ __webpack_exports__["default"] = ({
  name: 'posts-page',
  components: {
    Navbar: __WEBPACK_IMPORTED_MODULE_0__components_navbar_Navbar___default.a,
    Question: __WEBPACK_IMPORTED_MODULE_1__components_Qcm_question___default.a
  },
  data() {
    return {
      qcmAnswers: {},
      questionsList: []
    };
  },
  methods: {
    onClickChild(value) {
      if (this.qcmAnswers[value.id] === undefined) {
        this.qcmAnswers[value.id] = [];
        this.qcmAnswers[value.id] = value.answer;
      } else {
        this.qcmAnswers[value.id] = { 'value': value.answer, 'question': value.question };
      }
      console.log(this.qcmAnswers);
    },
    getAppQuestions() {
      __WEBPACK_IMPORTED_MODULE_2__api_server_vue___default.a.getAllQuestions().then(result => {
        this.questionsList = result.data;
        this.initResponses();
      });
    },
    initResponses() {
      this.questionsList.forEach(question => {
        this.qcmAnswers[question.uniqid] = { 'value': '50', 'question': question.name };
      });
    },
    sendResponses() {
      var jwt = window.localStorage.getItem('jwtToken');
      __WEBPACK_IMPORTED_MODULE_2__api_server_vue___default.a.sendResponsesApi(jwt, this.qcmAnswers).then(() => {
        this.makeToast('Réponses envoyées ! Merci !');
      });
    },
    makeToast(text, append = false) {
      // eslint-disable-next-line
      let toast = this.$toasted.info(text, {
        theme: 'bubble',
        position: 'bottom-right',
        duration: 5000
      });
    }
  },
  mounted: function () {
    console.log("va chercher les Q");
    this.getAppQuestions();
  }
});

/***/ }),

/***/ 148:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__components_navbar_Navbar__ = __webpack_require__(31);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__components_navbar_Navbar___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0__components_navbar_Navbar__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__api_server_vue__ = __webpack_require__(57);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__api_server_vue___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1__api_server_vue__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__components_informations_CardPrivateInfos__ = __webpack_require__(227);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__components_informations_CardPrivateInfos___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_2__components_informations_CardPrivateInfos__);
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//





/* harmony default export */ __webpack_exports__["default"] = ({
  props: ['toggleMenu', 'pageStack'],
  name: 'create-user',
  data: function () {
    return {
      password: ''
    };
  },
  methods: {
    validatePassword() {
      __WEBPACK_IMPORTED_MODULE_1__api_server_vue___default.a.createAccount(this.password).then(result => {
        this.makeToast('Votre identifiant est: ' + result.data.Username);
        this.$router.push({ name: 'loginPage', query: { user: result.data.Username } });
      }).catch(() => {
        this.makeToast('Erreur lors de la création de l\'utilisateur');
      });
    },
    makeToast(text, append = false) {
      // eslint-disable-next-line
      let toast = this.$toasted.info(text, {
        theme: 'bubble',
        position: 'bottom-right',
        duration: 15000
      });
    }
  },
  components: { Navbar: __WEBPACK_IMPORTED_MODULE_0__components_navbar_Navbar___default.a, CardPrivateInfos: __WEBPACK_IMPORTED_MODULE_2__components_informations_CardPrivateInfos___default.a
    // eslint-disable-next-line
  } });

/***/ }),

/***/ 149:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__components_navbar_Navbar__ = __webpack_require__(31);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__components_navbar_Navbar___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0__components_navbar_Navbar__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__api_server_vue__ = __webpack_require__(57);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__api_server_vue___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1__api_server_vue__);
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//




/* harmony default export */ __webpack_exports__["default"] = ({
  props: ['toggleMenu', 'pageStack'],
  name: 'login-page',
  data: function () {
    return {
      password: '',
      user: this.$route.query.user
    };
  },
  methods: {
    validatePassword() {
      __WEBPACK_IMPORTED_MODULE_1__api_server_vue___default.a.login(this.user, this.password).then(result => {
        if (result.data) {
          this.saveLoggedin(result.data);
          this.goTo('home');
        } else {
          this.makeToast('Le mot de passe saisi est incorrect');
        }
      }).catch(() => {
        this.makeToast('Le mot de passe saisi est incorrect');
      });
    },
    makeToast(text, append = false) {
      // eslint-disable-next-line
      let toast = this.$toasted.info(text, {
        theme: 'bubble',
        position: 'bottom-right',
        duration: 5000
      });
    },
    getIfLoggedIn() {
      this.clientRegistered = window.localStorage.getItem('jwtToken') !== '';
    },
    saveLoggedin(data) {
      window.localStorage.setItem('jwtToken', data.token);
    }
  },
  mounted: function () {
    console.log('MAIS LE LOGIN ?');
    this.getIfLoggedIn();
  },
  components: { Navbar: __WEBPACK_IMPORTED_MODULE_0__components_navbar_Navbar___default.a
    // eslint-disable-next-line
  } });

/***/ }),

/***/ 150:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_vuex__ = __webpack_require__(58);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__components_loading_indicator_LoadingIndicator__ = __webpack_require__(228);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__components_loading_indicator_LoadingIndicator___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1__components_loading_indicator_LoadingIndicator__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__components_navbar_Navbar__ = __webpack_require__(31);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__components_navbar_Navbar___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_2__components_navbar_Navbar__);
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//





/* harmony default export */ __webpack_exports__["default"] = ({
  name: 'user-page',
  components: {
    LoadingIndicator: __WEBPACK_IMPORTED_MODULE_1__components_loading_indicator_LoadingIndicator___default.a,
    Navbar: __WEBPACK_IMPORTED_MODULE_2__components_navbar_Navbar___default.a
  },
  computed: __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0_vuex__["a" /* mapGetters */])({
    info: 'getInfo'
  })
});

/***/ }),

/***/ 151:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_axios__ = __webpack_require__(59);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_axios___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_axios__);


const http = __WEBPACK_IMPORTED_MODULE_0_axios___default.a.create({
  // baseURL: `http://127.0.0.1:9019/`,
  baseURL: `https://strawpoll-be.aiotools.ovh/`,
  timeout: 10000,
  headers: {
    // Authorization: 'Bearer {token}'
  }
});
/* harmony export (immutable) */ __webpack_exports__["a"] = http;


/***/ }),

/***/ 152:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_element_ui__ = __webpack_require__(91);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_element_ui___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_element_ui__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_element_ui_lib_theme_chalk_index_css__ = __webpack_require__(93);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_element_ui_lib_theme_chalk_index_css___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_element_ui_lib_theme_chalk_index_css__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_element_ui_lib_locale_lang_ja__ = __webpack_require__(92);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_element_ui_lib_locale_lang_ja___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_2_element_ui_lib_locale_lang_ja__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_vue__ = __webpack_require__(1);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4_vue_onsenui__ = __webpack_require__(99);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4_vue_onsenui___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_4_vue_onsenui__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5_vue_router__ = __webpack_require__(100);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6_axios__ = __webpack_require__(59);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6_axios___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_6_axios__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7_vue_axios__ = __webpack_require__(97);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7_vue_axios___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_7_vue_axios__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8_onsenui_css_onsenui_css__ = __webpack_require__(95);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8_onsenui_css_onsenui_css___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_8_onsenui_css_onsenui_css__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9__App__ = __webpack_require__(98);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9__App___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_9__App__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_10__routes__ = __webpack_require__(90);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_11__store__ = __webpack_require__(32);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_12_vue_toasted__ = __webpack_require__(101);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_12_vue_toasted___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_12_vue_toasted__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_13_onsenui_css_onsen_css_components_css__ = __webpack_require__(94);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_13_onsenui_css_onsen_css_components_css___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_13_onsenui_css_onsen_css_components_css__);
















// import '../static/css/onsen-css-components-pink.min.css';

__WEBPACK_IMPORTED_MODULE_3_vue__["default"].config.productionTip = false;

__webpack_require__(96);
__WEBPACK_IMPORTED_MODULE_3_vue__["default"].use(__WEBPACK_IMPORTED_MODULE_0_element_ui___default.a, { locale: __WEBPACK_IMPORTED_MODULE_2_element_ui_lib_locale_lang_ja___default.a });
__WEBPACK_IMPORTED_MODULE_3_vue__["default"].use(__WEBPACK_IMPORTED_MODULE_4_vue_onsenui___default.a);
__WEBPACK_IMPORTED_MODULE_3_vue__["default"].use(__WEBPACK_IMPORTED_MODULE_5_vue_router__["a" /* default */]);
__WEBPACK_IMPORTED_MODULE_3_vue__["default"].use(__WEBPACK_IMPORTED_MODULE_7_vue_axios___default.a, __WEBPACK_IMPORTED_MODULE_6_axios___default.a);
__WEBPACK_IMPORTED_MODULE_3_vue__["default"].use(__WEBPACK_IMPORTED_MODULE_12_vue_toasted___default.a);

const router = new __WEBPACK_IMPORTED_MODULE_5_vue_router__["a" /* default */]({
  mode: 'hash',
  base: window.location.href,
  routes: __WEBPACK_IMPORTED_MODULE_10__routes__["a" /* default */] // short for `routes: routes`
});

__WEBPACK_IMPORTED_MODULE_3_vue__["default"].mixin({
  data() {
    return {
      alphabet: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    };
  },
  methods: {
    goTo(routeName) {
      this.$router.push({ name: routeName });
      __WEBPACK_IMPORTED_MODULE_11__store__["a" /* default */].commit('toggleMenu', false);
    }
  }
});

new __WEBPACK_IMPORTED_MODULE_3_vue__["default"]({
  components: {
    App: __WEBPACK_IMPORTED_MODULE_9__App___default.a
  },
  template: '<App/>',
  router
}).$mount('#app');

/* eslint-disable no-new */
// new Vue({
//   el: '#app',
//   template: '<App/>',
//   router,
//   components: { App },
// });

/***/ }),

/***/ 153:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony default export */ __webpack_exports__["a"] = ({
  state: {
    courses: []
  },
  mutations: {
    initCourse(state) {
      state.courses = [];
    },
    addCourse(state, params) {
      if (params.edit) {
        state.courses[params.index] = params.data;
      } else {
        state.courses.push(params.data);
      }
    },
    removeCourse(state, num) {
      state.courses.splice(num, 1);
    }
  },
  getters: {},
  actions: {}
});

/***/ }),

/***/ 154:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
const state = {
  info: {
    name: 'ehama',
    ID: 'hoshinari'
  }
};

const getters = {
  getInfo: () => state.info
};

const actions = {};

const mutations = {};

/* harmony default export */ __webpack_exports__["a"] = ({
  state,
  getters,
  actions,
  mutations
});

/***/ }),

/***/ 207:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 208:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 209:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 210:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 211:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 212:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 213:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 214:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 215:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 216:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 226:
/***/ (function(module, exports, __webpack_require__) {

function injectStyle (ssrContext) {
  __webpack_require__(209)
}
var Component = __webpack_require__(4)(
  /* script */
  __webpack_require__(142),
  /* template */
  __webpack_require__(236),
  /* styles */
  injectStyle,
  /* scopeId */
  "data-v-3192a940",
  /* moduleIdentifier (server only) */
  null
)

module.exports = Component.exports


/***/ }),

/***/ 227:
/***/ (function(module, exports, __webpack_require__) {

function injectStyle (ssrContext) {
  __webpack_require__(211)
}
var Component = __webpack_require__(4)(
  /* script */
  __webpack_require__(143),
  /* template */
  __webpack_require__(238),
  /* styles */
  injectStyle,
  /* scopeId */
  "data-v-570a6ff8",
  /* moduleIdentifier (server only) */
  null
)

module.exports = Component.exports


/***/ }),

/***/ 228:
/***/ (function(module, exports, __webpack_require__) {

function injectStyle (ssrContext) {
  __webpack_require__(208)
}
var Component = __webpack_require__(4)(
  /* script */
  __webpack_require__(144),
  /* template */
  __webpack_require__(235),
  /* styles */
  injectStyle,
  /* scopeId */
  "data-v-3012564a",
  /* moduleIdentifier (server only) */
  null
)

module.exports = Component.exports


/***/ }),

/***/ 229:
/***/ (function(module, exports, __webpack_require__) {

function injectStyle (ssrContext) {
  __webpack_require__(216)
}
var Component = __webpack_require__(4)(
  /* script */
  __webpack_require__(146),
  /* template */
  __webpack_require__(243),
  /* styles */
  injectStyle,
  /* scopeId */
  "data-v-ab6ffe14",
  /* moduleIdentifier (server only) */
  null
)

module.exports = Component.exports


/***/ }),

/***/ 230:
/***/ (function(module, exports, __webpack_require__) {

function injectStyle (ssrContext) {
  __webpack_require__(215)
}
var Component = __webpack_require__(4)(
  /* script */
  __webpack_require__(147),
  /* template */
  __webpack_require__(242),
  /* styles */
  injectStyle,
  /* scopeId */
  "data-v-7d57eac0",
  /* moduleIdentifier (server only) */
  null
)

module.exports = Component.exports


/***/ }),

/***/ 231:
/***/ (function(module, exports, __webpack_require__) {

function injectStyle (ssrContext) {
  __webpack_require__(207)
}
var Component = __webpack_require__(4)(
  /* script */
  __webpack_require__(148),
  /* template */
  __webpack_require__(234),
  /* styles */
  injectStyle,
  /* scopeId */
  null,
  /* moduleIdentifier (server only) */
  null
)

module.exports = Component.exports


/***/ }),

/***/ 232:
/***/ (function(module, exports, __webpack_require__) {

function injectStyle (ssrContext) {
  __webpack_require__(214)
}
var Component = __webpack_require__(4)(
  /* script */
  __webpack_require__(149),
  /* template */
  __webpack_require__(241),
  /* styles */
  injectStyle,
  /* scopeId */
  null,
  /* moduleIdentifier (server only) */
  null
)

module.exports = Component.exports


/***/ }),

/***/ 233:
/***/ (function(module, exports, __webpack_require__) {

function injectStyle (ssrContext) {
  __webpack_require__(212)
}
var Component = __webpack_require__(4)(
  /* script */
  __webpack_require__(150),
  /* template */
  __webpack_require__(239),
  /* styles */
  injectStyle,
  /* scopeId */
  "data-v-70105326",
  /* moduleIdentifier (server only) */
  null
)

module.exports = Component.exports


/***/ }),

/***/ 234:
/***/ (function(module, exports, __webpack_require__) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('v-ons-page', [_c('navbar', {
    attrs: {
      "returnPath": "loginPage"
    }
  }), _vm._v(" "), _c('div', {
    staticClass: "login-page"
  }, [_c('div', {
    staticClass: "center-screen"
  }, [_c('v-ons-row', [_c('img', {
    staticClass: "login-logo",
    attrs: {
      "src": __webpack_require__(88)
    }
  })]), _vm._v(" "), _c('v-ons-row', [_c('p', {
    staticClass: "login-header"
  }, [_vm._v("Création de compte")])]), _vm._v(" "), _c('v-ons-row', {
    staticClass: "login-form"
  }, [_c('v-ons-input', {
    attrs: {
      "placeholder": "Choisis un mot de passe",
      "float": "",
      "type": "password"
    },
    model: {
      value: (_vm.password),
      callback: function($$v) {
        _vm.password = $$v
      },
      expression: "password"
    }
  })], 1), _vm._v(" "), _c('v-ons-row', [_c('v-ons-col', [_c('v-ons-button', {
    attrs: {
      "modifier": "large"
    },
    on: {
      "click": function($event) {
        return _vm.validatePassword()
      }
    }
  }, [_vm._v("Créer le compte")])], 1)], 1)], 1), _vm._v(" "), _c('div', [_c('v-ons-row', [_c('v-ons-col', [_c('CardPrivateInfos')], 1)], 1)], 1)])], 1)
},staticRenderFns: []}

/***/ }),

/***/ 235:
/***/ (function(module, exports) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return (_vm.isLoading) ? _c('div', {
    staticClass: "loading-wrapper"
  }, [_c('svg', {
    staticClass: "progress-circular progress-circular--indeterminate"
  }, [_c('circle', {
    staticClass: "progress-circular__background"
  }), _vm._v(" "), _c('circle', {
    staticClass: "progress-circular__primary progress-circular--indeterminate__primary"
  }), _vm._v(" "), _c('circle', {
    staticClass: "progress-circular__secondary progress-circular--indeterminate__secondary"
  })])]) : _c('div')
},staticRenderFns: []}

/***/ }),

/***/ 236:
/***/ (function(module, exports) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('v-ons-card', {
    staticClass: "card"
  }, [_c('div', {
    staticClass: "title"
  }, [_c('h1', [_vm._v(_vm._s(_vm.question))])]), _vm._v(" "), _c('div', {
    staticClass: "content"
  }, [_c('v-ons-row', [_c('v-ons-col', {
    attrs: {
      "width": "10%",
      "vertical-align": "center"
    }
  }, [_c('span', [_vm._v(" Non ")])]), _vm._v(" "), _c('v-ons-col', {
    attrs: {
      "width": "80%",
      "vertical-align": "center"
    }
  }, [_c('v-ons-range', {
    staticStyle: {
      "width": "90%"
    },
    on: {
      "click": function($event) {
        return _vm.clickAnswer(_vm.question)
      }
    },
    model: {
      value: (_vm.volume),
      callback: function($$v) {
        _vm.volume = $$v
      },
      expression: "volume"
    }
  })], 1), _vm._v(" "), _c('v-ons-col', {
    attrs: {
      "width": "10%",
      "vertical-align": "center"
    }
  }, [_c('span', [_vm._v(" Oui ")])])], 1)], 1)])
},staticRenderFns: []}

/***/ }),

/***/ 237:
/***/ (function(module, exports) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('v-ons-toolbar', {
    staticClass: "home-toolbar"
  }, [(_vm.navType == 'menu') ? _c('div', {
    staticClass: "left"
  }, [_c('v-ons-toolbar-button', {
    on: {
      "click": function($event) {
        return _vm.toggleMenu()
      }
    }
  }, [_c('v-ons-icon', {
    attrs: {
      "icon": "ion-navicon, material:md-menu"
    }
  })], 1)], 1) : (_vm.navType == 'back') ? _c('div', {
    staticClass: "left"
  }, [(_vm.enabled == 'true') ? _c('v-ons-button', {
    staticStyle: {
      "margin": "3px 0"
    },
    attrs: {
      "modifier": "quiet"
    },
    on: {
      "click": function($event) {
        return _vm.goTo(_vm.returnPath)
      }
    }
  }, [_c('v-ons-icon', {
    attrs: {
      "size": "50px",
      "icon": "md-caret-left"
    }
  })], 1) : _vm._e()], 1) : _vm._e(), _vm._v(" "), _c('div', {
    staticClass: "center",
    staticStyle: {
      "font-size": "15px",
      "font-weight": "800"
    }
  }, [_vm._v(_vm._s(_vm.msg))])])
},staticRenderFns: []}

/***/ }),

/***/ 238:
/***/ (function(module, exports) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('v-ons-card', {
    staticClass: "bluecard"
  }, [_c('div', {
    staticClass: "title"
  }, [_vm._v("\n      Informations importantes\n    ")]), _vm._v(" "), _c('div', {
    staticClass: "content"
  }, [_c('p', [_vm._v("Le questionnaire est anonyme, nous ne collectons aucune donnée personelle.")]), _vm._v(" "), _c('p', [_vm._v("Le but de cette application est d'évaluer la possible présence du COVID-19 au sein de l'entreprise en regroupant les réponses anonymes des collaborateurs.")])])])
},staticRenderFns: []}

/***/ }),

/***/ 239:
/***/ (function(module, exports, __webpack_require__) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('v-ons-page', [_c('navbar'), _vm._v(" "), _c('v-ons-card', [_c('div', {
    attrs: {
      "align": "center"
    }
  }, [_c('h3', [_vm._v("My Page")]), _vm._v(" "), _c('img', {
    attrs: {
      "src": __webpack_require__(89)
    }
  }), _vm._v(" "), _c('b', [_c('p', [_vm._v(_vm._s(_vm.info.name))])]), _vm._v(" "), _c('p', [_vm._v("user ID: " + _vm._s(_vm.info.ID))])])])], 1)
},staticRenderFns: []}

/***/ }),

/***/ 240:
/***/ (function(module, exports) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('v-ons-page', {
    attrs: {
      "id": "app"
    }
  }, [_c('router-view'), _vm._v(" "), _c('v-ons-splitter', [_c('v-ons-splitter-side', {
    attrs: {
      "swipeable": "",
      "collapse": "",
      "width": "250px",
      "open": _vm.menuIsOpen
    },
    on: {
      "update:open": [function($event) {
        _vm.menuIsOpen = $event
      }, _vm.onUserInteraction]
    }
  }, [_c('side-menu')], 1), _vm._v(" "), _c('v-ons-splitter-content', [_c('transition', {
    attrs: {
      "name": "slide-fade"
    }
  }, [_c('router-view')], 1)], 1)], 1)], 1)
},staticRenderFns: []}

/***/ }),

/***/ 241:
/***/ (function(module, exports, __webpack_require__) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('v-ons-page', [_c('navbar', {
    attrs: {
      "enabled": "false"
    }
  }), _vm._v(" "), _c('div', {
    staticClass: "login-page"
  }, [_c('div', {
    staticClass: "center-screen"
  }, [_c('v-ons-row', [_c('img', {
    staticClass: "login-logo",
    attrs: {
      "src": __webpack_require__(88)
    }
  })]), _vm._v(" "), _c('v-ons-row', [_c('p', {
    staticClass: "login-header"
  }, [_vm._v("Connexion")])]), _vm._v(" "), _c('v-ons-row', {
    staticClass: "login-form"
  }, [_c('v-ons-input', {
    attrs: {
      "placeholder": "nom d'utilisateur",
      "float": "",
      "type": "text"
    },
    model: {
      value: (_vm.user),
      callback: function($$v) {
        _vm.user = $$v
      },
      expression: "user"
    }
  })], 1), _vm._v(" "), _c('v-ons-row', {
    staticClass: "login-form"
  }, [_c('v-ons-input', {
    attrs: {
      "placeholder": "mot de passe",
      "float": "",
      "type": "password"
    },
    model: {
      value: (_vm.password),
      callback: function($$v) {
        _vm.password = $$v
      },
      expression: "password"
    }
  })], 1), _vm._v(" "), _c('v-ons-row', [_c('v-ons-col', {
    staticClass: "button-page"
  }, [_c('v-ons-button', {
    attrs: {
      "modifier": "large"
    },
    on: {
      "click": function($event) {
        return _vm.goTo('accountCreationPage')
      }
    }
  }, [_vm._v("Pas de compte ?")])], 1), _vm._v(" "), _c('v-ons-col', [_c('v-ons-button', {
    attrs: {
      "modifier": "large"
    },
    on: {
      "click": function($event) {
        return _vm.validatePassword()
      }
    }
  }, [_vm._v("Se connecter")])], 1)], 1)], 1)])], 1)
},staticRenderFns: []}

/***/ }),

/***/ 242:
/***/ (function(module, exports) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('v-ons-page', [_c('navbar', {
    attrs: {
      "enabled": "false"
    }
  }), _vm._v(" "), (_vm.questionsList) ? _c('div', {
    staticClass: "home-page"
  }, [_vm._l((_vm.questionsList), function(row, indexRow) {
    return _c('div', {
      key: indexRow
    }, [_c('question', {
      attrs: {
        "questionId": row.uniqid,
        "question": row.name
      },
      on: {
        "clicked": _vm.onClickChild
      }
    })], 1)
  }), _vm._v(" "), _c('div', {
    staticClass: "validation-button"
  }, [_c('v-ons-button', {
    attrs: {
      "modifier": "large"
    },
    on: {
      "click": function($event) {
        return _vm.sendResponses()
      }
    }
  }, [_vm._v("Valider")])], 1)], 2) : _vm._e()], 1)
},staticRenderFns: []}

/***/ }),

/***/ 243:
/***/ (function(module, exports, __webpack_require__) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('v-ons-page', [_c('v-ons-toolbar', {
    attrs: {
      "modifier": "transparent"
    }
  }), _vm._v(" "), _c('div', {
    staticClass: "header"
  }, [_c('img', {
    attrs: {
      "src": __webpack_require__(89)
    }
  })]), _vm._v(" "), _c('div', {
    attrs: {
      "align": "center"
    }
  }, [_c('router-link', {
    attrs: {
      "to": "user-page"
    }
  }, [_vm._v(_vm._s(_vm.info.name))]), _vm._v(" "), _c('p', [_vm._v("user ID: " + _vm._s(_vm.info.ID))])], 1), _vm._v(" "), _c('v-ons-list-title', [_vm._v("Onsen UI Essential Links")]), _vm._v(" "), _c('v-ons-list', _vm._l((_vm.essentialLinks), function(item) {
    return _c('v-ons-list-item', {
      key: item.routeName,
      attrs: {
        "modifier": "chevron"
      },
      on: {
        "click": function($event) {
          return _vm.goTo(item.routeName)
        }
      }
    }, [_c('div', {
      staticClass: "left"
    }, [_c('v-ons-icon', {
      attrs: {
        "fixed-width": "",
        "icon": item.icon
      }
    })], 1), _vm._v(" "), _c('div', {
      staticClass: "center"
    }, [_vm._v(_vm._s(item.label))])])
  }), 1)], 1)
},staticRenderFns: []}

/***/ }),

/***/ 31:
/***/ (function(module, exports, __webpack_require__) {

function injectStyle (ssrContext) {
  __webpack_require__(210)
}
var Component = __webpack_require__(4)(
  /* script */
  __webpack_require__(145),
  /* template */
  __webpack_require__(237),
  /* styles */
  injectStyle,
  /* scopeId */
  "data-v-55bafb39",
  /* moduleIdentifier (server only) */
  null
)

module.exports = Component.exports


/***/ }),

/***/ 32:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_vue__ = __webpack_require__(1);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_vuex__ = __webpack_require__(58);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__modules_userInfo__ = __webpack_require__(154);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__modules_createPlan__ = __webpack_require__(153);





__WEBPACK_IMPORTED_MODULE_0_vue__["default"].use(__WEBPACK_IMPORTED_MODULE_1_vuex__["b" /* default */]);

/* harmony default export */ __webpack_exports__["a"] = (new __WEBPACK_IMPORTED_MODULE_1_vuex__["b" /* default */].Store({
  modules: {
    userInfo: __WEBPACK_IMPORTED_MODULE_2__modules_userInfo__["a" /* default */],
    createPlan: __WEBPACK_IMPORTED_MODULE_3__modules_createPlan__["a" /* default */]
  },
  state: {
    menuIsOpen: false,
    currentArea: { id: 1, name: '北海道' },
    username: ''
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
    }
  }
}));

/***/ }),

/***/ 57:
/***/ (function(module, exports, __webpack_require__) {

var Component = __webpack_require__(4)(
  /* script */
  __webpack_require__(141),
  /* template */
  null,
  /* styles */
  null,
  /* scopeId */
  null,
  /* moduleIdentifier (server only) */
  null
)

module.exports = Component.exports


/***/ }),

/***/ 88:
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__.p + "static/img/AIO-logo.d6dea93.png";

/***/ }),

/***/ 89:
/***/ (function(module, exports) {

module.exports = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxEHBhEQBxIQExIWEBUQEA8VDg8QEBIWFBEWFxUVFhUYHSggGBsmGxgVITEhJSktLi4uFx8zODMsNygtLisBCgoKDQ0ODg0PDi0ZFRkrKysrKy0rKysrKysrKy0rKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrK//AABEIAOEA4QMBIgACEQEDEQH/xAAaAAEBAQEBAQEAAAAAAAAAAAAABQQBAwIH/8QAMhABAAECAwYDBwMFAAAAAAAAAAECAwQRIRIxQVFhkQUiMhNygaGxwdEzUnEUIzTh8f/EABYBAQEBAAAAAAAAAAAAAAAAAAABAv/EABYRAQEBAAAAAAAAAAAAAAAAAAABEf/aAAwDAQACEQMRAD8A/TgGWwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdpjaqyhrw+Cmqc72kcuMgxvSmzVV6aZ7K1u3FuPJEQ+1TUn+jr/b84fFVmqn1Uz2WQNQhZu2abseePjxTsThZs6745/kVnAQAAAAAAAAAAAAAAAAAAHpas1XfRHx4PbC4T2sZ16Rw5yo0UxRTlTuUeOEw/saPNltcZaAEAAAAHJjONXQE7FYPYjatbuMcv8ATGup+Nwuz5re7jHLqDEAigAAAAAAAAAAAAAD1w9mb9zKN3GeTyVMBTs4eOszKjREbMZQ6AgAAAAAAAA5MZxq6Al4vDexqzp9M/LozLVyiLlExVxR66diqYq4TkK+QEAAAAAAAAAAAABXwcZYanLl90hWwU54aPjHzUr3AEAAAAAAAAAAEvxCnZxGnGIn7fZUTfEv1492PrIRkARQAAAAAAAAAAABR8NqztTHKc+//E5q8Oqyv5c4+iimAIAAAAAAAAAAJviU/wB6Pd+8qSVjq9rEz00CM4CKAAAAAAAAAAAAKfh9OWHz6zqmK2C/xacuv1lSvcAQAAAAAAAAAAR8VGWJq/nPusI2InO/Vn+6QjzARQAAAAAAAAAAABR8NqztTHKc+6c04C5sX8p3Tp8eCioAIAAAAAAAAAA5M5Rqi3KtuuZ5zMqmNr2MPPXTukhABFAAAAAAAAAAAAAAVMJiIu24iqfNG/r1aUJYw054en3YVHqAAAAAAAAOTOUZywXcftW8qIynjOf0B5Y297W5lG6NI69WcEUAAAAAAAAAAAAAAAAU/D69qxlyn6pjRg73sr2u6dJ+yiqAIAAAAAA8MZXsYeeundJbPEq87kU8IjPuxiwAQAAAAAAAAAAAAAAAADcPqiiblcRTvkFqJzh1ymMqYjo6qAAAAAAJviNuYu7XCdOzItXLcXaMq9yffwU29besfOBWUBAAAAAAAAAAAAAB2mmapypjMHBqtYGqr16R3ns1W8HRRv1/n8KMFmxVenyR8eClh8PFiNNZ4y9YjKNHRAAAAAAAAAAHhew1N7fpPOGW5gKo9ExPylRARK7c2588TD5XJjONWe7g6K92k9PwLqWNN3BVW/TrHTf2ZkAAAAAHaaZrqyp1kHHrasVXfRHx3Q24fBxRrd1nlwj8taprFawER+rOfSNIa6KIojKiIh9AAAAAAAAAAAAAAAAAAADwxGGi9HKef5e4CLdtzaqyrh8LdyiLlOVcZwl4nDzYq6cJFeACDsRtTlCrhcPFinXfxn7Mnh1vauzM8I+cqSpQAAAAAAAAAAAAAAAAAAAAAAAB81UxXTlVrD6AZP6Cnr3dagGLwz0VfzDaAAAOAAAAAAAAAAAAAAAAAAQ6AAAAAAAP/9k="

/***/ }),

/***/ 90:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__pages_home_HomePage__ = __webpack_require__(230);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__pages_home_HomePage___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0__pages_home_HomePage__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__pages_login_form_LoginPage__ = __webpack_require__(232);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__pages_login_form_LoginPage___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1__pages_login_form_LoginPage__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__pages_login_form_AccountCreationPage__ = __webpack_require__(231);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__pages_login_form_AccountCreationPage___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_2__pages_login_form_AccountCreationPage__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__pages_user_page_UserPage__ = __webpack_require__(233);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__pages_user_page_UserPage___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_3__pages_user_page_UserPage__);





/* harmony default export */ __webpack_exports__["a"] = ([{ name: 'home', path: '/', component: __WEBPACK_IMPORTED_MODULE_0__pages_home_HomePage___default.a }, { name: 'userPage', path: '/user-page', component: __WEBPACK_IMPORTED_MODULE_3__pages_user_page_UserPage___default.a }, { name: 'loginPage', path: '/login-page', component: __WEBPACK_IMPORTED_MODULE_1__pages_login_form_LoginPage___default.a }, { name: 'accountCreationPage', path: '/account-creation-page', component: __WEBPACK_IMPORTED_MODULE_2__pages_login_form_AccountCreationPage___default.a }]);

/***/ }),

/***/ 93:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 94:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 95:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 98:
/***/ (function(module, exports, __webpack_require__) {

function injectStyle (ssrContext) {
  __webpack_require__(213)
}
var Component = __webpack_require__(4)(
  /* script */
  __webpack_require__(140),
  /* template */
  __webpack_require__(240),
  /* styles */
  injectStyle,
  /* scopeId */
  "data-v-7759836e",
  /* moduleIdentifier (server only) */
  null
)

module.exports = Component.exports


/***/ })

},[152]);