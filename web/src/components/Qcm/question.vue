<template>
  <v-ons-card class="card">
    <div class="title">
      <h1>{{ question }}</h1>
    </div>
    <div class="content">
      <v-ons-row>
        <v-ons-col width="10%" vertical-align="center">
          <span> Non </span>
        </v-ons-col>
        <v-ons-col width="80%" vertical-align="center">
          <v-ons-range @click="clickAnswer()" v-model="value" style="width: 90%;"></v-ons-range>
        </v-ons-col>
        <v-ons-col width="10%" vertical-align="center">
          <span> Oui </span>
        </v-ons-col>
      </v-ons-row>
      <!-- <v-ons-row>
        <v-ons-col vertical-align="center"> -->
          <v-ons-card class="call-card" v-show="displayCallButton">
            <div class="content">
          Vous pouvez appeler votre correspondant dans l’entreprise pour échanger avec lui et prendre une décision ensemble du choix qui est fait pour la journée
        </div>
      </v-ons-card>
        <!-- </v-ons-col>
      </v-ons-row> -->
    </div>
  </v-ons-card>
</template>

<script>

export default{
  props: {
    id: {
      default: ''
    },
    question: {
      default: 'covid AIO',
    },
    questionId: {
      default: ''
    }
  },
  data () {
    return {
      displayCallButton: false,
      value: '',
    }
  },
  methods: {
    clickAnswer () {
      this.displayCallButton = (this.value > 70)
      this.$emit('clicked', {'id': this.questionId, 'answer': this.value, 'question': this.question})
    },
  }
  // eslint-disable-next-line
};

</script>

<style scoped>
.call-card {
 background-color: #ffd175;
}
.card {
  width: 80%;
  margin: 0 auto;
  margin-bottom: 1%;
  margin-top: 1%;
}
.center-screen {
  top: 50%;
  left: 50%;
  vertical-align: middle;
  /* bring your own prefixes */
  min-width: 273px;
}
</style>