const express = require('express');
const router = express.Router();
const catchAsync = require('../helpers/async.catch');
const ChatController = require('../controllers/chat.controller');
const { verifyAuth } = require('../middlewares/auth.verify');

router.use(catchAsync(verifyAuth));

router.post('/create', catchAsync(ChatController.createNewChat));
router.post('/newMessage', catchAsync(ChatController.addMessage));
router.put('/update', catchAsync(ChatController.updateSchema));
router.put('/rename', catchAsync(ChatController.renameChat));
router.delete('/delete', catchAsync(ChatController.deleteChat));
router.get('/history-chats', catchAsync(ChatController.loadHistoryChat));
router.get('/history-messages/:chatId', catchAsync(ChatController.loadHistoryMessages));

module.exports = router;