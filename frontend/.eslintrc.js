module.exports = {
  root: true,
  parserOptions: {
    "parser": "babel-eslint",
  },
  env: {
    browser: true,
    node: true
  },
  extends: ['standard',
    "plugin:vue/recommended",
  ],
  // required to lint *.vue files
  plugins: [
    "vue"
  ],
  // add your custom rules here
  rules: {},
  globals: {}
}