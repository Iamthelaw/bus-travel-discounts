const m = require('mithril')

const LoginForm = require('./../components/LoginForm')
const Page = require('./../components/Page/Minimal')

module.exports = {
  view () {
    return m(Page, [
      m('h1.title', 'Login'),
      m('h2.subtitle', [
        'Don\'t have an account? ',
        m('a[href=/register]', {oncreate: m.route.link}, 'Register'), '.'
      ]),
      m('hr'),
      m(LoginForm)
    ])
  }
}
