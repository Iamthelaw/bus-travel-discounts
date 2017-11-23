const m = require('mithril')

const Auth = require('./../../../models/Auth')
const TextInput = require('./../TextInput')

module.exports = {
  view () {
    return m(TextInput, {
      label: 'Username',
      type: 'text',
      placeholder: 'johndoe2',
      oninput: m.withAttr('value', Auth.setUsername),
      value: Auth.username,
      errors: Auth.errors && Auth.errors.username
    })
  }
}
