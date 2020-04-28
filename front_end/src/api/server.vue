<script>

import {http} from './http.js'

function getAllQuestions () {
  return http.get('/api/questions')
}

function createAccount (password) {
  return http.post('/api/users/signup', {'password': password})
}

function login(username, password) {
  return http.post('/api/users/login', {'username': username, 'password': password})
}

function saveResponses(jwt, responses) {
  return http.post('/api/responses', {'jwt': jwt, 'responses': responses})
}

export default {
  getAllQuestions,
  createAccount,
  login,
  saveResponses
}

</script>