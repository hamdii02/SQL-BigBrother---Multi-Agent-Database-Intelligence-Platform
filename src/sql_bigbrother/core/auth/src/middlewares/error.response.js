"use strict";

const StatusCode = {
	BAD_REQUEST: 400,
	UNAUTHORIZED: 401,
	FORBIDDEN: 403,
	NOT_FOUND: 404,
	METHOD_NOT_ALLOWED: 405,
	REQUEST_TIMEOUT: 408,
	CONFLICT: 409,
	INTERNAL_SERVER: 500,
};

const StatusMessage = {
	BAD_REQUEST: `Bad request error`,
	UNAUTHORIZED: `Unauthorized error`,
	FORBIDDEN: `Forbidden error`,
	NOT_FOUND: `File not found error`,
	METHOD_NOT_ALLOWED: `Method not allowed error`,
	REQUEST_TIMEOUT: `Request timeout error`,
	CONFLICT: `Conflict error`,
	INTERNAL_SERVER: `Internal Server error`,
};

class ErrorResponse extends Error {
	constructor(message, code) {
		super(message);
		this.code = code;
	}
}

class BadRequestError extends ErrorResponse {
	constructor(
		message = StatusMessage.BAD_REQUEST,
		code = StatusCode.BAD_REQUEST
	) {
		super(message, code);
	}
}

class AuthorizedError extends ErrorResponse {
	constructor(
		message = StatusMessage.UNAUTHORIZED,
		code = StatusCode.UNAUTHORIZED
	) {
		super(message, code);
	}
}

class ForbiddenError extends ErrorResponse {
	constructor(
		message = StatusMessage.FORBIDDEN,
		code = StatusCode.FORBIDDEN
	) {
		super(message, code);
	}
}

class FileNotFoundError extends ErrorResponse {
	constructor(
		message = StatusMessage.NOT_FOUND,
		code = StatusCode.NOT_FOUND
	) {
		super(message, code);
	}
}

class MethodNotAllowedError extends ErrorResponse {
	constructor(
		message = StatusMessage.METHOD_NOT_ALLOWED,
		code = StatusCode.METHOD_NOT_ALLOWED
	) {
		super(message, code);
	}
}

class RequestTimeoutError extends ErrorResponse {
	constructor(
		message = StatusMessage.REQUEST_TIMEOUT,
		code = StatusCode.REQUEST_TIMEOUT
	) {
		super(message, code);
	}
}

class ConflictError extends ErrorResponse {
	constructor(message = StatusMessage.CONFLICT, code = StatusCode.CONFLICT) {
		super(message, code);
	}
}

class InternalServerError extends ErrorResponse {
	constructor(
		message = StatusMessage.INTERNAL_SERVER,
		code = StatusCode.INTERNAL_SERVER
	) {
		super(message, code);
	}
}

module.exports = {
	InternalServerError,
	BadRequestError,
	AuthorizedError,
	ForbiddenError,
	FileNotFoundError,
	MethodNotAllowedError,
	RequestTimeoutError,
	ConflictError,
};
