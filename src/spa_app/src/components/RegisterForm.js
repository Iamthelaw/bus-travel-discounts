const m = require('mithril')
const Auth = require('../models/Auth')
const TextInput = require('./Form/TextInput')
const Button = require('./Form/Button')
const Modal = require('./Modal')

const LoginForm = {
  oninit: Auth.getCSRFToken,
  view (vnode) {
    return m('form', {
      onsubmit (e) {
        e.preventDefault()
        Auth.register()
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
        placeholder: 'John Doe',
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
        m(Button, {
          text: 'Cancel',
          onclick: Modal.hide
        })
      ])
    ])
  }
}

module.exports = LoginForm
