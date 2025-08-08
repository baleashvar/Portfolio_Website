const mongoose = require('mongoose');

const skinSchema = new mongoose.Schema({
  name: String,
  image: String,
  price: Number,
  sellerId: String,
});

module.exports = mongoose.model('Skin', skinSchema);
