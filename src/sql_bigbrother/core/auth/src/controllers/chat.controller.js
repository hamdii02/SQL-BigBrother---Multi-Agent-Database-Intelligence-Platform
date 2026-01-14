const { SuccessResponse } = require("../middlewares/success.response");
const ChatService = require("../services/chat.services");

class ChatController {
	/************************************* CREATE NEW CHAT **********************************************
	 * @url     /api/v1/chat/create
	 * @method  POST
	 * @desc    Create a new chat
	 * @param   {String} userId
	 * @return  {JSON} newChat
	 */
	static async createNewChat(req, res, next) {
		const userId = req.user._id;
		const metadata = await ChatService.createNewChat({ userId });

		return new SuccessResponse({
			code: 201,
			message: `✔️ Created new Chat`,
			metadata,
		}).send({ response: res });
	}

	/************************************* UPDATE SCHEMA **********************************************
	 * @url     /api/v1/chat/update
	 * @method  PUT
	 * @desc    Update new schema
	 * @param   {String} chatId
	 * @param   {String} schema
	 * @param   {String} userId
	 * @return  {JSON} updatedChat
	 */
	static async updateSchema(req, res, next) {
		const userId = req.user._id;
		const { chatId, schema, title, recommends } = req.body;
		const metadata = await ChatService.updateSchema({
			chatId,
			schema,
			title,
			recommends,
			userId,
		});

		return new SuccessResponse({
			code: 200,
			message: `✔️ Updated new Schema`,
			metadata,
		}).send({ response: res });
	}

	/************************************* RENAME CHAT **********************************************
	 * @url     /api/v1/chat/rename
	 * @method  PUT
	 * @desc    Rename a chat
	 * @param   {String} chatId
	 * @param   {String} title
	 * @param   {String} userId
	 * @return  {JSON} updatedChat
	 */
	static async renameChat(req, res, next) {
		const userId = req.user._id;
		const { chatId, title } = req.body;
		const metadata = await ChatService.renameChat({
			chatId,
			title,
			userId,
		});

		return new SuccessResponse({
			code: 200,
			message: `✔️ Renamed chat`,
			metadata,
		}).send({ response: res });
	}

	/************************************* ADD NEW MESSAGE **********************************************
	 * @url     /api/v1/chat/newMessage
	 * @method  POST
	 * @desc    Add new message to Chat
	 * @param   {String} chatId
	 * @param   {String} type
	 * @param   {String} body
	 * @param   {Array} data
	 * @param   {String} userId
	 * @return  {JSON} newMessage
	 */
	static async addMessage(req, res, next) {
		const userId = req.user._id;
		const { chatId, type, body, data } = req.body;

		return new SuccessResponse({
			code: 201,
			message: `✔️ Added new message`,
			metadata: await ChatService.addMessage({
				chatId,
				type,
				body,
				data,
				userId,
			}),
		}).send({ response: res });
	}

	/************************************* DELETE CHAT **********************************************
	 * @url     /api/v1/chat/delete
	 * @method  DELETE
	 * @desc    Delete a chat
	 * @param   {String} chatId
	 * @param   {String} userId
	 * @return  {JSON}
	 */
	static async deleteChat(req, res, next) {
		const userId = req.user._id;
		const { chatId } = req.body;

		return new SuccessResponse({
			code: 200,
			message: `✔️ Deleted chat`,
			metadata: await ChatService.deleteChat({ chatId, userId }),
		}).send({ response: res });
	}

	/************************************* LOAD HISTORY CHATS **********************************************
	 * @url     /api/v1/chat/history-chats
	 * @method  GET
	 * @desc    Get history chats
	 * @return  {JSON} historyChats
	 */
	static async loadHistoryChat(req, res, next) {
		const userId = req.user._id;

		return new SuccessResponse({
			code: 200,
			message: `✔️ Loaded history chats`,
			metadata: await ChatService.loadHistoryChat({ userId }),
		}).send({ response: res });
	}

	/************************************* LOAD HISTORY MESSAGES **********************************************
	 * @url     /api/v1/chat/history-message
	 * @method  GET
	 * @desc    Get history messages
	 * @param   {String} chatId
	 * @return  {JSON} historyMessages
	 */
	static async loadHistoryMessages(req, res, next) {
		const userId = req.user._id;
		const { chatId } = req.params;

		return new SuccessResponse({
			code: 200,
			message: `✔️ Loaded history messages`,
			metadata: await ChatService.loadHistoryMessages({ chatId, userId }),
		}).send({ response: res });
	}
}

module.exports = ChatController;
