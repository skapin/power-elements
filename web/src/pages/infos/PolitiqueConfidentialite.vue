<template>
  <v-ons-page id="politique">
    <navbar returnPath="home"></navbar>
    <ons-card>
      <div class="title">
          <h1>Notre engagement sur la confidentialité</h1>
      </div>
      <div class="content">
        <v-ons-list class="bubble">
          <v-ons-list-item expandable :expanded.sync="isExpanded">
            Quelles sont les informations enregistrées ?
            <div class="expandable-content">Votre nom de compte anonyme, votre mot de passe chiffré (donc illisible), ainsi que la réponse aux questions avec date.
            Lien vers <a href="/static/img/db_schema.png"> la table User</a> et <a href="/static/img/db_schema_2.png">la table de réponse</a>

          </div>
          </v-ons-list-item>
        </v-ons-list>
        <v-ons-list class="bubble">
          <v-ons-list-item expandable :expanded.sync="isExpanded">
            J'ai peur qu'un tier puisse accède aux données, ou sont elles stockées ?
            <div class="expandable-content">L'application est hébergé sur un serveur dédié à AIO fournit par une société française (Online, groupe Illiad). <br>Le serveur se situe physiquement dans le datacenter 2 (DC2) à Vitry sur Seine
              (<a href="https://documentation.online.net/fr/dedicated-server/overview/datacenters#scaleway_datacenter_dc2" >Plus d'info)</a></div>
          </v-ons-list-item>
        </v-ons-list>
        <v-ons-list class="bubble">
          <v-ons-list-item expandable :expanded.sync="isExpanded">
            Je veux supprimer mes données, comment faire ?
            <div class="expandable-content">Cette action est possible mais irréversible. Pour cela
              <v-ons-button @click="removeUserData">Cliquez ici</v-ons-button>
            </div>
          </v-ons-list-item>
        </v-ons-list>
        <v-ons-list class="bubble">
          <v-ons-list-item expandable :expanded.sync="isExpanded">
            J'ai vu sur internet ou à la TV que l'on pouvait m'identifier et me tracker quand même à cause de l'adresse IP. Est-ce vrai ? Comment ça fonctionne ?
            <div class="expandable-content">
              Une <a href="https://fr.wikipedia.org/wiki/Adresse_IP" title="adresse ip">adresse IP</a> est un identifiant fournit par votre fournisseur d'accès internet (fixe ou téléphone portable). Elle permet d'identifier l'équipement (box ou téléphone) et ainsi de transférer les paquets internet d'un point A à un point B (entre vous et un site web par exemple). Cet identifiant est une suite de chiffres. Seul votre fournisseur d'accès internet peut faire le lien entre cette suite de chiffres et le compte internet (et donc le nom et l'adresse). Il faut une procédure légale, comme une enquête policière pour de graves délits, pour demander et accéder à ces informations. En France, la <a href="https://www.cnil.fr/" title="cnil">CNIL</a> est l'organisme indépendant qui s'assure des droits et libertés sur internet.<br>
              Il faut savoir que l'adresse IP de votre équipement n'est pas fixe et peut changer (être attribuée à un autre usager voir être falsifiée). À titre d'information, dans un même logement ou entreprise, tous les équipements ont la même adresse IP.
            </div>
          </v-ons-list-item>
        </v-ons-list>
      </div>
    </ons-card>
  </v-ons-page>
</template>

<script>
import Navbar from '../../components/navbar/Navbar'
import server from './../../api/server.vue'

export default {
  name: 'politique-confidentialite',
  components: {
    Navbar
  },
  data() {
    return {
      isExpanded: false
    }
  },
  methods: {
    removeUserData () {
      server.clearUserInfo().then(result => {
        this.$store.dispatch('LogOut').then(() => {
          location.reload()
        })

      }).catch((err) => {
        if (err.response.status == 404) {
          let toast = this.$toasted.error('Votre compte est déjà supprimé...', {
            theme: 'bubble',
            position: 'bottom-center',
            duration: 10000
          })
        }
      })
    }

  },
  mounted: function () {
  },
};
</script>

<style lang='css'>
a {
  text-decoration: none;
  font-style: italic;
  color:cornflowerblue;
  font-weight: bold;
}

#politique .list-item {
  background-color: cornflowerblue;
  font-weight: bold;
  padding-left: 0;
  color: white;
  border-radius: 10px;
}
#politique .center{
  padding-left: 2%;
}
#politique .expandable-content {
  font-weight: normal;
  background-color: #d4deed;
  padding-left: 4%;
  color: #333333;
}
</style>
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
.bubble {
  margin-bottom: 5px;
}
</style>
