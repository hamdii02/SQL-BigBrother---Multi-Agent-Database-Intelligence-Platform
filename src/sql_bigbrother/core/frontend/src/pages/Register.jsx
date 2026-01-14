import React, { useEffect, useState } from "react";
import { LuAtSign, LuFileKey, LuKey, LuUser } from "react-icons/lu";
import { Link, useNavigate } from "react-router-dom";
import configDev from "../configs";
import useFetch from "../hooks/useFetch";

export default function RegisterPage() {
	const { fetch, loading, error } = useFetch();
	const navigate = useNavigate();

	const [formData, setFormData] = useState({
		username: "",
		email: "",
		password: "",
		confirmPassword: "",
		gender: "male",
	});

	const onSubmit = async () => {	
		const options = {
			url: configDev['BACKEND_URL'] + "/auth/signUp",
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			data: formData,
			withCredentials: true,
		};

		const result = await fetch(options);
		if (result) {
			navigate("/login");
		}
	};

	const handleChangeInput = (e) => {
		const { name, value } = e.target;
		setFormData({ ...formData, [name]: value });
	};

	return (
		<div
			className="w-[30rem] min-h-[28rem] flex flex-col items-center justify-center 
       bg-white/10 backdrop-blur-md rounded-2xl p-8 gap-4 shadow-2xl border border-white/20"
		>
			<div className="flex flex-col items-center mb-6">
				<h1 className="text-4xl font-bold text-white mb-2 tracking-tight">
					SQL <span className="text-blue-400">BigBrother</span>
				</h1>
				<p className="text-white/70 text-sm font-medium">Create your account</p>
			</div>

			<label className="w-full bg-white/10 backdrop-blur-sm rounded-xl flex items-center gap-4 px-4 py-3 border border-white/20 focus-within:border-blue-400/50 transition-colors">
				<LuUser className="text-white/70" />
				<input
					type="text"
					placeholder="Username"
					name="username"
					value={formData["username"]}
					className="bg-transparent text-white placeholder:text-white/50 flex-1 outline-none"
					onChange={(e) => {
						handleChangeInput(e);
					}}
				/>
			</label>

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
					onChange={(e) => {
						handleChangeInput(e);
					}}
				/>
			</label>

			<label className="w-full bg-white/10 backdrop-blur-sm rounded-xl flex items-center gap-4 px-4 py-3 border border-white/20 focus-within:border-blue-400/50 transition-colors">
				<LuFileKey className="text-white/70" />
				<input
					type="password"
					placeholder="Confirm Password"
					name="confirmPassword"
					value={formData["confirmPassword"]}
					className="bg-transparent text-white placeholder:text-white/50 flex-1 outline-none"
					onChange={(e) => {
						handleChangeInput(e);
					}}
				/>
			</label>

			<div className="flex items-center justify-center gap-8 mt-3">
				<label className="flex items-center gap-3 cursor-pointer">
					<input
						onChange={(e) => {
							handleChangeInput(e);
						}}
						type="radio"
						name="gender"
						value="male"
						className="radio radio-sm border-2 border-white/30 checked:bg-blue-500 checked:border-blue-500"
						defaultChecked
					/>
					<span className="text-white/80 text-sm">Male</span>
				</label>
				<label className="flex items-center gap-3 cursor-pointer">
					<input
						onChange={(e) => {
							handleChangeInput(e);
						}}
						type="radio"
						name="gender"
						value="female"
						className="radio radio-sm border-2 border-white/30 checked:bg-pink-500 checked:border-pink-500"
					/>
					<span className="text-white/80 text-sm">Female</span>
				</label>
			</div>

			{error && (
				<div className="w-[60%] px-4 py-2 mt-2 text-center text-xs bg-red-400 text-white rounded opacity-90">
					{error}
				</div>
			)}

			<button
				disabled={loading}
				onClick={onSubmit}
				className="w-full h-12 rounded-xl text-center mt-6 bg-blue-500 hover:bg-blue-600 disabled:opacity-50 flex items-center justify-center transition-colors font-medium shadow-lg"
			>
				{loading ? (
					<span className="loading loading-infinity text-white"></span>
				) : (
					<span className="text-white text-base">Create Account</span>
				)}
			</button>

			<div className="divider text-xs my-4 text-white/50">OR</div>

			<Link
				to={"/login"}
				className="text-sm text-white/70 hover:text-blue-400 transition-colors"
			>
				Already have an account? Sign in
			</Link>
		</div>
	);
}