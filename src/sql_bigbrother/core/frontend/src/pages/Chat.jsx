import React, { useCallback, useEffect, useState } from "react";
import MessageBox from "../components/Chat/MessageBox";
import Sidebar from "../components/Chat/Sidebar";
import classNames from "classnames";
import configs from "../configs";
import axios from "axios";

export default function ChatPage() {
	const [formData, setFormData] = useState({
		question: "",
		schema: "",
		// is_explain: false,
		model: "qwen2.5:7b",
	});
	const [sidebarTab, setSidebarTab] = useState("chat");
	const [initialIntroduction, setInitialIntroduction] = useState(null);
	const [isAutoInitialized, setIsAutoInitialized] = useState(false);
	const [discoveredDatabases, setDiscoveredDatabases] = useState([]);
	const [sessionId, setSessionId] = useState(null);
	const [chatHistory, setChatHistory] = useState([]);

	// Fetch initial chat state on mount
	useEffect(() => {
		const fetchInitialState = async () => {
			try {
				const response = await axios.get(`${configs["CREWAI_URL"]}/chat/init`);
				if (response.data) {
					setInitialIntroduction(response.data.introduction);
					setFormData(prev => ({
						...prev,
						schema: response.data.sql_content || ""
					}));
					setRecommends(response.data.recommends || []);
					setDiscoveredDatabases(response.data.discovered_databases?.databases || []);
					setIsAutoInitialized(true);
				}
			} catch (error) {
				console.log("Auto-initialization not available:", error.message);
			}
		};

		fetchInitialState();
	}, []);

	const handleChangeForm = useCallback(
		(name, value) => {
			setFormData({ ...formData, [name]: value });
		},
		[formData]
	);

	const [showDatabase, setShowDatabase] = useState(true);
	const handleToggleDatabase = useCallback(() => {
		setShowDatabase((prev) => !prev);
	}, []);

	const [recommends, setRecommends] = useState([]);

	return (
		<div className="flex justify-start items-center w-full gap-0 h-full">
			<div
				className={classNames({
					"h-[100svh] flex flex-col items-center shadow-2xl bg-slate-800/50 backdrop-blur-md border-r border-white/10 transition-all": true,
					"w-[25rem]": sidebarTab === "chat",
					"w-[35rem]": sidebarTab === "schema" || sidebarTab === "databases",
					hidden: !showDatabase,
				})}
			>
				<Sidebar
					formData={formData}
					handleChangeForm={handleChangeForm}
					showDatabase={showDatabase}
					sidebarTab={sidebarTab}
					setSidebarTab={setSidebarTab}
					handleToggleDatabase={handleToggleDatabase}
					setRecommends={setRecommends}
					discoveredDatabases={discoveredDatabases}
				/>
			</div>
			<div
				className={classNames({
					"h-[100svh] flex flex-1 flex-col items-center bg-slate-900/30 backdrop-blur-sm": true,
					"w-[70%]": showDatabase,
					"w-[100%]": !showDatabase,
				})}
			>
				<MessageBox
					formData={formData}
					handleChangeForm={handleChangeForm}
					showDatabase={showDatabase}
					handleToggleToggle={handleToggleDatabase}
					setSidebarTab={setSidebarTab}
					recommends={recommends}
					setRecommends={setRecommends}
					initialIntroduction={initialIntroduction}
					isAutoInitialized={isAutoInitialized}
					sessionId={sessionId}
					setSessionId={setSessionId}
					chatHistory={chatHistory}
					setChatHistory={setChatHistory}
					discoveredDatabases={discoveredDatabases}
				/>
			</div>
		</div>
	);
}
