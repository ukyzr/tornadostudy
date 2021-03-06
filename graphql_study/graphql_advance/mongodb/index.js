// mongodb/index.js
// import mongoose from 'mongoose'
// import config from '../config'

const mongoose = require('mongoose');
const config = require('../config');
require('./schema/list')

const database = () => {
  mongoose.set('debug', true)

  mongoose.connect(config.dbPath)

  mongoose.connection.on('disconnected', () => {
    mongoose.connect(config.dbPath)
  })
  mongoose.connection.on('error', err => {
    console.error(err)
  })

  mongoose.connection.on('open', async () => {
    console.log('Connected to MongoDB ', config.dbPath)
  })
}

module.exports = database
