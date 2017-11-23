const m = require('mithril')
const Cookies = require('js-cookie')

const Auth = {
  username: '',
  password: '',
  email: '',

  CSRFToken: '',
  getCSRFToken () {
    Auth.CSRFToken = document.querySelector(
      'input[name=csrfmiddlewaretoken]'
    ).value
  },

  setUsername (value) {
    Auth.username = value || ''
  },
  setPassword (value) {
    Auth.password = value || ''
  },
  setEmail (value) {
    Auth.email = value || ''
  },

  canSubmit () {
    return Auth.username !== '' && Auth.password !== ''
  },

  user: {
    id: null,
    name: null,
    token: null,
    loggedIn: false
  },
  errors: {},

  register () {
    m.request({
      method: 'POST',
      url: '/auth/users/create/',
      data: {
        email: Auth.email,
        username: Auth.username,
        password: Auth.password
      },
      withCredentials: true,
      headers: {'X-CSRFToken': Auth.CSRFToken}
    })
    .then((data) => {
      Auth.user.name = data.username
      Auth.user.id = data.id
      Auth.user.registered = true
    })
    .catch((error) => {
      Auth.errors = JSON.parse(error.message)
    })
  },

  login () {
    m.request({
      method: 'POST',
      url: '/auth/token/create/',
      data: {
        username: Auth.username,
        password: Auth.password
      },
      withCredentials: true,
      headers: {'X-CSRFToken': Auth.CSRFToken}
    })
    .then((data) => {
      Auth.user.loggedIn = true
      Cookies.set('sessiontoken', data.auth_token)
    })
    .catch((error) => {
      console.error(error)
    })
  },

  logout () {
    let sessionToken = Cookies.get('sessiontoken')
    m.request({
      method: 'POST',
      url: '/auth/token/destroy/',
      headers: {'Authorization': `Token ${sessionToken}`}
    })
    .then((data) => {
      Cookies.remove('sessiontoken')
      Auth.user.loggedIn = false
    })
    .catch((error) => {
      console.error(error)
    })
  },

  check () {
    let sessionToken = Cookies.get('sessiontoken')
    m.request({
      method: 'GET',
      url: '/auth/me/',
      headers: {'Authorization': `Token ${sessionToken}`}
    })
    .then((data) => {
      Auth.user.name = data.username
      Auth.user.email = data.email
      Auth.user.id = data.id
      Auth.user.loggedIn = true
    })
    .catch((error) => {
      Auth.user.loggedIn = false
      console.error(error)
    })
  }
}

module.exports = Auth
