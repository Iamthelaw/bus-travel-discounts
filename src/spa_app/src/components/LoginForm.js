const m = require('mithril')

const Auth = require('../models/Auth')

const Username = require('./Form/Field/Username')
const Password = require('./Form/Field/Password')
const ActionButtonGroup = require('./Form/ActionButtonGroup')

const LoginForm = {
  oninit: Auth.getCSRFToken,
  view () {
    return m('form', {
      onsubmit (e) {
        e.preventDefault()
        Auth.login()
        if (Auth.user.loggedIn) {
          Auth.check()
          m.route.set('/')
        }
      }
    }, [
      m(Username),
      m(Password),
      m(ActionButtonGroup, {text: 'Login', disabled: !Auth.canSubmit()})
    ])
  }
}

module.exports = LoginForm
