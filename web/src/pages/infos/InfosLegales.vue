<template>
  <v-ons-page>
    <navbar returnPath="home"></navbar>
    <ons-card>
        <div class="title">
            <h1>Informations légales</h1>
        </div>
        <div class="content">
            <p>
                Site web réalisé uniquement par AIO, pour AIO en 2020. Le serveur est hebergé en France, à Vitry sur seine.<br>
            </p>
            <p>
                Pour toutes questions, n'hesiter pas à consulter la rubrique "Confidentialité", nous demander de vive voix ou même nous envoyer un mail <i><small>(florian.boudinet aio eu)</small></i>
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
  },
  mounted: function () {
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
