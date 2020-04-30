<template>
  <v-ons-page>
    <navbar returnPath="home"></navbar>
    <ons-card>
        <div class="title">
            <h1>Merci !</h1>
        </div>
        <div class="content">
          <p>
          </p>
            <img src="../../assets/thank_you.png" title="Merci">
        </div>
    </ons-card>
  </v-ons-page>
</template>

<script>
import Navbar from '../../components/navbar/Navbar'

export default {
  name: 'merci',
  components: {
    Navbar
  },
  data() {
    return {
      qcmAnswers: {},
      questionsList: [],
      validateDisabled: true
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
   // this.getAppQuestions()
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
  background: linear-gradient(#61d7ff, #2667a8);
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
