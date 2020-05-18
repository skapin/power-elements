<template>
  <v-ons-card class="card">
    <div class="content">
      <v-ons-row>
        <v-ons-col width="50%" vertical-align="center">
          <h3>{{ question }}</h3>
        </v-ons-col>
        <v-ons-col width="3%"></v-ons-col>
        <v-ons-col width="12%" vertical-align="center"><p class="float-right"><b>Non</b></p></v-ons-col>
        <v-ons-col width="22%" vertical-align="center">
          <!-- <v-ons-range @click="clickAnswer()" v-model="value" style="width: 90%;"></v-ons-range> -->
          <v-ons-switch @click="clickAnswer()" :input-id="questionId"
            v-model="value" class="float-right btn"
          ></v-ons-switch>
        </v-ons-col>
        <v-ons-col width="12%" vertical-align="center"><p class="float-right"><b>Oui</b></p></v-ons-col>
      </v-ons-row>
      <!-- <v-ons-row>
        <v-ons-col vertical-align="center"> -->
          <v-ons-card class="call-card" v-show="displayCallButton">
            <div class="content" ><p>
          Vous pouvez appeler votre correspondant dans l’entreprise pour échanger avec lui et prendre une décision ensemble du choix qui est fait pour la journée:</p>
          <a href="tel:0681786159"><v-ons-button class="btn">Appeler</v-ons-button></a>
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
      default: 'AIO Strawpoll',
    },
    questionId: {
      default: ''
    }
  },
  data () {
    return {
      displayCallButton: false,
      value: false,
    }
  },
  methods: {
    clickAnswer () {
      this.displayCallButton = !this.displayCallButton
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
.btn:hover {
  cursor: pointer;
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
.float-right {
  float: right;
}
</style>