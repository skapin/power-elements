<script>

import http from '@/utils/http'

function getAllQuestions () {
  return http.get('/api/questions')
}

function createAccount (password) {
  return http.post('/api/users/signup', {'password': password})
}

function sendResponsesApi(responses) {
  return http.post('/api/responses', {'responses': JSON.stringify(responses)})
}

function clearUserInfo() {
  return http.delete('/api/user_info')
}

export default {
  getAllQuestions,
  createAccount,
  sendResponsesApi,
  clearUserInfo
}

</script>