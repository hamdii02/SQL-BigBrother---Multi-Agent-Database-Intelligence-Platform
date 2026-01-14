const JWT = require("jsonwebtoken");
const crypto = require("crypto");
const _ = require("lodash");

module.exports.filterData = ({ object = {}, fields = [] }) => {
	return _.pick(object, fields);
};

module.exports.generateKeys = () => {
	const privateKey = crypto.randomBytes(64).toString("hex");
	const publicKey = crypto.randomBytes(64).toString("hex");

	return { privateKey, publicKey };
};

module.exports.generateTokens = async (payload, publicKey, privateKey) => {
	const accessToken = await JWT.sign(payload, publicKey, {
		expiresIn: "2 days",
	});

	const refreshToken = await JWT.sign(payload, privateKey, {
		expiresIn: "7 days",
	});

	return { accessToken, refreshToken };
};

module.exports.verifyTokens = async (token, secetKey) => {
	return await JWT.verify(token, secetKey, (err, decode) => {
		if (err) return null;
		return decode;
	});
};
