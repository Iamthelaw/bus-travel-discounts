const m = require('mithril')

module.exports = {
  view (vnode) {
    return m('.field', [
      m('.control', [
        m('label.checkbox', [
          m('input.checkbox', {
            name: vnode.attrs.name,
            type: 'checkbox'
          }),
          ' ',
          vnode.attrs.label
        ])
      ])
    ])
  }
}
