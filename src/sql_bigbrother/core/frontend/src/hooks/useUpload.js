import axios from "axios";
import { useState } from "react";
import configs from "../configs";
import { useAuthContext } from "../contexts/AuthProvider";

export default function useUpload() {
	const [loading, setLoading] = useState(false);
	const [error, setError] = useState(null);
	const { showLoading, setShowLoading } = useAuthContext();

	const upload = async (file) => {
		setLoading(true);
		setShowLoading(true);
        const formData = new FormData();
		formData.append("file", file);

        const options = {
			url: configs["CREWAI_URL"] + "/init-chat",
			method: "POST",
			headers: {
				"Content-Type": "multipart/form-data",
			},
			data: formData,
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
				setShowLoading(false);
				setError(null);
			});
	};

	return { upload, loading, error };
}
