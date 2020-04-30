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
            <v-ons-button class="btn" modifier="large" @click="goTo('accountCreationPage')">Pas de compte ?</v-ons-button>
          </v-ons-col>
          <v-ons-col>
            <v-ons-button 
              :disabled="loading" 
              class="btn" 
              modifier="large" 
              @click="handleLogin()"
            >
              Se connecter
            </v-ons-button>
          </v-ons-col>
        </v-ons-row>

      </div>
    </div>
  </v-ons-page>
</template>
<script>
import Navbar from '../../components/navbar/Navbar';
import server from './../../api/server.vue'
import { mapGetters } from 'vuex'

export default {
  props: ['toggleMenu', 'pageStack'],
  name: 'login-page',
  data: function () {
    return {
      user: '',
      password: '',
      loading: false
    }
  },
  methods: {
    makeToast (text, append = false) {
      // eslint-disable-next-line
      let toast = this.$toasted.info(text, {
        theme: 'bubble',
        position: 'bottom-right',
        duration: 5000
      })
    },
    handleLogin () {
      this.$toasted.clear()
      this.loading = true
      let data = { 'username': this.user, 'password': this.password}
      this.$store.dispatch('Login', data).then(() => {
        this.loading = false
        this.makeToast('Connexion avec succès !')
        this.goTo('home')
      }).catch((error) => {
        this.loading = false
        this.password = ''
        this.$toasted.error('Mauvais compte ou mot de passe ')
      })
    }
  },
  computed: {
    getUser () {
      return this.$store.getters.user
    }
  },
  mounted: function () {
    if (this.$route.query.user) {
      this.user = this.$route.query.user
    } else {
      if ( this.getUser ) {
        this.user = this.getUser
      }
    }
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

.btn:hover {
  cursor:pointer !important;
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
