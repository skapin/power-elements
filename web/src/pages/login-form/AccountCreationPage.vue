<template>
  <v-ons-page>
    <navbar returnPath="loginPage"></navbar>
    <div class="background"></div>
    <div class="content">
      <div class="account-page">
        <div class="center-screen">
          <!-- <v-ons-row>
            <img class="login-logo" src="../../assets/AIO-logo.png" />
          </v-ons-row> -->
          <v-ons-row>
            <p class="login-header">Création de compte</p>
          </v-ons-row>
          <v-ons-row>
            <p
              class="login-info"
            >Votre pseudonyme sera généré aléatoirement pour garantir votre anonymat. Veuillez simplement entrer un mot de passe !</p>
          </v-ons-row>
          <v-ons-row class="login-form">
            <v-ons-input
              placeholder="Choisis un mot de passe"
              float
              type="password"
              v-model="password"
            ></v-ons-input>
          </v-ons-row>
          <v-ons-row>
            <v-ons-col>
              <v-ons-button
                class="btn"
                modifier="large"
                @click="validatePassword()"
                :disabled="loading || !password"
              >Créer le compte</v-ons-button>
            </v-ons-col>
          </v-ons-row>
          <v-ons-row>
            <CardPrivateInfos />
          </v-ons-row>
        </div>
      </div>
    </div>
  </v-ons-page>
</template>
<script>
import Navbar from "../../components/navbar/Navbar";
import server from "./../../api/server.vue";
import CardPrivateInfos from "../../components/informations/CardPrivateInfos";

export default {
  props: ["toggleMenu", "pageStack"],
  name: "create-user",
  data: function() {
    return {
      password: "",
      loading: false
    };
  },
  methods: {
    validatePassword() {
      this.$toasted.clear();
      this.loading = true;
      server
        .createAccount(this.password)
        .then(result => {
          this.loading = false;
          this.makeToast("Votre identifiant est: " + result.Username);
          this.$router.push({
            name: "loginPage",
            query: { user: result.Username }
          });
        })
        .catch(err => {
          this.loading = false;
          this.makeToast("Erreur lors de la création de l'utilisateur");
        });
    },
    makeToast(text, append = false) {
      // eslint-disable-next-line
      let toast = this.$toasted.info(text, {
        theme: "bubble",
        position: "bottom-right",
        duration: 15000
      });
    }
  },
  components: { Navbar, CardPrivateInfos }
  // eslint-disable-next-line
};
</script>

<style scoped>
.home-block {
  margin-top: 25%;
}
.login-logo {
  width: 50vw;
  height: 40vw;
  margin: 0px auto 10px auto;
}
.button-page {
  margin-right: 10px;
}
v-ons-button {
  font-size: 1.5rem;
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
  font-size: 1rem;
  margin: 0px;
}
.login-info {
  text-align: center;
  background-color: #78c7f0;
  width: 100%;
  height: 100%;
  padding: 15px;
  color: white;
  font-size: 1rem;
  margin: 0px;
}
.center-screen {
  display: flex;
  margin-top: 20px;
  flex-direction: column;
  align-items: center;
  width: 40vh;
  min-width: 300px;
}
.account-page {
  min-height: calc(100vh - 44px);
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}

ons-input {
  width: 50%;
  min-width: 250px;
}
.btn:hover {
  cursor: pointer;
}

.background {
  /* background-color: green !important; */
  background: linear-gradient(#61d7ff, #2667a8) !important;
}
</style>
