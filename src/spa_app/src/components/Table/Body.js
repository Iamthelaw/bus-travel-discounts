const m = require('mithril')

module.exports = {
  view (vnode) {
    return m('tbody', [
      vnode.attrs.items.map((row) => {
        return m('tr', row.map((cell) => m('td', cell)))
      })
    ])
  }
}
