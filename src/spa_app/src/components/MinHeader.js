const m = require('mithril')
const Modal = require('./Modal')
const LoginForm = require('./LoginForm')
const TopNav = require('./Nav/Top')

var MinHeader = {
  view () {
    return [
      m(Modal, {title: 'Login'}, [m(LoginForm)]),
      m('header', [
        m(TopNav)
      ])
    ]
  }
}

module.exports = MinHeader
