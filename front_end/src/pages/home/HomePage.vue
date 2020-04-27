<template>
  <v-ons-page>
    <navbar enabled="false"></navbar>
    <div class="home-page">
      <div v-for="(row, indexRow) in questionsList" v-bind:key="indexRow">
        <question @clicked="onClickChild"
                :questionId="row.uniqid"
                :question="row.name"/>
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
      qcmAnswers: [],
      questionsList: []
    }
  },
  methods: {
    onClickChild (value) {
      if (this.qcmAnswers[value.id] === undefined) {
        this.qcmAnswers[value.id] = []
        this.qcmAnswers[value.id] = value.answer
      } else {
        this.qcmAnswers[value.id] = value.answer
      }
    },
    getAppQuestions () {
      server.getAllQuestions().then((result) => {
        this.questionsList = result.data
      })
    }
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
.body {
  margin-top: 50px;
}
.home-page {
  height: 100vh;
  overflow: auto;
  background: linear-gradient(#61d7ff, #2667a8);
}
</style>
