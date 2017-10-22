const m = require('mithril')

const RegisterForm = require('./../components/RegisterForm')
const MinPage = require('./../components/MinPage')

module.exports = {
  view () {
    return m(MinPage, [
      m('h1.title', 'Register'),
      m(RegisterForm)
    ])
  }
}
