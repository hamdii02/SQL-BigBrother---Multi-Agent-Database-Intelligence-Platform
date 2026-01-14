"use strict";

class SuccessResponse {
	constructor({
		success = true,
		code = 200,
		message = "✔️  Success!",
		metadata = null,
		options = null,
	}) {
		this.success = success;
		this.code = code;
		this.message = message;
		this.metadata = metadata;
		this.options = options;
	}

	send = ({response, headers = {}, callback }) => {
		if(callback) callback(response);
		return response.status(this.code).json(this);
	};
}

module.exports = { SuccessResponse };
