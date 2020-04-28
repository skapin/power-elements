<template>
  <v-ons-page >
  
    <navbar enabled="false"></navbar>
    <div class="home-page" v-if="questionsList">
      <div v-for="(row, indexRow) in questionsList" v-bind:key="indexRow">
        <question @clicked="onClickChild"
                :questionId="row.uniqid"
                :question="row.name"/>
      </div>
      <div class="validation-button">
        <v-ons-button class="btn" @click="sendResponses()" modifier="large">Valider</v-ons-button>
      </div>
    </div>
  </v-ons-page>
</template>

<script>
import Navbar from '../../components/navbar/Navbar';
import Question from '../../components/Qcm/question'
import server from './../../api/server.vue'

export default {
  name: 'posts-page',
  components: {
    Navbar,
    Question
  },
  data() {
    return {
      qcmAnswers: {},
      questionsList: []
    }
  },
  methods: {
    onClickChild (value) {
      if (this.qcmAnswers[value.id] === undefined) {
        this.qcmAnswers[value.id] = []
        this.qcmAnswers[value.id] = value.answer
      } else {
        this.qcmAnswers[value.id] = {'value': value.answer, 'question': value.question}
      }
      console.log(this.qcmAnswers)
    },
    getAppQuestions () {
      server.getAllQuestions().then((result) => {
        this.questionsList = result.data
        this.initResponses()
      })
    },
    initResponses() {
      this.questionsList.forEach(question => {
        this.qcmAnswers[question.uniqid] = {'value': '50', 'question': question.name}
      });
    },
    sendResponses() {
      var jwt = window.localStorage.getItem('jwtToken')
      server.sendResponsesApi(jwt, this.qcmAnswers).then(() => {
        this.makeToast('Réponses envoyées ! Merci !')
      })
    },
    makeToast (text, append = false) {
      // eslint-disable-next-line
      let toast = this.$toasted.info(text, {
        theme: 'bubble',
        position: 'bottom-right',
        duration: 5000
      })
    },
  },
  mounted: function () {
   this.getAppQuestions()
  },
};
</script>

<style lang='scss' scoped>
.bgno {
  background: inherit;
}

.page-title {
  text-align: center;
}

.btn:hover {
  cursor: pointer;
}
.home-page {

  max-width: 1200px;
  margin: auto;
  min-height: calc(100vh - 44px);
}
.validation-button {
  width: 50%;
  min-width: 300px;
  margin: 0 auto;
  margin-bottom: 1%;
  margin-top: 3%;
}
</style>
