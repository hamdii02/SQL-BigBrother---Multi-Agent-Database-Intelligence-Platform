import React, { useCallback, useEffect, useState } from "react";
import MessageBox from "../components/Chat/MessageBox";
import Sidebar from "../components/Chat/Sidebar";
import classNames from "classnames";

export default function ChatPage() {
	const [formData, setFormData] = useState({
		question: "",
		schema: "",
		// is_explain: false,
		model: "qwen2.5:7b",
	});
	const [sidebarTab, setSidebarTab] = useState("chat");

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
					"w-[35rem]": sidebarTab === "schema",
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
					handleToggleDatabase={handleToggleDatabase}
					setSidebarTab={setSidebarTab}
					recommends={recommends}
					setRecommends={setRecommends}
				/>
			</div>
		</div>
	);
}
