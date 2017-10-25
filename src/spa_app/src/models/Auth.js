const m = require('mithril')

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
      m.route.set('/thank-you')
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
      console.log(data)
    })
  }
}

module.exports = Auth
