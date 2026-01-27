import React, { useEffect, useState } from "react";
import {
	LuDatabase,
	LuHardDrive,
	LuHelpCircle,
	LuMessageSquare,
	LuPencil,
	LuPlus,
	LuTrash,
	LuZap,
} from "react-icons/lu";
import UserOptions from "../UserOptions";
import useChat from "../../../../hooks/useChat";
import { Link, useNavigate, useParams } from "react-router-dom";
import classNames from "classnames";
import { useAuthContext } from "../../../../contexts/AuthProvider";

export default function ChatTab({
	handleToggleDatabase,
	setSidebarTab,
	handleChangeForm,
}) {
	const { chatId } = useParams();
	const { chats, setChats } = useAuthContext();
	const navigate = useNavigate();
	const { deleteChat, error: chatError } = useChat();

	const onDeleteChat = async (_id) => {
		const result = await deleteChat(_id);
		navigate("/chat");
		setChats(chats.filter((chat) => chat._id !== _id));
		console.log(result);
	};

	return (
		<>
			<div className="bg-slate-800/50 backdrop-blur-md border-b border-white/10 w-full text-white px-6 text-center h-16 flex items-center justify-between">
				<div className="flex items-center justify-start gap-3">
					<h3 className="text-lg font-semibold text-white">SQL <span className="text-blue-400">BigBrother</span></h3>
				</div>
				<div className="flex items-center justify-center gap-2 cursor-default">
					<div
						onClick={() => setSidebarTab("chat")}
						className="bg-blue-500/20 border border-blue-400/30 flex items-center gap-2 px-4 py-2 rounded-xl"
					>
						<LuMessageSquare size={18} />
					</div>
					<div
						onClick={() => setSidebarTab("schema")}
						className="p-2 rounded-xl hover:bg-white/10 cursor-pointer transition-colors"
					>
						<LuDatabase size={18} />
					</div>
					<div
						onClick={() => setSidebarTab("databases")}
						className="p-2 rounded-xl hover:bg-white/10 cursor-pointer transition-colors"
					>
						<LuHardDrive size={18} />
					</div>
					<div className="p-2 rounded-xl hover:bg-white/10 cursor-pointer transition-colors">
						<LuHelpCircle size={18} />
					</div>
				</div>

				<UserOptions handleToggleDatabase={handleToggleDatabase} />
			</div>

			<div className="overflow-y-hidden relative w-full flex flex-col flex-1 text-sm bg-slate-800/30 backdrop-blur-sm text-white overflow-x-hidden">
				{/* NOW CHATS */}
				<div className="text-white p-4">
					<div className="py-2 font-semibold text-sm text-white/70 cursor-default">
						Current Session
					</div>
					<div
						onClick={() => {
							handleChangeForm("schema", "");
							setSidebarTab("schema");
						}}
						className={classNames({
							"chat-title relative rounded-lg bg-[#353535] cursor-pointer text-[.975rem]": true,
							active: !chatId,
						})}
					>
						<Link
							to={"/chat"}
							className="flex items-center justify-between gap-2 py-2 px-4"
						>
							<p>New chat</p>
							<div className="flex items-center opacity-0">
								<div className="p-2">
									<LuPlus />
								</div>
							</div>
						</Link>
					</div>
				</div>

				<div className="py-[0.05rem] bg-zinc-600"></div>

				{/* PREVIOUS CHATS */}
				<div className="flex-1 text-white p-3">
					<div className="py-2 font-normal text-xs cursor-default">
						Previous chats
					</div>
					<ul className="font-normal space-y-[0.4rem] max-h-[70svh] overflow-y-scroll my-2">
						{chats?.map((chat, idx) => {
							return (
								<li key={idx}>
									<Link
										to={`/chat/${chat._id}`}
										className={classNames({
											"chat-title flex item-center justify-between relative rounded-lg hover:bg-[#353535] text-[.975rem] px-3 py-1": true,
											active: chat._id == chatId,
										})}
									>
										<div
											className="flex items-center justify-between gap-2 py-1 w-[80%]"
										>
											<p className={classNames({
												"typing": chat._id == chatId
											})}>{chat.title}</p>
										</div>
										<div className="flex items-center opacity-0">
											<div className="p-2 hover:bg-[#2d2d2d] rounded-full">
												<LuPencil />
											</div>
											<div
												onClick={() =>
													onDeleteChat(chat?._id)
												}
												className="p-2 hover:bg-[#2d2d2d] rounded-full"
											>
												<LuTrash color="#FA7070" />
											</div>
										</div>
									</Link>
								</li>
							);
						})}
					</ul>
				</div>
			</div>
		</>
	);
}
