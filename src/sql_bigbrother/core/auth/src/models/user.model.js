const { model, Schema, Types } = require("mongoose");

const userSchema = new Schema(
	{
		username: { type: String, required: true },
		email: { type: String, required: true },
		password: { type: String },
		avatar: { type: String, required: true },
		gender: { type: String, enum: ["male", "female"] },
        googleId: { type: String, unique: true }
	},
	{
		timestamps: true,
	}
);

module.exports = model('User', userSchema);