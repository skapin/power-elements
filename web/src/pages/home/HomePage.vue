<template>
  <v-ons-page>
    <navbar enabled="false" navType="menu"></navbar>
    <div class="home-page page-template">
      <v-ons-row style="height: 50%">
        <v-ons-col vertical-align="center" id="part1">
        </v-ons-col>
      </v-ons-row>
      <v-ons-row>
        <v-ons-col vertical-align="center" id="hal">
          <img 
              src="../../assets/back_app_home.png" 
              alt="hal"
              @click="goTo('boss')"
          >
          <div id="timer">
            {{getBossTimer}}
          </div>
        </v-ons-col>
      </v-ons-row>
      <v-ons-row>
        <v-ons-col vertical-align="center">
        </v-ons-col>
      </v-ons-row>
    </div>
  </v-ons-page>
</template>

<script>
import Navbar from "../../components/navbar/Navbar";
import { mapGetters } from "vuex";


export default {
  name: "posts-page",
  components: {
    Navbar
  },
  data() {
    return {
      qcmAnswers: {},
      questionsList: [],
      validateDisabled: true,
      loading: false,
      bossTimerFct: null
    };
  },
  computed: mapGetters(['getBossTimer']),
  methods: {
    bossTimer () {
      this.$store.commit('increaseTimer')
      this.bossTimerFct = setTimeout(function () {
            this.bossTimer()
          }.bind(this), 1000)

    }
  },
  mounted: function() {
    this.$store.commit('startBossTimer')
    this.bossTimer()
  }
};
</script>

<style>
.page-title {
  text-align: center;
}

.btn:hover {
  cursor: pointer;
}
#part1 {
  height: 40%;
}
.page-template {
  height: 100%;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  -ms-flex-align: center;
  -webkit-align-items: center;
  -webkit-box-align: center;
  align-items: center;
  color:white;

  max-width: 1200px;
  margin: auto;
  min-height: calc(100vh - 44px);
  background: linear-gradient(#282923, #050505, #282923) !important;
}
.home-page {
}
.validation-button {
  width: 50%;
  min-width: 300px;
  margin: 0 auto;
  margin-bottom: 1%;
  margin-top: 3%;
}
#hal {
  text-align: center;
}
#hal img
{
  width: 70%;
  height: auto;
}
#hal img:active
{
  width: 65%;
}
</style>
