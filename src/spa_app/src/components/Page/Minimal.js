const m = require('mithril')

const Footer = require('./../Footer')

module.exports = {
  view (vnode) {
    return [
      m('.top-border'),
      m('section.section.container', vnode.children),
      m(Footer)
    ]
  }
}
