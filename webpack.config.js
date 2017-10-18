var ExtractTextPlugin = require('extract-text-webpack-plugin')
var webpack = require('webpack')
var path = require('path')
var autoprefixer = require('autoprefixer')

module.exports = {
  entry: {
    tempelhof: [
      './tempelhof/assets/scss/style.scss',
      './tempelhof/assets/js/app.js'
    ],
    vendor: [
      'font-awesome/scss/font-awesome.scss',
      'jquery',
    ]
  },
  devtool: 'eval',
  output: {
    libraryTarget: 'var',
    library: 'tempelhof',
    path: path.resolve('./tempelhof/static/'),
    publicPath: '/static/',
    filename: '[name].js'
  },
  externals: {
    'django': 'django'
  },
  module: {
    noParse: /\.min\.js$/,
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules\/(?!adhocracy4|bootstrap)/,  // exclude all dependencies but adhocracy4 and bootstrap
        loader: 'babel-loader',
        options: {
          presets: ['babel-preset-es2015', 'babel-preset-react'].map(require.resolve)
        }
      },
      {
        test: /\.s?css$/,
        use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: [
            'css-loader',
            {
              loader: 'postcss-loader',
              options: {
                ident: 'postcss',
                plugins: (loader) => [
                  autoprefixer({
                    browsers: ['last 3 versions', 'ie >= 10']
                  })
                ]
              }
            },
            'sass-loader'
          ]
        })
      },
      {
        test: /fonts\/.*\.(svg|woff2?|ttf|eot)(\?.*)?$/,
        loader: 'file-loader',
        options: {
          name: 'fonts/[name].[ext]'
        }
      },
      {
        test: /\.svg$|\.png$/,
        loader: 'file-loader',
        options: {
          name: 'images/[name].[ext]'
        }
      }
    ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx', '.scss', '.css'],
    alias: {
      'jquery$': 'jquery/dist/jquery.min.js'
    },
    // when using `npm link`, dependencies are resolved against the linked
    // folder by default. This may result in dependencies being included twice.
    // Setting `resolve.root` forces webpack to resolve all dependencies
    // against the local directory.
    modules: [
      path.resolve('./node_modules'),
      path.resolve('./apps/'),
    ]
  },
  plugins: [
    new webpack.IgnorePlugin(/^\.\/locale$/, /moment$/),
    new webpack.optimize.CommonsChunkPlugin({
      name: 'vendor',
      filename: 'vendor.js'
    }),
    new ExtractTextPlugin({filename: '[name].css'})
  ]
}
