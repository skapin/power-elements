
export const Auth = {
  checkValidity: checkValidity,
  isAuthed: isAuthed,
  payload: payload,
  parseJwt: parseJwt,
  saveToken: saveToken,
  getToken: getToken,
  isTokenFresh: isTokenFresh,
  logout: logout
}

function getToken () {
  let data = window.localStorage['jwtToken']
  if (data && data !== {}) {
    return JSON.parse(data)
  }
  return false
}

function isAuthed () {
  let parsedToken = parseJwt(getToken())
  return (parsedToken && isTokenFresh(parsedToken))
}

function parseJwt (token) {
  if (!token) {
    return false
  }
  try {
    return payload(token)
  } catch (e) {
    console.error('Invalid Token Session', 'JWT error ' + e.message)
    return false
  }
}

function isTokenFresh (parsedToken) {
  if (parsedToken) {
    var isAuthed = (Math.round(new Date().getTime() / 1000) <= parsedToken.exp)
    if (isAuthed) {
      /* setTimeout(function () {
        this.checkValidity()
      }.bind(this), 50000) */
    }
    return isAuthed
  } else {
    return false
  }
}

function payload (token) {
  var base64Url = token.split('.')[1]
  var base64 = base64Url.replace('-', '+').replace('_', '/')

  return JSON.parse(window.atob(base64))
}

function checkValidity () {
  if (!isAuthed()) {
    window.location.reload()
  } else {
    setTimeout(function () {
      this.checkValidity()
    }.bind(this), 5000)
  }
}
function logout () {
  window.localStorage.removeItem('jwtToken')
}

function saveToken (token) {
  if (token) {
    window.localStorage.setItem('jwtToken', JSON.stringify(token))
  }
}

export default logout
