<template>
  <v-ons-card class="card">
    <div class="title">
      <h1>{{ question }}</h1>
    </div>
    <div class="content">
      <v-ons-row>
        <v-ons-col width="10%" vertical-align="center">
          <span> 0 </span>
        </v-ons-col>
        <v-ons-col width="80%" vertical-align="center">
          <v-ons-range v-model="volume" style="width: 90%;"></v-ons-range>
        </v-ons-col>
        <v-ons-col width="10%" vertical-align="center">
          <span> 100 </span>
        </v-ons-col>
      </v-ons-row>
    </div>
  </v-ons-card>
</template>

<script>

export default{
  props: {
    question: {
      default: 'covid AIO',
    },
  },
  data () {
    return {
      checkedAnswer: '',
      volume: '',
      progressValue: null,
      selectedAnswer: -1,
      selectedAnswerObj: null
    }
  },
  methods: {
    classResponse: function ($index, isCorrectAnswer) {
      return {'selected-response': this.selectedAnswer === $index && !this.displayResponse, 'bad-response': this.selectedAnswer === $index && this.displayResponse && !isCorrectAnswer, 'good-response': this.selectedAnswer === $index && this.displayResponse && isCorrectAnswer}
    },
    clickAnswere ($index, obj) {
      if (!this.displayResponse) {
        this.selectedAnswer = $index
        this.selectedAnswerObj = obj
        this.$emit('clicked', {'id': this.id, 'answer': obj, 'question_id': this.questionId})
      }
    },
  },
  mounted () {
  }
  // eslint-disable-next-line
};

</script>

<style scoped>
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