const m = require('mithril')

const Auth = require('./../../../models/Auth')
const TextInput = require('./../TextInput')

module.exports = {
  view () {
    return m(TextInput, {
      label: 'Password',
      type: 'password',
      placeholder: '******',
      oninput: m.withAttr('value', Auth.setPassword),
      value: Auth.password,
      errors: Auth.errors && Auth.errors.password
    })
  }
}
