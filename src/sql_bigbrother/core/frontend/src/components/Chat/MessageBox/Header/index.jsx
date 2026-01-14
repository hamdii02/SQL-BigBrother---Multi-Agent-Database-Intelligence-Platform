import classNames from "classnames";
import { useState } from "react";
import { LuChevronDown, LuDatabase } from "react-icons/lu";

const MODELS = [
	{ name: "Qwen 2.5 7B (Default)", model: "qwen2.5:7b" },
	{ name: "Qwen 2.5 14B", model: "qwen2.5:14b" },
	{ name: "Qwen 3 14B", model: "qwen3:14b" },
	{ name: "Qwen 3 30B", model: "qwen3:30b" },
	{ name: "GPT-OSS 20B", model: "gpt-oss:20b" },
];

export default function Header({
	formData,
	handleChangeForm,
	showDatabase,
	handleToggleDatabase,
}) {
	const [visiblePicker, setVisiblePicker] = useState(false);

	return (
		<div className="chatbox-header w-full flex items-center justify-between px-6 py-4 mb-6 bg-slate-800/30 backdrop-blur-md border-b border-white/10">
			<div className="flex items-center justify-center gap-4">
				<div className="flex items-center gap-3">
					<h2 className="text-xl font-semibold text-white">SQL <span className="text-blue-400">BigBrother</span></h2>
					<span className="text-xs bg-blue-500/20 text-blue-400 px-2 py-1 rounded-full">AI Assistant</span>
				</div>
				<div className="flex flex-col items-start justify-center">
					<div className="dropdown">
						<div
							tabIndex={0}
							onClick={() => setVisiblePicker(true)}
							role="button"
							className="px-4 py-2 rounded-xl bg-white/10 backdrop-blur-sm border border-white/20 hover:bg-white/20 flex items-center justify-between text-white text-sm min-w-[180px] transition-colors"
						>
							<span className="truncate">{MODELS.find(m => m.model === formData["model"])?.name || formData["model"]}</span>
							<LuChevronDown className="ml-2" />
						</div>
						{visiblePicker && (
							<ul
								onClick={() => setVisiblePicker(false)}
								tabIndex={0}
								className="dropdown-content menu bg-slate-800/95 backdrop-blur-md rounded-xl border border-white/20 z-[1] w-64 p-2 shadow-xl mt-2"
							>
								{MODELS.map((m, idx) => {
									return (
										<li key={idx}>
											<a onClick={() => handleChangeForm("model", m.model)}>
												{m.name}
											</a>
										</li>
									);
								})}
								
							</ul>
						)}
					</div>
				</div>
			</div>

			<div className="flex items-center justify-center gap-3">
				<div
					onClick={handleToggleDatabase}
					className={classNames({
						"p-3 rounded-xl bg-white/10 backdrop-blur-sm border border-white/20 hover:bg-white/20 cursor-pointer text-white transition-colors": true,
						hidden: showDatabase,
					})}
				>
					<LuDatabase size={20} />
				</div>
			</div>
		</div>
	);
}
