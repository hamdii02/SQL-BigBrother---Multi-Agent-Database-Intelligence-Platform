import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

export default function Recommend({ recommends, onSendMessage }) {
	const { chatId } = useParams();

	useEffect(() => {
		// console.log(chatId)
	}, [recommends]);

	return (
		<>
			{recommends?.length != 0 && (
				<div className="w-[70%] grid 2xl:grid-cols-4 grid-cols-2 items-center justify-center gap-4">
					{recommends?.map((rec, idx) => {
						return (
							<div
								key={idx}
								onClick={() => {
									onSendMessage(chatId, rec);
								}}
								className="text-[0.925rem] bg-[#E4E4FF] cursor-pointer hover:opacity-80 p-4 2xl:min-h-[150px] min-h-[100px] border border-gray-400 rounded-lg"
							>
								{rec}
							</div>
						);
					})}
				</div>
			)}
		</>
	);
}
