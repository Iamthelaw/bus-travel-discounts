const m = require('mithril')
const Logo = require('./../Logo')
const User = require('./User')
const Currency = require('./Currency')

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
          m('li.navbar-start', [
            m('.navbar-item', [m('input.input[type=text]', {placeholder: 'Riga'})]),
            m(Currency)
          ]),
          m('li.navbar-end', [
            m(User)
          ])
        ])
      ])
    ])
  }
}

module.exports = Top
