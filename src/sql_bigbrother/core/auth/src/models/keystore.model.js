const { model, Schema, Types } = require("mongoose");

const keyStoreSchema = new Schema(
	{
		user: { type: Types.ObjectId, ref: "User", required: true },
		publicKey: { type: String, required: true },
		privateKey: { type: String, required: true },
		refreshTokensUsed: { type: Array, default: [] },
		refreshToken: { type: String, required: true },
	},
	{
		timestamps: true,
	}
);

module.exports = model("keyStoreSchema", keyStoreSchema);
