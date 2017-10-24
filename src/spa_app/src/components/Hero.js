const m = require('mithril')

module.exports = {
  view (vnode) {
    return m('.container.has-text-centered', [
      m('h1.title', vnode.attrs.title),
      m('h2.subtitle', vnode.attrs.subtitle),
      m('a.button.is-primary[href=/register]', {oncreate: m.route.link}, 'Join the community'),
      m('small', [
        m('br'),
        'Have an account? ',
        m('a.has-text-weight-bold[href=/login]', {oncreate: m.route.link}, 'Log in'),
        '.',
        ]
      )
    ])
  }
}
