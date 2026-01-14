import React, { useCallback, useEffect, useRef } from "react";
import Message from "../Message";
import Response from "../Response";
import Recommend from "../../Recommend";
import classNames from "classnames";

export default function ChatBox({
	loading,
	messages,
	formData,
	onSendMessage,
	recommends,
	discoveredDatabases,
}) {
	const chatBoxRef = useRef(null);

	const scrollToBottom = useCallback(() => {
		if (chatBoxRef.current) {
			chatBoxRef.current.scrollTop = chatBoxRef.current.scrollHeight;
		}
	}, []);

	useEffect(() => {
		scrollToBottom();
	}, [messages]);

	return (
		<div
			ref={chatBoxRef}
			className="chatbox-content scroll-smooth overflow-y-scroll overflow-x-hidden w-full flex flex-1 flex-col items-start justify-between 2xl:px-5 px-7 py-2"
		>
			<div className="w-full flex flex-col items-start justify-between space-y-5">
				{messages.length === 0 ? (
					<div className="w-full h-[80svh] flex flex-col items-center justify-center">
						<img
							className={classNames({
								"w-56": formData["schema"],
								"w-72": !formData["schema"],
							})}
							src="https://ezticket.io.vn/logo_2.png"
							alt=""
						></img>
						{formData["schema"] && (
							<Recommend
								recommends={recommends}
								onSendMessage={onSendMessage}
							/>
						)}
					</div>
				) : (
					<>
						{messages?.map((mess, idx) => {
							if (mess.type === "introduction") {
								const getDbIcon = (type) => {
									switch (type) {
										case "postgresql": return "🐘";
										case "mysql": return "🐬";
										case "sqlite": return "💾";
										default: return "🗄️";
									}
								};

								return (
									<div key={idx} className="w-full mb-4 space-y-4">
										{/* Discovered Databases Summary */}
										{discoveredDatabases && discoveredDatabases.length > 0 && (
											<div className="p-5 bg-gradient-to-br from-green-500/15 to-blue-500/15 rounded-lg border border-green-400/30 backdrop-blur-sm">
												<div className="flex items-center gap-2 mb-4">
													<span className="text-2xl">🔍</span>
													<h3 className="text-lg font-semibold text-green-300">
														Discovered Databases ({discoveredDatabases.length})
													</h3>
												</div>
												<div className="space-y-3">
													{discoveredDatabases.map((db, dbIdx) => (
														<div 
															key={dbIdx}
															className="p-3 bg-gray-800/40 rounded-md border border-gray-600/30"
														>
															<div className="flex items-start gap-3">
																<span className="text-2xl">{getDbIcon(db.type)}</span>
																<div className="flex-1">
																	<div className="flex items-center gap-2 mb-1">
																		<span className="font-semibold text-gray-200">
																			{db.name || db.database || 'Unknown'}
																		</span>
																		<span className="px-2 py-0.5 text-xs bg-blue-500/30 text-blue-300 rounded">
																			{db.type?.toUpperCase()}
																		</span>
																	</div>
																	{db.path && (
																		<div className="text-sm text-gray-400 truncate">
																			📁 {db.path}
																		</div>
																	)}
																	{db.host && (
																		<div className="text-sm text-gray-400">
																			🌐 {db.host}
																		</div>
																	)}
																	{db.size_readable && (
																		<div className="text-sm text-gray-400">
																			💿 {db.size_readable}
																		</div>
																	)}
																</div>
															</div>
														</div>
													))}
												</div>
											</div>
										)}

										{/* Welcome Message */}
										<div className="p-6 bg-gradient-to-br from-blue-500/20 to-purple-500/20 rounded-lg border border-blue-400/30 backdrop-blur-sm">
											<div className="flex items-start gap-3">
												<div className="flex-shrink-0 w-10 h-10 bg-blue-500 rounded-full flex items-center justify-center">
													<span className="text-white text-xl">👋</span>
												</div>
												<div className="flex-1">
													<h3 className="text-lg font-semibold text-blue-300 mb-3">Welcome to SQL BigBrother!</h3>
													<div className="text-gray-200 whitespace-pre-wrap leading-relaxed">
														{mess.body}
													</div>
												</div>
											</div>
										</div>
									</div>
								);
							}
							return mess.type === "question" ? (
								<Message key={idx} message={mess} />
							) : (
								<Response recommends={recommends} onSendMessage={onSendMessage} key={idx} message={mess} />
							);
						})}

						{loading && (
							<Response
								message={"Đang xử lý"}
								isSkeleton={true}
							/>
						)}
					</>
				)}
			</div>
		</div>
	);
}
