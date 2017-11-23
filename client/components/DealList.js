const m = require('mithril')

const Deal = require('./../models/Deal')

const TableBody = require('./Table/Body')
const TableHead = require('./Table/Head')

module.exports = {
  oninit: Deal.loadTop10,
  view () {
    return m('table.table.is-fullwidth', [
      m(TableHead, {columns: [
        'Dates',
        'Destination',
        'Price',
        'Currency',
        '',
      ]}),
      m(TableBody, {items: Deal.list})
    ])
  }
}
