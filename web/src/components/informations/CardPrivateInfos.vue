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
      <div class="title title-font-size">
        Informations importantes
      </div>
      <div class="content content-font-size">
       <p>Le questionnaire est anonyme, nous ne collectons aucune donnée personelle.</p>
       <p>Le but de cette application est d'évaluer le risque sanitaire au sein de l'entreprise en regroupant les réponses anonymes des collaborateurs.</p>
      </div>
    </v-ons-card>
</template>

<script>
export default {
  name: 'CardPrivateInfos',
};
</script>
<style scoped>
.content-font-size{
    font-size: 1rem !important;
}

.title-font-size {
    font-size: 1.3rem !important ;
}
</style>
