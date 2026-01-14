import React, { useContext, useEffect, useState } from "react";
import { LuAtSign, LuKey } from "react-icons/lu";
import GoogleSVG from "../components/SVG/GoogleSVG";
import { Link, useNavigate } from "react-router-dom";
import configDev from "../configs";
import { AuthContext } from "../contexts/AuthProvider";
import useFetch from "../hooks/useFetch";
import { getAuth, GoogleAuthProvider, signInWithPopup } from "firebase/auth";
import useLoginWithGoogle from "../hooks/useLoginWithGoogle";

export default function LoginPage() {
	const { user, setUser } = useContext(AuthContext);
	const { fetch, loading, error } = useFetch();
	const [formData, setFormData] = useState({
		email: "",
		password: "",
	});
	const { loginWithGoogle } = useLoginWithGoogle();
	const navigate = useNavigate();
	
	const auth = getAuth();

	const onLoginWithGoogle = async () => {
		const provider = new GoogleAuthProvider();

		await signInWithPopup(auth, provider)
			.then(async (res) => {
				// console.log(res)
				const tempUser = res?.user?.providerData[0];
				const result = await loginWithGoogle(tempUser.displayName, tempUser.email, tempUser.photoURL, tempUser.uid);
				if (result) {
					storeLocalStorageUser(result);
				}
			})
			.catch((err) => {
				console.log(err);
			});
	};

	const onSubmit = async () => {
		const options = {
			url: configDev["BACKEND_URL"] + "/auth/signIn",
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			data: formData,
			withCredentials: true,
		};

		const result = await fetch(options);
		if (result) {
			storeLocalStorageUser(result);
		}
	};

	const handleChangeInput = (e) => {
		const { name, value } = e.target;
		setFormData({ ...formData, [name]: value });
	};

	const handleKeyDown = (e) => {
		if (e.key === "Enter") {
			onSubmit();
		}
	};

	const storeLocalStorageUser = (result) => {
		setUser(result.metadata.user);
		localStorage.setItem("user", JSON.stringify(result.metadata.user));
		localStorage.setItem("refreshToken", result.metadata.refreshToken);
		localStorage.setItem("accessToken", result.metadata.accessToken);
		navigate("/chat");
	};

	return (
		<div
			className="w-[28rem] min-h-[24rem] flex flex-col items-center justify-center 
       bg-white/10 backdrop-blur-md rounded-2xl p-8 gap-4 shadow-2xl border border-white/20"
		>
			<div className="flex flex-col items-center mb-6">
				<h1 className="text-4xl font-bold text-white mb-2 tracking-tight">
					SQL <span className="text-blue-400">BigBrother</span>
				</h1>
				<p className="text-white/70 text-sm font-medium">Intelligent SQL Query Assistant</p>
			</div>
			<label className="w-full bg-white/10 backdrop-blur-sm rounded-xl flex items-center gap-4 px-4 py-3 border border-white/20 focus-within:border-blue-400/50 transition-colors">
				<LuAtSign className="text-white/70" />
				<input
					type="email"
					placeholder="Email"
					name="email"
					value={formData["email"]}
					className="bg-transparent text-white placeholder:text-white/50 flex-1 outline-none"
					onChange={(e) => {
						handleChangeInput(e);
					}}
				/>
			</label>
			<label className="w-full bg-white/10 backdrop-blur-sm rounded-xl flex items-center gap-4 px-4 py-3 border border-white/20 focus-within:border-blue-400/50 transition-colors">
				<LuKey className="text-white/70" />
				<input
					type="password"
					placeholder="Password"
					name="password"
					value={formData["password"]}
					className="bg-transparent text-white placeholder:text-white/50 flex-1 outline-none"
					onKeyDown={handleKeyDown}
					onChange={(e) => {
						handleChangeInput(e);
					}}
				/>
			</label>

			{error && (
				<div className="w-[60%] px-4 py-2 mt-2 text-center text-xs bg-red-400 text-white rounded opacity-90">
					{error}
				</div>
			)}

			<button
				disabled={loading}
				onClick={onSubmit}
				className="w-full h-12 rounded-xl text-center mt-4 bg-blue-500 hover:bg-blue-600 disabled:opacity-50 flex items-center justify-center transition-colors font-medium shadow-lg"
			>
				{loading ? (
					<span className="loading loading-infinity text-white"></span>
				) : (
					<span className="text-white text-base">Sign In</span>
				)}
			</button>

			<div className="divider text-xs my-4 text-white/50">OR</div>

			<Link
				to={"/register"}
				className="text-sm text-white/70 hover:text-blue-400 transition-colors"
			>
				Don't have an account? Sign up
			</Link>

			<button
				onClick={onLoginWithGoogle}
				className="google-login-btn w-full h-12 rounded-xl text-sm mb-3 bg-white/10 backdrop-blur-sm border border-white/20 hover:bg-white/20 flex items-center justify-center gap-3 transition-colors"
			>
				<div className="w-6 h-6 flex items-center justify-center">
					<GoogleSVG />
				</div>
				<span className="text-white font-medium">
					Continue with Google
				</span>
			</button>
		</div>
	);
}
