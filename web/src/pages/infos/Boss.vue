<template>
  <v-ons-page>
    <navbar returnPath="home"></navbar>
    <div id="boss">
      <v-ons-row id="control">
        <v-ons-col class="">
          <v-ons-button
            class="attack"
            modifier="small"
            @click="attaquer"
          >Attaquer !</v-ons-button>
        </v-ons-col>
      </v-ons-row>
      <div class="speaking-bagul">
        Mouahah Je suis le Dark Bagoul !
      </div>
    </div>
  </v-ons-page>
</template>

<script>
import Navbar from '../../components/navbar/Navbar'

export default {
  name: 'boss',
  components: {
    Navbar
  },
  data() {
    return {
    }
  },
  methods: {
    attaquer () {
      this.playSound("boss_fail.mp3")
    }
    
  },
  mounted: function () {
  },
};
</script>

<style scoped>

.attack{
  background-color: rgba(0,0,0,0.8) !important;
  border: 3px solid !important;
}
#control {
  padding-top: 100%;
}
#boss {
  text-align: center;
  height: 100%;
  background: url('../../assets/dark_bagul.jpg');
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  background-color: #000000;
  position: relative;
}
#boss .speaking-bagul {
  position: absolute;
  bottom: 20%;
  left: 50px;
  text-align: center;
  color: #5e000c;
}

.thank_img {
  width: 100%;
}

</style>
