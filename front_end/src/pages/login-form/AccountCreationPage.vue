<template>
  <v-ons-page>
    <navbar returnPath="loginPage"></navbar>
    <div class="login-page">
      <div class="center-screen">
        <v-ons-row>
          <img class="login-logo" src="../../assets/onsenui-logo.png" />
        </v-ons-row>
        <v-ons-row>
          <p class="login-header">Création de compte</p>
        </v-ons-row>
        <v-ons-row class="login-form">
          <v-ons-input placeholder="Entrer le code" float type="password" v-model="password"></v-ons-input>
        </v-ons-row>
        <v-ons-row>
          <v-ons-col>
            <v-ons-button modifier="large" @click="validatePassword()">Créer le compte</v-ons-button>
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
  name: 'create-user',
  data: function () {
    return {
      password: '',
    }
  },
  methods: {
    validatePassword () {
      server
        .createAccount(this.password)
        .then((result) => {
          this.makeToast('Votre identifiant est: ' + result.data.Username)
          this.goTo('loginPage')
        })
        .catch(() => {
          this.makeToast('Erreur lors de la création de l\'utilisateur')
        })
    },
    makeToast (text, append = false) {
      // eslint-disable-next-line
      let toast = this.$toasted.info(text, {
        theme: 'bubble',
        position: 'bottom-right',
        duration: 15000
      })
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
  width: 40vh;
  margin-left: 2vw;
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
  margin: 4px;
}
.login-header {
  background-color: #215d9e;
  width: 100%;
  height: 100%;
  padding: 15px;
  color: white;
  font-size: 24px;
  margin: 0px;
}
.center-screen {
  position: fixed;
  top: 50%;
  left: 50%;
  width: 40vh;
  /* bring your own prefixes */
  transform: translate(-50%, -50%);
  min-width: 273px;
}
.login-page {
  height: 100vh;
  overflow: auto;
  background: linear-gradient(#61d7ff, #2667a8);
}

ons-input{
  width: 100%;
}
</style>
