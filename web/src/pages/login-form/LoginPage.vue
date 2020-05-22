<template>
  <v-ons-page class="ma_page_login">
    <div class="background"></div>
    <div class="content">
      <div class="login-page">
        <div class="center-screen">
          <!-- <v-ons-row>
            <img class="login-logo" src="../../assets/AIO-logo.png" />
          </v-ons-row> -->
          <v-ons-row>
            <p class="login-header">Connexion Top Secrète !</p>
          </v-ons-row>
          <v-ons-row class="login-form">
            <v-ons-input placeholder="mot de passe" float type="password" v-model="password"></v-ons-input>
          </v-ons-row>
          <v-ons-row>
            <v-ons-col class="button-page">
              <v-ons-button
                class="btn"
                modifier="large"
                @click="forgotPassword"
              >J'ai oublié mon mot de passe</v-ons-button>
            </v-ons-col>
            <v-ons-col>
              <v-ons-button
                :disabled="loading"
                class="btn"
                modifier="large"
                @click="handleLogin()"
              >Se connecter</v-ons-button>
            </v-ons-col>
          </v-ons-row>
        </div>
      </div>
    </div>
  </v-ons-page>
</template>
<script>
import server from "./../../api/server.vue";
import { mapGetters } from "vuex";

export default {
  props: ["toggleMenu", "pageStack"],
  name: "login-page",
  data: function() {
    return {
      password: "",
      loading: false
    };
  },
  computed: mapGetters({
    isLogged: 'getIsLogged',
  }),
  methods: {
    makeToast(text, append = false) {
      // eslint-disable-next-line
      this.$toasted.clear()
      let toast = this.$toasted.error(text, {
        theme: "bubble",
        position: "top-center",
        duration: 5000
      });
    },
    forgotPassword () {
      this.makeToast("Cette fonctionnalité est désactivée")
      this.playSound("bank.mp3")
    },
    handleLogin () {
      this.$toasted.clear()
      this.loading = true
      this.$store
        .dispatch("Login", this.password)
        .then(() => {
          this.loading = false
          this.playSound("correct.mp3")
          clearTimeout(this.time)
          this.goTo("home")
        })
        .catch(error => {
          this.loading = false
          this.password = ""
          this.playSound("faux.mp3")
          // this.$toasted.error("Oh non ! C'est faux :'( ", {
          //   theme: "bubble",
          //   position: "top-center",
          //   duration: 5000
          // });
        });
    },
    playAmbiance () {
      this.playSound("maillon_ambiance.mp3")
      this.time = setTimeout(function () {
          this.playAmbiance()
        }.bind(this), 4400)
    }
  },
  mounted: function() {
    this.playAmbiance()
  },
  components: {  }
  // eslint-disable-next-line
};
</script>

<style scoped>
.home-block {
  margin-top: 25%;
}
.login-logo {
  width: 280px;
  height: 200px;
  margin: 0px auto 10px auto;
}
.button-page {
  margin-right: 10px;
}
v-ons-button {
  font-size: 1.5rem;
}

.btn:hover {
  cursor: pointer !important;
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
  font-size: 1.5rem;
  margin: 0px;
}
.center-screen {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 40vh;
  min-width: 300px;
  /*background: url('../../assets/back_maillon.png') no-repeat;
  padding: 100px;*/

}
.login-page {
  min-height: calc(100vh - 44px);
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
}

.background {
  /* background-color: green !important; */
  background: linear-gradient(#2667a8, #050505, #080254) !important;
}

ons-input {
  width: 50%;
  min-width: 250px;
}
</style>
