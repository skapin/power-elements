<template>
  <v-ons-page>
    <navbar enabled="false"></navbar>
    <div class="login-page">
      <div class="center-screen">
        <v-ons-row>
          <img class="login-logo" src="../../assets/AIO-logo.png" />
        </v-ons-row>
        <v-ons-row>
          <p class="login-header">Connexion</p>
        </v-ons-row>
        <v-ons-row class="login-form">
          <v-ons-input
            placeholder="nom d'utilisateur"
            float
            type="text"
            v-model="user"
          ></v-ons-input>
        </v-ons-row>
        <v-ons-row class="login-form">
          <v-ons-input placeholder="mot de passe" float type="password" v-model="password"></v-ons-input>
        </v-ons-row>
        <v-ons-row>
          <v-ons-col class="button-page">
            <v-ons-button modifier="large" @click="goTo('accountCreationPage')">Pas de compte ?</v-ons-button>
          </v-ons-col>
          <v-ons-col>
            <v-ons-button modifier="large" @click="validatePassword()">Se connecter</v-ons-button>
          </v-ons-col>
        </v-ons-row>

      </div>
    </div>
  </v-ons-page>
</template>
<script>
import Navbar from '../../components/navbar/Navbar';
import server from './../../api/server.vue'

export default {
  props: ['toggleMenu', 'pageStack'],
  name: 'login-page',
  data: function () {
    return {
      password: '',
      user: this.$route.query.user
    }
  },
  methods: {
    validatePassword () {
      server
        .login(this.user, this.password)
        .then(result => {
          if (result.data) {
            this.saveLoggedin(result.data)
            this.goTo('home')
          } else {
            this.makeToast('Le mot de passe saisi est incorrect')
          }
        })
        .catch(() => {
          this.makeToast('Le mot de passe saisi est incorrect')
        })
    },
    makeToast (text, append = false) {
      // eslint-disable-next-line
      let toast = this.$toasted.info(text, {
        theme: 'bubble',
        position: 'bottom-right',
        duration: 5000
      })
    },
    getIfLoggedIn () {
      this.clientRegistered =
        window.localStorage.getItem('jwtToken') !== ''
    },
    saveLoggedin (data) {
      window.localStorage.setItem('jwtToken', data.token)
      this.$store.commit('setInfo', {'Username': data.username})
    }
  },
  mounted: function () {
    this.getIfLoggedIn()
  },
  components: { Navbar }
  // eslint-disable-next-line
}
</script>

<style>
.home-block {
  margin-top: 25%;
}
.login-logo {
  width: 100%;
  margin-bottom: 20px;
}
.button-page {
  margin-right: 10px;
}
v-ons-button {
  font-size: 24px;
}

.login-form {
  background-color: white;
  padding: 15px;
  margin: 2px 0;
}
.login-header {
  text-align: center;
  background-color: #215d9e;
  width: 100%;
  height: 100%;
  padding: 15px;
  color: white;
  font-size: 24px;
  margin: 0px;
}
.center-screen {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 40vh;
  min-width: 300px;
}
.login-page {
  height: calc(100vh - 44px);
  display:flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
  background: linear-gradient(#61d7ff, #2667a8);
}

ons-input{
  width: 50%;
  min-width: 300px;
}
</style>
