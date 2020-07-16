module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? './pro'
    : './dev',
  outputDir: process.env.NODE_ENV === 'production'
    ? './dist/pro'
    : './dist/dev',
};
