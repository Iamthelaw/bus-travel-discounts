const m = require('mithril')
const Auth = require('../models/Auth')
const TextInput = require('./Form/TextInput')
const Button = require('./Form/Button')

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
      m(TextInput, {
        label: 'Email',
        type: 'email',
        placeholder: 'love2travel@gmail.com',
        oninput: m.withAttr('value', Auth.setEmail),
        value: Auth.email,
        errors: Auth.errors && Auth.errors.email
      }),
      m(TextInput, {
        label: 'Username',
        type: 'text',
        placeholder: 'johndoe2',
        oninput: m.withAttr('value', Auth.setUsername),
        value: Auth.username,
        errors: Auth.errors && Auth.errors.username
      }),
      m(TextInput, {
        label: 'Password',
        type: 'password',
        placeholder: '******',
        oninput: m.withAttr('value', Auth.setPassword),
        value: Auth.password,
        errors: Auth.errors && Auth.errors.password
      }),
      m('.field.is-grouped', [
        m(Button, {
          submit: true,
          primary: true,
          text: 'Register',
          disabled: !Auth.canSubmit()
        }),
        m('a.button[href=/]', {oncreate: m.route.link}, 'Cancel')
      ])
    ])
  }
}

module.exports = LoginForm
