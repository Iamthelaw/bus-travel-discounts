const m = require('mithril')

module.exports = {
  view (vnode) {
    return m(
      'a[href=/]',
      {oncreate: m.route.link, class: vnode.attrs.class}, [
        m(
          `img.logo${vnode.attrs.center ? '.center' : ''}`,
          {src: '/static/logo.svg'}
        )
      ]
    )
  }
}
