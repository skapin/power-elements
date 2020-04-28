<template>
  <v-ons-page>
    <navbar returnPath="loginPage"></navbar>
    <div class="login-page">
      <div class="center-screen">
        <v-ons-row>
          <img class="login-logo" src="../../assets/AIO-logo.png" />
        </v-ons-row>
        <v-ons-row>
          <p class="login-header">Création de compte</p>
        </v-ons-row>
        <v-ons-row class="login-form">
          <v-ons-input placeholder="Choisis un mot de passe" float type="password" v-model="password"></v-ons-input>
        </v-ons-row>
        <v-ons-row>
          <v-ons-col>
            <v-ons-button modifier="large" @click="validatePassword()">Créer le compte</v-ons-button>
          </v-ons-col>
        </v-ons-row>
        </div>
        <div>
        <v-ons-row>
          <v-ons-col>
            <CardPrivateInfos />
          </v-ons-col>
        </v-ons-row>
     </div>
    </div>
  </v-ons-page>
</template>
<script>
import Navbar from '../../components/navbar/Navbar';
import server from './../../api/server.vue';
import CardPrivateInfos from '../../components/informations/CardPrivateInfos'

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
  components: { Navbar, CardPrivateInfos }
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
  justify-content: space-around;
  align-items: center;
  background: linear-gradient(#61d7ff, #2667a8);
}

ons-input{
  width: 50%;
  min-width: 300px;
}
</style>
