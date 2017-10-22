const m = require('mithril')

module.exports = {
  view () {
    return m('nav.tabs.is-boxed.is-fullwidth', [
      m('ul.container', [
        m('li.is-active', [m('a', {href: '#'}, 'Best Deals')]),
        m('li', [m('a', {href: '#'}, 'By Country')])
      ])
    ])
  }
}
