const Currency = {
  getCodes () {
    // mock
    Currency.codes = [
      'RUB',
      'USD',
      'EUR'
    ]
  },
  setCode (code) { Currency.current = code || '' },
  codes: [],
  current: ''
}

module.exports = Currency
