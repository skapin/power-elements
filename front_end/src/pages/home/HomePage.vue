<template>
  <v-ons-page>
    <navbar enabled="false"></navbar>
    <div class="home-page">
      <question @clicked="onClickChild"
                questionId='1'
                id='1'
                question='Question 1'/>
      <question @clicked="onClickChild"
                questionId='2'
                id='2'
                question='Question 2'/>
      <question @clicked="onClickChild"
                questionId='3'
                id='3'
                question='Question 3'/>
    </div>
  </v-ons-page>
</template>

<script>
import Navbar from '../../components/navbar/Navbar';
import Question from '../../components/Qcm/question'

export default {
  name: 'posts-page',
  components: {
    Navbar,
    Question
  },
  data() {
    return {
      qcmAnswers: []
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
      console.log(this.qcmAnswers)
    },
  },
  computed: {
  }
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
