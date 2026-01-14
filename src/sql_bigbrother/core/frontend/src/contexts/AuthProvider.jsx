import React, { createContext, useContext, useEffect, useState } from "react";

export const AuthContext = createContext();
import { getAuth } from "firebase/auth";
import "../firebase/config";

export const useAuthContext = () => {
	return useContext(AuthContext);
}

export default function AuthProvider({ children }) {
	const [user, setUser] = useState(() => {
		const jsonUser = localStorage.getItem("user");
		return JSON.parse(jsonUser) || null;
	});
	const [chats, setChats] = useState([]);
	const [showLoading, setShowLoading] = useState(false);
	
	
	useEffect(() => {
		if (!user) {
			setUser(null);
			localStorage.clear();
		}
	}, [user]);

	return (
		<AuthContext.Provider value={{ user, setUser, showLoading, setShowLoading, chats, setChats }}>
			{children}
		</AuthContext.Provider>
	);
}
