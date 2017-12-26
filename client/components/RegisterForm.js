const m = require('mithril')

const Auth = require('../models/Auth')

const Username = require('./Form/Field/Username')
const Password = require('./Form/Field/Password')
const Email = require('./Form/Field/Email')
const ActionButtonGroup = require('./Form/ActionButtonGroup')

const LoginForm = {
  oninit: Auth.getCSRFToken,
  view (vnode) {
    return m('form', {
      onsubmit (e) {
        e.preventDefault()
        Auth.register()
        m.route.set('/thank-you')
      }
    }, [
      m(Email),
      m(Username),
      m(Password),
      m(ActionButtonGroup, {text: 'Register', disabled: !Auth.canSubmit()})
    ])
  }
}

module.exports = LoginForm
