const m = require('mithril')

module.exports = {
  view (vnode) {
    let primary = vnode.attrs.primary
    let attrs = {
      disabled: vnode.attrs.disabled,
      onclick: vnode.attrs.onclick
    }
    if (vnode.attrs.submit) { attrs.type = 'submit' }
    return m('.control', [
      m(
                `button.button${primary ? '.is-primary' : ''}`,
                attrs, vnode.attrs.text
            )
    ])
  }
}
