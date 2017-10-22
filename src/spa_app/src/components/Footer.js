const m = require('mithril')

module.exports = {
  view () {
    const heart = m('span.heart', '♥️')
    const siteAuthor = m('a', {
      href: 'https://github.com/iamthelaw',
      title: 'Github page'
    }, 'iamthelaw')
    const iconAuthor = m('a', {
      href: 'http://www.freepik.com',
      title: 'Freepick'
    }, 'Freepik')
    const iconSite = m('a', {
      href: 'https://www.flaticon.com',
      title: 'Flaticon'
    }, 'www.flaticon.com')
    const license = m('a', {
      href: 'http://creativecommons.org/licenses/by/3.0/',
      title: 'Creative Commons BY 3.0',
      target: '_blank'
    }, 'CC 3.0 BY')
    const mithril = m('a', {
      href: 'https://mithril.js.org',
      title: 'Frontend framework'
    }, 'Mithril')
    const django = m('a', {
      href: 'https://www.djangoproject.com',
      title: 'Server framework'
    }, 'Django')
    const bulma = m('a', {
      href: 'https://bulma.io',
      title: 'Css framework'
    }, 'Bulma')
    return m('footer.footer', [
      m('.container.content.has-text-centered', [
        m('p', ['Created with ', heart, ' by ', siteAuthor]),
        m('p', [
          'Thank you, creators of amazing frameworks ',
          django, ', ', mithril, ' and ', bulma, m('br'),
          'Icons made by ', iconAuthor,
          ' from ', iconSite, ' is licensed by ', license
        ])
      ])
    ])
  }
}
