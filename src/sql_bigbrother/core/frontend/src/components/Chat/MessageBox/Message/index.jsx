import React from "react";
import { formatTimestamp } from "../../../../utils";
import classNames from "classnames";

export default function Message({
	message,
	shouldShake = false,
	hiddenTime = false,
}) {
	return (
		<div className="mx-auto flex flex-1 justify-end gap-1 text-base w-[100%] md:max-w-3xl lg:max-w-[40rem] xl:max-w-[48rem]">
			<div
				className={`message-right flex flex-col items-start gap-2 my-2 max-w-[60%]`}
			>
				<div
					className={classNames({
						"message text-sm rounded-lg px-4 py-2 bg-gray-100 text-black": true,
						"self-end": true,
						shake: shouldShake,
					})}
					style={{
						wordWrap: "break-word",
						overflowWrap: "break-word",
						wordBreak: "break-word",
					}}
				>
					{message.body}
				</div>
				<div
					className={classNames({
						"text-xs text-gray-400": true,
						hidden: hiddenTime,
						"self-end": true,
					})}
				>
					{formatTimestamp(message.createdAt)}
				</div>
			</div>
		</div>
	);
}
