const m = require('mithril')

module.exports = {
  view (vnode) {
    let errors = vnode.attrs.errors || []
    return m('.field', [
      m('label.label', vnode.attrs.label),
      m('.control', [
        m('input.input',
          {
            type: vnode.attrs.type,
            name: vnode.attrs.label.toLowerCase(),
            placeholder: vnode.attrs.placeholder || vnode.attrs.label,
            oninput: vnode.attrs.oninput
          })
      ]),
      errors.map(
        (error) => m('p.help.is-danger', error)
      )
    ])
  }
}
