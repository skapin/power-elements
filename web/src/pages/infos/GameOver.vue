<template>
  <v-ons-page>
    <div id="boss">
      <v-ons-row id="control">
        <v-ons-col class="">
        </v-ons-col>
      </v-ons-row>
      <div class="speaking-bagul">
        Tu as perdu Ahhaha ! A moi les petits !
      </div>
    </div>
  </v-ons-page>
</template>

<script>
import Navbar from '../../components/navbar/Navbar'

export default {
  name: 'game-over',
  components: {
    Navbar
  },
  data() {
    return {
    }
  },
  methods: {
    
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
  width:auto;
  background: url('../../assets/dark_bagul_win.jpg');
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  background-color: #000000;
  position: relative;
}
#boss .speaking-bagul {
  position: absolute;
  bottom: 60%;
  left: 50px;
  text-align: center;
  color: #a0000c;
  font-size: 2em;
}

.thank_img {
  width: 100%;
}

</style>
