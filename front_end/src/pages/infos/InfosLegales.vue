<template>
  <v-ons-page>
    <navbar returnPath="home"></navbar>
    <ons-card>
        <div class="title">
            <h1>Informations légales</h1>
        </div>
        <div class="content">
            <p>
                Sed ut tum ad senem senex de senectute, sic hoc libro ad amicum amicissimus scripsi de amicitia. Tum est Cato locutus, quo erat nemo fere senior temporibus illis, nemo prudentior; nunc Laelius et sapiens (sic enim est habitus) et amicitiae gloria excellens de amicitia loquetur. Tu velim a me animum parumper avertas, Laelium loqui ipsum putes. C. Fannius et Q. Mucius ad socerum veniunt post mortem Africani; ab his sermo oritur, respondet Laelius, cuius tota disputatio est de amicitia, quam legens te ipse cognosces.

                Post haec indumentum regale quaerebatur et ministris fucandae purpurae tortis confessisque pectoralem tuniculam sine manicis textam, Maras nomine quidam inductus est ut appellant Christiani diaconus, cuius prolatae litterae scriptae Graeco sermone ad Tyrii textrini praepositum celerari speciem perurgebant quam autem non indicabant denique etiam idem ad usque discrimen vitae vexatus nihil fateri conpulsus est.

                Quaestione igitur per multiplices dilatata fortunas cum ambigerentur quaedam, non nulla levius actitata constaret, post multorum clades Apollinares ambo pater et filius in exilium acti cum ad locum Crateras nomine pervenissent, villam scilicet suam quae ab Antiochia vicensimo et quarto disiungitur lapide, ut mandatum est, fractis cruribus occiduntur.
            </p>
        </div>
    </ons-card>
  </v-ons-page>
</template>

<script>
import Navbar from '../../components/navbar/Navbar'

export default {
  name: 'infos-legales',
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
