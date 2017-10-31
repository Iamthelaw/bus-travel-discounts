const m = require('mithril')
const TopNav = require('./Nav/Top')
const TabNav = require('./Nav/Tab')
const Hero = require('./Hero')

var Header = {
  view () {
    return [
      m(TopNav),
      m('header.hero.is-primary.is-medium', [
        m('section.hero-body.lead-image', [
          m(Hero, {
            title: 'Travel by bus',
            subtitle: 'Where will be your next destination?'
          })
        ]),
        m('section.hero-foot', [m(TabNav)])
      ])
    ]
  }
}

module.exports = Header
