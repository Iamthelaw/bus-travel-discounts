const m = require('mithril')

const DealList = require('./../components/DealList')
const Page = require('./../components/Page')

module.exports = {
  view () {
    return m(Page, [
      m(DealList)
    ])
  }
}
