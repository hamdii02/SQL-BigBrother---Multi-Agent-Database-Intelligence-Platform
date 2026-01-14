const { AuthorizedError, BadRequestError } = require("./error.response");
const { verifyTokens } = require("../ultils");
const userModel = require("../models/user.model");
const KeyStoreService = require("../services/keystore.services");

module.exports.verifyAuth = async (req, res, next) => {
	const clientId = req.headers["x-client-id"]?.toString();
	if (!clientId) throw new BadRequestError("❌ ClientId Not Provided");

	const keyStore = await KeyStoreService.findByUser(clientId);
	if (!keyStore) throw new AuthorizedError("❌ Your're not sign in yet");

	const refreshToken = req.headers['x-rtoken-id"']?.toString();
	if (refreshToken) {
		const decode = verifyTokens(refreshToken, keyStore.privateKey);
		if (!decode || decode.userId !== clientId)
			throw new AuthorizedError("❌ Unauthorized Error");

		req.keyStore = keyStore;
		req.user = user;
		req.refreshToken = refreshToken;
		next();
	} else {
		const accessToken = req.cookies["accessToken"]?.toString();
		console.log(accessToken);
		if (!accessToken) throw new AuthorizedError("❌ No Token Provided");

		const decode = await verifyTokens(accessToken, keyStore.publicKey);
		if (!decode || decode.userId !== clientId)
			throw new AuthorizedError("❌ Unauthorized Error");

		const user = await userModel
			.findById(clientId)
			.select("-password")
			.lean();
		if (!user) throw new AuthorizedError("❌ User not existed");

		req.user = user;
		next();
	}
};
