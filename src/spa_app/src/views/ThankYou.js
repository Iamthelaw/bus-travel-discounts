const m = require('mithril')

const LoginForm = require('./../components/LoginForm')
const Page = require('./../components/Page/Minimal')

module.exports = {
  view () {
    return m(Page, [
      m('h1.title', 'Hooray! 👏'),
      m('h2.subtitle', 'Now you part of the team!'),
      m('p', 'Log in now to have full access to your account'),
      m('hr'),
      m(LoginForm)
    ])
  }
}
