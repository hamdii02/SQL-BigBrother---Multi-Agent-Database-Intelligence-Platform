const express = require('express');
const router = express.Router();
const catchAsync = require('../helpers/async.catch');
const AuthController = require('../controllers/auth.controller');
const { verifyAuth } = require('../middlewares/auth.verify');


router.post('/signUp', catchAsync(AuthController.signUp));
router.post('/signIn', catchAsync(AuthController.signIn));
router.post('/signInWithGoogle', catchAsync(AuthController.signInWithGoogle));

router.use(catchAsync(verifyAuth));
router.post('/logOut', catchAsync(AuthController.logOut));

module.exports = router;