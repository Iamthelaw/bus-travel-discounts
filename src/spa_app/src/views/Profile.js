const m = require('mithril')

const City = require('./../models/City')
const Checkbox = require('./../components/Form/Checkbox')
const Page = require('./../components/Page/Minimal')

module.exports = {
  oninit: City.loadList,
  view () {
    return m(
      Page, [
        m('h1.title', 'User Profile'),
        City.list.map((city) => m(Checkbox, {label: city.name}))
      ]
    )
  }
}
