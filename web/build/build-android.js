require('./check-versions')()

process.env.NODE_ENV = 'production'

var fs = require("fs")
var ora = require('ora')
var rm = require('rimraf')
var path = require('path')
var chalk = require('chalk')
var webpack = require('webpack')
var config = require('../config')
var webpackConfig = require('./webpack.prod.conf')

var spinner = ora('building for production...')
spinner.start()

rm(path.join(config.build.assetsRoot, config.build.assetsSubDirectory), err => {
  if (err) throw err
  webpack(webpackConfig, function (err, stats) {
    spinner.stop()
    if (err) throw err
    process.stdout.write(stats.toString({
      colors: true,
      modules: false,
      children: false,
      chunks: false,
      chunkModules: false
    }) + '\n\n')
    console.log(chalk.cyan('  webpack Build complete.\n'))
    const execSync = require('child_process').execSync

    var apk_spinner = ora('Building Android APK file....')
    apk_spinner.start()
    fs.access("cordova/platforms/android", fs.constants.R_OK | fs.constants.W_OK, (error) => {
      if (error) {
        if (error.code === "ENOENT") {
          execSync('pwd; cd cordova; cordova platform add android;').toString()
        } else {
          return;
        }
      }
    });
    const result =  execSync('pwd; cd cordova; cordova build android --release;').toString()
    apk_spinner.stop()
    console.log(result)
    console.log(chalk.cyan('  APK Build complete.\n'))
  })
})
