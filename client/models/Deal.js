const m = require('mithril')

var Deal = {
  list: [],
  loadData () {
    // mock
    Deal.list = [
      [
        '10/10/2017',
        'Helsinki - Riga',
        2000,
        'RUB'
      ],
      [
        '12/10/2017',
        'Berlin - Paris',
        1500,
        'RUB'
      ]
    ]
  },
  loadTop10 () {
    m.request({url: '/api/v1/discount/top/'})
    .then((data) => {
      Deal.list = data
    })
    .catch((error) => {
      console.error(error)
    })
  }
}

module.exports = Deal
