const m = require('mithril')

module.exports = {
  view (vnode) {
    return m('thead', [
      m('tr', [vnode.attrs.columns.map((column) => {
        return m('th', column)
      })])
    ])
  }
}
