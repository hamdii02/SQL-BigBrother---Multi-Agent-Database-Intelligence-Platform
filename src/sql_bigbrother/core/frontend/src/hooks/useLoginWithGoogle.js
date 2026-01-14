import axios from "axios";
import { useState } from "react";
import configDev from "../configs";

export default function useLoginWithGoogle() {
	const [loading, setLoading] = useState(false);
	const [error, setError] = useState(null);
 
	const loginWithGoogle = async (username, email, avatar, googleId) => {
		setLoading(true);

        const options = {
			url: configDev["BACKEND_URL"] + "/auth/signInWithGoogle",
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
            data: JSON.stringify({ username, email, avatar, googleId }),
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

	return { loginWithGoogle, loading, error };
}
