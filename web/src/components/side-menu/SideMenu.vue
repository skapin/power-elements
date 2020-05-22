<template>
  <v-ons-page>
    <v-ons-toolbar modifier="transparent"></v-ons-toolbar>
    <v-ons-list-title>Infos</v-ons-list-title>
    <v-ons-list>
      <v-ons-list-item modifier="chevron" tappable @click="goTo('home')">
        <div class="left">
          <v-ons-icon fixed-width icon="fa-home"></v-ons-icon>
        </div>
        <div class="center">Accueil</div>
      </v-ons-list-item> 
      <v-ons-list-item modifier="chevron" tappable @click="goTo('infosLegales')">
        <div class="left">
          <v-ons-icon fixed-width icon="fa-info"></v-ons-icon>
        </div>
        <div class="center">Infos légales</div>
      </v-ons-list-item>
      <v-ons-list-item modifier="chevron" tappable @click="goTo('politiqueConfidentialite')">
        <div class="left">
          <v-ons-icon fixed-width icon="fa-info"></v-ons-icon>
        </div>
        <div class="center">Confidentialité</div>
      </v-ons-list-item>
      <v-ons-list-item class="admin" modifier="chevron" tappable @click="goTo('admin')">
        <div class="left">
          <v-ons-icon fixed-width icon="fa-bar-chart"></v-ons-icon>
        </div>
        <div class="center">Panel admin</div>
      </v-ons-list-item>
      <v-ons-list-item modifier="chevron" tappable @click="signout()">
        <div class="left">
          <v-ons-icon fixed-width icon="fa-sign-out"></v-ons-icon>
        </div>
        <div class="center">Déconnexion</div>
      </v-ons-list-item>
    </v-ons-list>
  </v-ons-page>
</template>

<script>
import { mapGetters } from 'vuex';
import store from '../../store';
import logout from '../../utils/auth.js'

export default {
  name: 'side-menu',
  store,
  data() {
    return {
      msg: 'OpenWeatherMap',
    }
  },
  computed: mapGetters({
    info: 'getInfo',
  }),
  methods: {
    signout() {
      this.$store.dispatch('LogOut').then(() => {
        location.reload()
      })
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .header {
    text-align: center;
    margin-bottom: 20px;
  }
  img {
    max-width: 150px;
  }
  ons-list-item {
    cursor: pointer;
  }
@media screen and (max-width: 1000px) {
  .admin {
    display: none;
  }
}
</style>
