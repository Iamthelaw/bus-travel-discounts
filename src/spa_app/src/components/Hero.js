const m = require('mithril')

module.exports = {
  view (vnode) {
    return m('.container.has-text-centered', [
      m('h1.title', vnode.attrs.title),
      m('h2.subtitle', vnode.attrs.subtitle)
    ])
  }
}
