const m = require('mithril')

const RegisterForm = require('./../components/RegisterForm')
const Page = require('./../components/Page/Minimal')

module.exports = {
  view () {
    return m(Page, [
      m('h1.title', 'Register'),
      m('h2.subtitle', [
        'Already have an account? ',
        m('a[href=/login]', {oncreate: m.route.link}, 'Log in'), '.'
      ]),
      m('hr'),
      m(RegisterForm)
    ])
  }
}
