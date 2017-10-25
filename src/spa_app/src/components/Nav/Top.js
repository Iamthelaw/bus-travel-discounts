const m = require('mithril')

const Top = {
  visible: false,
  toggleMenu () { Top.visible = !Top.visible },
  view () {
    return m('nav.navbar.is-primary', [
      m('ul.container', [
        m('li.navbar-brand', [
          m('a.navbar-item[href=/]', {oncreate: m.route.link}, [
            m('img', {src: '/static/spa_app/logo.svg', width: 50})
          ]),
          m('span.navbar-burger.burger', {
            onclick: Top.toggleMenu
          }, [m('span'), m('span'), m('span')])
        ]),
        m(`ul.navbar-menu${Top.visible ? 'is-active' : ''}`, [
          m('li.navbar-end', [
            m('a.navbar-item[href=/]', {oncreate: m.route.link}, 'Best Deals'),
            m('a.navbar-item[href=/]', {oncreate: m.route.link}, 'By Country'),
          ])
        ])
      ])
    ])
  }
}

module.exports = Top
