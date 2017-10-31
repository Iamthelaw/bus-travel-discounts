const m = require('mithril')
const {capitalize} = require('./../../utils')
const Auth = require('./../../models/Auth')

module.exports = {
  oninit () { Auth.check() },
  view () {
    if (Auth.user.loggedIn) {
      return [
        m('a.navbar-item[href=/profile]', {oncreate: m.route.link}, [
          m('img.icon[src=/static/spa_app/icon/user.svg]')
        ]),
        m('a.navbar-item', {onclick: Auth.logout}, [
          m('img.icon[src=/static/spa_app/icon/logout.svg]')
        ])
      ]
    } else {
      return [
        m('a.navbar-item[href=/login]', {oncreate: m.route.link}, 'Log in'),
        m('a.navbar-item.button[href=/register]', {oncreate: m.route.link}, 'Join')
      ]
    }
  }
}
