<template>
  <v-ons-page>
    <navbar></navbar>
    <!-- Camera view -->
    <VueCamera :striker="striker"></VueCamera>
    <section style="margin: 16px">
      <v-ons-button modifier="large"
                    style="margin: 6px 0"
                    id="play-btn"
                    @click="changePlayState">
        {{striker.playButtonTxt}}
      </v-ons-button>
      <span class="notification"
            modifier="large"
            :style="{ 'background-color': labelColor, margin: '6px 0' }"
            id="label-notification">
        {{labelTxt}}
      </span>
    </section>
  </v-ons-page>
</template>

<script>
import Navbar from '../../components/navbar/Navbar';
import VueCamera from '../../components/camera/vue-camera.vue'

export default {
  name: 'posts-page',
  components: {
    Navbar,
    VueCamera
  },
  data() {
    return {
      striker: {
        isStreaming: false,
        strikeLabel: "Not connected",
        playButtonTxt: "Play"
      }
    }
  },
  methods: {
    changePlayState() {
      if(this.striker.isStreaming){
        this.striker.isStreaming = false
        this.striker.playButtonTxt = "Play"
        this.striker.strikeLabel = "NotConnected"
        console.log('Setting play state')
      } else {
        this.striker.isStreaming = true
        this.striker.playButtonTxt = "Stop"
        this.striker.strikeLabel = "..."
        console.log('Setting pause state')
      }
    },
  },
  computed: {
    labelTxt: function () {
      return this.striker.strikeLabel
    },
    labelColor: function () {
      return (this.striker.strikeLabel == 'In' ? 'MediumSeaGreen' : 'red')
    }
  }
};
</script>

<style lang='scss' scoped>
.page-title {
  text-align: center;
}
.body {
  margin-top: 50px;
}
</style>
