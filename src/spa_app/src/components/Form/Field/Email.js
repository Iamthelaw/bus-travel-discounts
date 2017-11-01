const m = require('mithril')

const Auth = require('./../../../models/Auth')
const TextInput = require('./../TextInput')

module.exports = {
  view (vnode) {
    return m(TextInput, {
      label: 'Email',
      type: 'email',
      placeholder: 'love2travel@gmail.com',
      oninput: m.withAttr('value', Auth.setEmail),
      value: Auth.email,
      errors: Auth.errors && Auth.errors.email
    })
  }
}
