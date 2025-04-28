const path = require('path');

module.exports = {
  entry: './src/index.js', // The main entry point for your application
  output: {
    filename: 'main.js', // The name of the bundled output file
    path: path.resolve(__dirname, 'dist'), // The output directory
  },
  mode: 'development', // Use 'development' mode for easier debugging
  devServer: {
    static: path.join(__dirname, 'public'), // Serve static files from the 'public' directory
    port: 8080, // The port to run the development server on
    open: true, // Automatically open the browser when the server starts
    historyApiFallback: true, // Ensures SPA routes fallback to 'index.html'
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/, // Match .js and .jsx files
        exclude: /node_modules/, // Exclude node_modules directory
        use: {
          loader: 'babel-loader', // Use Babel to transpile JSX and ES6+
        },
      },
      {
        test: /\.css$/, // Match .css files
        use: ['style-loader', 'css-loader'], // Use style-loader and css-loader to handle CSS
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx'], // Resolve .js and .jsx extensions
  },
};