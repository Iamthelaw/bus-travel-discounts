const m = require('mithril')

const Header = require('./../Header')
const Footer = require('./../Footer')

module.exports = {
  view (vnode) {
    return [
      m(Header),
      m('section.section.container', vnode.children),
      m(Footer)
    ]
  }
}
