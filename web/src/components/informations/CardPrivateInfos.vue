<style scoped>
.bluecard {
  background-color: #215d9e;
  border: solid 1px white;
  color: white;
}
.bluecard p {
  color: white;
}
</style>

<template>
  <v-ons-card class="bluecard">
      <div class="title">
        Informations importantes
      </div>
      <div class="content">
       <p>Le questionnaire est anonyme, nous ne collectons aucune donnée personelle.</p>
       <p>Le but de cette application est d'évaluer la possible présence du COVID-19 au sein de l'entreprise en regroupant les réponses anonymes des collaborateurs.</p>
      </div>
    </v-ons-card>
</template>

<script>
export default {
  name: 'CardPrivateInfos',
};
</script>
