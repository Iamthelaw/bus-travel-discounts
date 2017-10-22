const m = require('mithril')

const MinHeader = require('./MinHeader')
const Footer = require('./Footer')

module.exports = {
  view (vnode) {
    return [
      m(MinHeader),
      m('section.section.container', vnode.children),
      m(Footer)
    ]
  }
}
