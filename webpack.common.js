const webpack = require('webpack')
const path = require('path')
const autoprefixer = require('autoprefixer')
const CopyWebpackPlugin = require('copy-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

module.exports = {
  entry: {
    tempelhof: [
      './tempelhof/assets/scss/style.scss',
      './tempelhof/assets/js/app.js'
    ],
    vendor: [
      '@fortawesome/fontawesome-free/scss/fontawesome.scss',
      '@fortawesome/fontawesome-free/scss/brands.scss',
      '@fortawesome/fontawesome-free/scss/regular.scss',
      '@fortawesome/fontawesome-free/scss/solid.scss',
      'jquery'
    ]
  },
  output: {
    libraryTarget: 'this',
    library: '[name]',
    path: path.resolve('./tempelhof/static/'),
    publicPath: '/static/'
  },
  externals: {
    'django': 'django'
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules\/(?!(bootstrap)\/).*/,
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-env'].map(require.resolve),
          plugins: ['@babel/plugin-transform-runtime', '@babel/plugin-transform-modules-commonjs']
        }
      },
      {
        test: /\.s?css$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader
          },
          {
            loader: 'css-loader',
            options: {
              url: false
            },
          },
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                ident: 'postcss',
                plugins: [
                  require('autoprefixer')
                ]
              }
            }
          },
          {
            loader: 'sass-loader'
          }
        ]
      },
      {
        test: /(fonts|files)\/.*\.(svg|woff2?|ttf|eot|otf)(\?.*)?$/,
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
    fallback: { path: require.resolve('path-browserify') },
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
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery'
    }),
    new webpack.optimize.SplitChunksPlugin({
      name: 'vendor',
      filename: 'vendor.js'
    }),
    new MiniCssExtractPlugin({
      filename: '[name].css',
      chunkFilename: '[id].css'
    }),
    new CopyWebpackPlugin({
      patterns: [{
        from: './tempelhof/assets/images/**/*',
        to: 'images/[name].[ext]',
      }]
    })
  ]
}
