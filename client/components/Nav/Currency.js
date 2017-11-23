const m = require('mithril')
const Currency = require('./../../models/Currency')

const CurrencySelector = {
  oninit () {
    Currency.getCodes()
    Currency.setCode(Currency.codes[0])
  },

  view () {
    return m('.navbar-item.has-dropdown.is-hoverable', [
      m('a.navbar-link', Currency.current),
      m('.navbar-dropdown', [
        Currency.codes
        .filter((code) => code !== Currency.current)
        .map((code) => m('a.navbar-item', { onclick: () => Currency.setCode(code) }, code))
      ])
    ])
  }
}

module.exports = CurrencySelector
