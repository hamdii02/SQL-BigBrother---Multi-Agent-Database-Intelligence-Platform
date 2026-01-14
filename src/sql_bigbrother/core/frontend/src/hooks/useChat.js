import axios from "axios";
import { useState } from "react";
import configs from "../configs";
import { useAuthContext } from "../contexts/AuthProvider";

export default function useChat() {
	const [loading, setLoading] = useState(false);
	const [error, setError] = useState(null);
	const { user } = useAuthContext();

	const createNewChat = async () => {
		setLoading(true);

		const options = {
			url: configs["BACKEND_URL"] + "/chat/create",
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"x-client-id": user._id,
			},
			withCredentials: true,
		};

		return await axios
			.request(options)
			.then((response) => response.data)
			.catch((err) => {
				console.log(err);
				setError(err?.response?.data?.message || "Error occured!");
				return null;
			})
			.finally(() => {
				setLoading(false);
				setError(null);
			});
	};

	const addNewMessage = async (chatId, type, body, data) => {
		setLoading(true);

		const options = {
			url: configs["BACKEND_URL"] + "/chat/newMessage",
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"x-client-id": user._id,
			},
			data: JSON.stringify({ chatId, type, body, data }),
			withCredentials: true,
		};

		return await axios
			.request(options)
			.then((response) => response.data)
			.catch((err) => {
				console.log(err);
				setError(err?.response?.data?.message || "Error occured!");
				return null;
			})
			.finally(() => {
				setLoading(false);
				setError(null);
			});
	};

	const updateSchema = async (chatId, schema, title, recommends) => {
		setLoading(true);

		const options = {
			url: configs["BACKEND_URL"] + "/chat/update",
			method: "PUT",
			headers: {
				"Content-Type": "application/json",
				"x-client-id": user._id,
			},
			data: JSON.stringify({ chatId, schema, title, recommends }),
			withCredentials: true,
		};

		return await axios
			.request(options)
			.then((response) => response.data)
			.catch((err) => {
				console.log(err);
				setError(err?.response?.data?.message || "Error occured!");
				return null;
			})
			.finally(() => {
				setLoading(false);
				setError(null);
			});
	};

	const loadHistoryChats = async () => {
		setLoading(true);

		const options = {
			url: configs["BACKEND_URL"] + "/chat/history-chats",
			method: "GET",
			headers: {
				"Content-Type": "application/json",
				"x-client-id": user._id,
			},
			withCredentials: true,
		};

		return await axios
			.request(options)
			.then((response) => response.data)
			.catch((err) => {
				console.log(err);
				setError(err?.response?.data?.message || "Error occured!");
				return null;
			})
			.finally(() => {
				setLoading(false);
				setError(null);
			});
	};

	const loadHistoryMessages = async (chatId) => {
		setLoading(true);

		const options = {
			url: configs["BACKEND_URL"] + `/chat/history-messages/${chatId}`,
			method: "GET",
			headers: {
				"Content-Type": "application/json",
				"x-client-id": user._id,
			},
			withCredentials: true,
		};

		return await axios
			.request(options)
			.then((response) => response.data)
			.catch((err) => {
				console.log(err);
				setError(err?.response?.data?.message || "Error occured!");
				return null;
			})
			.finally(() => {
				setLoading(false);
				setError(null);
			});
	};

	const deleteChat = async (chatId) => {
		setLoading(true);

		const options = {
			url: configs["BACKEND_URL"] + `/chat/delete`,
			method: "DELETE",
			headers: {
				"Content-Type": "application/json",
				"x-client-id": user._id,
			},
			data: JSON.stringify({ chatId }),
			withCredentials: true,
		};

		return await axios
			.request(options)
			.then((response) => response.data)
			.catch((err) => {
				console.log(err);
				setError(err?.response?.data?.message || "Error occured!");
				return null;
			})
			.finally(() => {
				setLoading(false);
				setError(null);
			});
	};

	return {
		createNewChat,
		addNewMessage,
		deleteChat,
		updateSchema,
		loadHistoryChats,
		loadHistoryMessages,
		loading,
		error,
	};
}
