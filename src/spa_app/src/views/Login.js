const m = require('mithril')

const LoginForm = require('./../components/LoginForm')
const MinPage = require('./../components/MinPage')

module.exports = {
  view () {
    return m(MinPage, [
      m('h1.title', 'Login'),
      m(LoginForm)
    ])
  }
}
