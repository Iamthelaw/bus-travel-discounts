const m = require('mithril')

module.exports = {
  view (vnode) {
    return m('tbody', [
      vnode.attrs.items.map((row) => {
        row.link = m('a', {href: row.link}, '→')
        let fromCity = [
          m(`span.flag-icon.flag-icon-${row.from_country_code.toLowerCase()}`),
          m('span.city-name', row.from_city)
        ]
        let toCity = [
          m(`span.flag-icon.flag-icon-${row.to_country_code.toLowerCase()}`),
          m('span.city-name', row.to_city)
        ]
        return m('tr', [
          m('td', fromCity),
          m('td', toCity),
          m('td', [row.original_price]),
          m('td', [row.original_currency]),
          m('td', [row.link])
        ])
      })
    ])
  }
}
