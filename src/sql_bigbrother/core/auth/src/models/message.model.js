const { model, Schema, Types } = require("mongoose");

const messageSchema = new Schema(
	{
		type: { type: String, enum: ['question', 'response'], default: 'question' },
		chat: { type: Types.ObjectId, ref: "Chat", required: true },
		body: { type: String },
		data: { type: Schema.Types.Mixed }
	},
	{
		timestamps: true,
	}
);

module.exports = model("Message", messageSchema);
