<script>

import {http} from './http.js'

function getAllQuestions () {
  return http.get('/api/questions')
}

export default {
  getAllQuestions
}

</script>