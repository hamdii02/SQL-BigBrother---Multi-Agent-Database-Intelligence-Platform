import React, { useEffect, useState } from "react";
import ChatTab from "./ChatTab";
import SchemaTab from "./SchemaTab";
import DiscoveredDatabases from "../DiscoveredDatabases";
import { LuDatabase, LuHardDrive, LuMessageSquare } from "react-icons/lu";
import useChat from "../../../hooks/useChat";
import { useParams } from "react-router-dom";
import { useAuthContext } from "../../../contexts/AuthProvider";
import UserOptions from "./UserOptions";

export default function Sidebar({
	formData,
	handleChangeForm,
	showDatabase,
	sidebarTab,
	setSidebarTab,
	handleToggleDatabase,
	setRecommends,
	discoveredDatabases,
}) {
	const { chats, setChats } = useAuthContext();
	const {
		loadHistoryChats,
		loading: chatLoading,
		error: chatError,
	} = useChat();
	const { chatId } = useParams();

	// LOAD HISTORY CHATS
	useEffect(() => {
		const LoadHistory = async () => {
			const result = await loadHistoryChats();
			if (!chatError) {
				// console.log(result);
				setChats(result?.metadata);
				const chat = result?.metadata.find(
					(chat) => chat._id === chatId
				);
				handleChangeForm("schema", chat?.schema || "");
			}
		};

		LoadHistory();
	}, [chatId]);

	return (
		<>
			{sidebarTab === "chat" ? (
				<ChatTab
					handleToggleDatabase={handleToggleDatabase}
					handleChangeForm={handleChangeForm}
					setSidebarTab={setSidebarTab}
				/>
			) : sidebarTab === "databases" ? (
				<>
					<div className="bg-zinc-800 border-b border-zinc-600 w-full text-[#ccc] px-6 text-center h-16 flex items-center justify-between">
						<div className="flex items-center justify-center gap-2 cursor-default">
							<div
								onClick={() => setSidebarTab("chat")}
								className="p-3 rounded-box hover:bg-[#353535] cursor-pointer"
							>
								<LuMessageSquare size={20} />
							</div>
							<div
								onClick={() => setSidebarTab("schema")}
								className="p-3 rounded-box hover:bg-[#353535] cursor-pointer"
							>
								<LuDatabase size={20} />
							</div>
							<div
								onClick={() => setSidebarTab("databases")}
								className="active flex items-center gap-2 px-4 py-2 rounded-box"
							>
								<LuHardDrive size={20} />
							</div>
						</div>
						<UserOptions handleToggleDatabase={handleToggleDatabase} />
					</div>
					<div className="flex-1 overflow-y-auto p-4">
						<DiscoveredDatabases />
					</div>
				</>
			) : (
				<SchemaTab
					formData={formData}
					handleChangeForm={handleChangeForm}
					setSidebarTab={setSidebarTab}
					handleToggleDatabase={handleToggleDatabase}
					setRecommends={setRecommends}
				/>
			)}
		</>
	);
}
