const m = require('mithril')
const Logo = require('./../Logo')

const Top = {
  visible: false,
  toggleMenu () { Top.visible = !Top.visible },
  view () {
    return m('nav.navbar.is-primary', [
      m('ul.container', [
        m('li.navbar-brand', [
          m(Logo, {class: 'navbar-item'}),
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
