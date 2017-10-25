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
      }
    }, [
      m(TextInput, {
        label: 'Username',
        type: 'text',
        placeholder: 'John Doe',
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
