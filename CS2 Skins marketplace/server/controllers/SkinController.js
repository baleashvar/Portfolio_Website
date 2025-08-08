const express = require('express');
const router = express.Router();
const Skin = require('../models/Skin');

router.get('/', async (req, res) => {
  const skins = await Skin.find().exec();
  return res.json(skins);
});

// ... Add more routes for CRUD operations
