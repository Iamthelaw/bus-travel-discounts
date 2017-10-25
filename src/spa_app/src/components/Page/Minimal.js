const m = require('mithril')

const Logo = require('./../Logo')
const Footer = require('./../Footer')

module.exports = {
  view (vnode) {
    return [
      m('.top-border'),
      m(Logo, {center: true}),
      m('section.section.container', vnode.children),
      m(Footer)
    ]
  }
}
