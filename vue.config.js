const path = require('path');

function resolveSrc(_path) {
  return path.join(__dirname, _path);
}
module.exports = {
  publicPath: '/HappyClick/',
  lintOnSave: true,
  configureWebpack: {
    // Set up all the aliases we use in our app.
    resolve: {
      alias: {
        assets: resolveSrc('src/assets')
      }
    }
  },
  css: {
    // Enable CSS source maps.
    sourceMap: process.env.NODE_ENV !== 'production'
  }
};