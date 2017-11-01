const m = require('mithril')
const Button = require('./Button')

module.exports = {
  view (vnode) {
    return m('.field.is-grouped', [
      m(Button, {
        submit: true,
        primary: true,
        text: vnode.attrs.text,
        disabled: vnode.attrs.disabled
      }),
      m('a.button[href=/]', {oncreate: m.route.link}, 'Cancel')
    ])
  }
}
