const m = require('mithril')
const LoginForm = require('./LoginForm')
const TopNav = require('./Nav/Top')
const TabNav = require('./Nav/Tab')
const Hero = require('./Hero')

var Header = {
  view () {
    return [
      m('header.hero.is-medium.is-primary.is-bold', [
        m('section.hero-head', [m(TopNav)]),
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
