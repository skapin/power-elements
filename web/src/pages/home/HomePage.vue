<template>
  <v-ons-page>
    <navbar enabled="false" navType="menu"></navbar>
    <div class="home-page" v-if="questionsList">
      <div v-for="(row, indexRow) in questionsList" v-bind:key="indexRow">
        <question @clicked="onClickChild"
                :questionId="row.uniqid"
                :question="row.name"/>
      </div>
      <div class="validation-button btn">
        <v-ons-button 
          @click="sendResponses()" 
          :disabled="validateDisabled || loading" 
          modifier="large"
        >
          Valider
        </v-ons-button>
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
      questionsList: [],
      validateDisabled: true,
      loading: false
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
      this.validateDisabled = false
    },
    getAppQuestions () {
      server.getAllQuestions().then((result) => {
        this.questionsList = result
        this.initResponses()
      })
    },
    initResponses() {
      this.questionsList.forEach(question => {
        this.qcmAnswers[question.uniqid] = {'value': '50', 'question': question.name}
      });
    },
    sendResponses() {
      this.loading = true
      server.sendResponsesApi(this.qcmAnswers).then(() => {
        this.loading = false
        this.makeToast('Réponses envoyées ! Merci !')
        this.goTo('merci')
      }).catch((err) => {
        this.loading = false
        if (err.response.status == 404) {
          let toast = this.$toasted.error('Compte introuvable...', {
            theme: 'bubble',
            position: 'bottom-center',
            duration: 5000
          })
        }
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
