import React from "react";
import Markdown from "../../../Markdown";
import { LuCopy, LuRefreshCcw, LuThumbsDown } from "react-icons/lu";
import Table from "../../Table";
import { formatTimestamp, isNumber } from "../../../../utils";
import classNames from "classnames";
import BarChart from "../../Charts/Barchart";
import { useParams } from "react-router-dom";

export default function Response({
	message,
	recommends,
	onSendMessage,
	isSkeleton = false,
}) {
	const { chatId } = useParams();

	// message?.execute?.forEach(e => console.log(e))
	return (
		<div className="mx-auto flex flex-1 gap-1 text-base w-[100%] md:max-w-3xl lg:max-w-[40rem] xl:max-w-[48rem]">
			<div className="flex-shrink-0 flex flex-col relative items-end">
				<div>
					<div className="pt-0.5 juice:pt-0">
						<div className="gizmo-bot-avatar flex h-12 w-12 items-center justify-center overflow-hidden rounded-full juice:h-8 juice:w-8">
							<div className="relative mt-[-10px] rounded-sm flex items-center justify-center bg-token-main-surface-primary text-token-text-primary h-14 w-14">
								<img
									src="https://ezticket.io.vn/logo.ico"
									alt=""
								/>
							</div>
						</div>
					</div>
				</div>
			</div>
			{isSkeleton ? (
				<>
					<div className="flex w-full flex-col gap-3 p-[8px]">
						<div className="skeleton h-4 w-full bg-[#ccc]"></div>
						<div className="skeleton h-4 w-[50%] bg-[#ccc]"></div>
						<div className="skeleton h-4 w-[70%] bg-[#ccc]"></div>
						<div className="skeleton h-4 w-full bg-[#ccc]"></div>
					</div>
				</>
			) : (
				<div className="relative flex w-full min-w-0 flex-col agent-turn">
					<div className="flex-col gap-1 md:gap-3">
						<div className="flex flex-grow flex-col w-full max-w-full">
							<div className="min-h-[20px] text-message flex flex-col items-start break-words juice:w-full juice:items-end overflow-x-auto gap-2">
								<div className="flex w-full flex-col gap-1 juice:empty:hidden juice:first:pt-[3px]">
									{/* Check if this is a conversational response (starts with emoji) */}
									{message?.body?.startsWith('💬') ? (
										<div className="markdown prose w-full break-words dark:prose-invert dark text-sm leading-7 p-4 rounded-lg bg-gradient-to-br from-slate-700/50 to-slate-600/50 border border-slate-500/30">
											<Markdown content={message?.body.replace('💬 ', '')} />
										</div>
									) : (
										<>
											<div className="markdown prose w-full break-words dark:prose-invert dark text-sm leading-7 p-2 rounded-lg space-y-6">
												<strong>SQL Query: </strong>
												<Markdown content={message?.body} />
											</div>

											{message?.data?.rows?.length != 0 ? (
												<>
													<div className="markdown prose w-full break-words dark:prose-invert dark text-sm leading-6 p-2 rounded-lg">
														<strong>Execution: </strong>
													</div>
													<Table
														data={message?.data?.rows}
														columns={message?.data?.columns}
													/>

													{message?.data?.rows[0]?.some((e) =>
														isNumber(e)
													) && (
														<BarChart
															data={message?.data}
														/>
													)}
												</>
											) : (
												<>
													<p className="text-amber-500 text-sm p-[8px] bg-amber-500/10 rounded-lg border border-amber-500/30">
														💡 Query generated successfully. 
														{message?.body?.includes('execute') || message?.body?.includes('run') ? 
															<span> Say <strong>"execute"</strong> or <strong>"run the query"</strong> to see results.</span>
															:
															<span> No results to display yet.</span>
														}
													</p>

													{recommends && recommends.length > 0 && (
														<>
															<strong>Suggestions:</strong>
															<ul className="w-full flex flex-col items-start justify-center gap-2">
																{recommends?.map((rec, idx) => {
																	return <li onClick={() => {
																		onSendMessage(chatId, rec);
																	}} className="hover:bg-[#bdc] cursor-pointer w-full p-2 rounded-lg text-sm" key={idx}>{idx + 1}. {rec}</li>
																})}
															</ul>
														</>
													)}
												</>
											)}
										</>
									)}
								</div>
							</div>
						</div>
						<div className="mt-1 flex gap-3 empty:hidden juice:-ml-3">
							<div className="items-center justify-start rounded-xl p-1 flex">
								<div className="flex items-center">
									<span className="flex" data-state="closed">
										<button className="rounded-lg text-token-text-secondary hover:bg-[#ccc]">
											<span className="flex h-[30px] w-[30px] items-center justify-center">
												<LuCopy />
											</span>
										</button>
									</span>
									<span className="flex" data-state="closed">
										<button className="rounded-lg text-token-text-secondary hover:bg-[#ccc]">
											<span className="flex h-[30px] w-[30px] items-center justify-center">
												<LuRefreshCcw />
											</span>
										</button>
									</span>
									<div className="flex">
										<span className="" data-state="closed">
											<button className="rounded-lg text-token-text-secondary hover:bg-[#ccc]">
												<span className="flex h-[30px] w-[30px] items-center justify-center">
													<LuThumbsDown />
												</span>
											</button>
										</span>
									</div>
									<div
										className={classNames({
											"text-xs text-gray-400 h-[30px] flex items-center ml-4": true,
											"self-end": true,
										})}
									>
										{formatTimestamp(message.createdAt)}
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			)}
		</div>
	);
}
