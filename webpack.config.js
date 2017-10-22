const path = require('path')

module.exports = {
  entry: './src/spa_app/src/main.js',
  output: {
    path: path.resolve(__dirname, './src/spa_app/static/spa_app'),
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
