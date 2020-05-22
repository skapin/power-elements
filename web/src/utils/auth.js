
export const Auth = {
  isAuthed: isAuthed,
  saveToken: saveToken,
  getToken: getToken,
  logout: logout
}

function getToken () {
  let data = window.localStorage['logged']
  console.log(data)
  if (data && data !== {}) {
    console.log("OK")
    return JSON.parse(data)
  }
  console.log("LAFLSE")
  return false
}

function isAuthed () {
  return getToken()
}

function logout () {
  window.localStorage.removeItem('logged')
}

function saveToken (token) {
  if (token) {
    window.localStorage.setItem('logged', JSON.stringify(token))
  }
}

export default logout
