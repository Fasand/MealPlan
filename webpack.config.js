module.exports = [
  {
    entry: "./mealplan/frontend/src/index.js",
    output: {
      path: __dirname,
      filename: "./mealplan/frontend/static/frontend/main.js",
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader",
          },
        },
        {
          test: /\.less$/,
          use: [
            {
              loader: "style-loader",
            },
            {
              loader: "css-loader",
              options: {
                importLoaders: 1,
              },
            },
            {
              loader: "less-loader",
              options: {
                javascriptEnabled: true,
              },
            },
          ],
        },
      ],
    },
  },
];
