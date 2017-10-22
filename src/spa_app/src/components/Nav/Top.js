const m = require('mithril')
const Modal = require('./../Modal')

const Top = {
  visible: false,
  toggleMenu () { Top.visible = !Top.visible },
  view () {
    return m('nav.navbar.is-primary', [
      m('ul.container', [
        m('li.navbar-brand', [
          // m('a.navbar-item', {href: '#!/app'}, 'TBB'),
          m('a.navbar-item', {href: '#!/app'}, [m('img', {src: '/static/spa_app/logo.svg', width: 50})]),
          // m('img', {src: '/static/spa_app/logo.svg'}),
          m('span.navbar-burger.burger', {
            onclick: Top.toggleMenu
          }, [m('span'), m('span'), m('span')])
        ]),
        m(`ul.navbar-menu${Top.visible ? 'is-active' : ''}`, [
          m('li.navbar-end', [
            m('a.navbar-item', {
              href: '#',
              onclick: Modal.show
            }, 'Log In')
          ])
        ])
      ])
    ])
  }
}

module.exports = Top
