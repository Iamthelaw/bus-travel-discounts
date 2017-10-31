const m = require('mithril')
const Auth = require('./../models/Auth')
const TopNav = require('./Nav/Top')
const TabNav = require('./Nav/Tab')
const Hero = require('./Hero')

const heroParams = {
  title: 'Travel by bus',
  subtitle: 'Where will be your next destination?'
}

const Header = {
  view () {
    return [
      m(TopNav),
      m('header.hero.is-primary.is-medium', [
        !Auth.user.loggedIn && m('section.hero-body.lead-image', [m(Hero, heroParams)]),
        m('section.hero-foot', [m(TabNav)])
      ])
    ]
  }
}

module.exports = Header
