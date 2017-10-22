const City = {
  list: [],
  loadList () {
    // mock request
    City.list = [
      {name: 'Helsinki'},
      {name: 'Paris'}
    ]
  }
}

module.exports = City
