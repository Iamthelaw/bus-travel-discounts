const path = require('path')

module.exports = {
  entry: './client/main.js',
  output: {
    path: path.resolve(__dirname, './server/bus_travel/static'),
    filename: 'app.js'
  },
  module: {
    loaders: [{
      test: /\.js$/,
      exclude: /node_modules/,
      loader: 'babel-loader'
    }]
  }
}
