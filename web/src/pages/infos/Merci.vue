<template>
  <v-ons-page>
    <navbar returnPath="home"></navbar>
    <ons-card class="mycard">
        <div class="content">
            <img class="thank_img" src="../../assets/thank_you.png" title="Merci">
        </div>
        <v-ons-row v-if="showForm">
            <v-ons-col><h2>Êtes vous en entreprise ?</h2></v-ons-col>
            <v-ons-col>
                <v-ons-list>
                    <v-ons-list-item v-for="(propal, $index) in propositions" :key="propal" tappable>
                        <label class="left">
                            <v-ons-radio
                            :input-id="'radio-' + $index"
                            :value="propal"
                            v-model="selectedPropal"
                            ></v-ons-radio>
                        </label>
                        <label :for="'radio-' + $index" class="center">
                            {{ propal }}
                        </label>
                    </v-ons-list-item>
                </v-ons-list>
            </v-ons-col>
            <v-ons-col><v-ons-button class="btn" @click="updateAccount()">Valider</v-ons-button></v-ons-col>
        </v-ons-row>
    </ons-card>
  </v-ons-page>
</template>

<script>
import Navbar from '../../components/navbar/Navbar'
import server from "./../../api/server.vue"

export default {
  name: 'merci',
  components: {
    Navbar
  },
  data() {
    return {
      qcmAnswers: {},
      questionsList: [],
      validateDisabled: true,
      propositions: ['OUI', 'NON'],
      selectedPropal: 'OUI',
      showForm: true
    }
  },
  methods: {
    updateAccount() {
        var is_here = false
        if (this.selectedPropal === 'OUI') {
            is_here = true
        }
        server.isAtWork(is_here).then(() => {
            this.makeToast('Merci !!')
            this.showForm = false
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

.btn:hover {
  cursor: pointer;
}
.mycard {
  max-width: 90vw;
  margin: 200px auto;
  text-align: center;
}

.thank_img {
  width: 100%;
}

</style>
