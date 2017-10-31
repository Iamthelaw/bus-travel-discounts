const m = require('mithril')
const Auth = require('../models/Auth')
const TextInput = require('./Form/TextInput')
const Button = require('./Form/Button')

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
      m(TextInput, {
        label: 'Username',
        type: 'text',
        placeholder: 'johndoe2',
        oninput: m.withAttr('value', Auth.setUsername),
        value: Auth.username
      }),
      m(TextInput, {
        label: 'Password',
        type: 'password',
        placeholder: '******',
        oninput: m.withAttr('value', Auth.setPassword),
        value: Auth.password
      }),
      m('.field.is-grouped', [
        m(Button, {
          submit: true,
          primary: true,
          text: 'Login',
          disabled: !Auth.canSubmit()
        }),
        m('a.button[href=/]', {oncreate: m.route.link}, 'Cancel')
      ])
    ])
  }
}

module.exports = LoginForm
