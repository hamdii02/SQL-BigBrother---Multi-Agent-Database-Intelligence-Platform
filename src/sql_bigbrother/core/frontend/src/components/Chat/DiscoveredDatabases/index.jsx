import React, { useEffect, useState } from "react";
import axios from "axios";
import configs from "../../../configs";
import { LuDatabase, LuRefreshCw, LuCheck, LuX } from "react-icons/lu";

export default function DiscoveredDatabases({ onSelect }) {
	const [databases, setDatabases] = useState([]);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState(null);
	const [summary, setSummary] = useState("");

	const fetchDatabases = async () => {
		setLoading(true);
		setError(null);
		try {
			const response = await axios.get(`${configs["CREWAI_URL"]}/databases`);
			setDatabases(response.data.databases || []);
			setSummary(response.data.summary || "");
		} catch (err) {
			setError(err.message);
		} finally {
			setLoading(false);
		}
	};

	useEffect(() => {
		fetchDatabases();
	}, []);

	const handleRediscover = async () => {
		setLoading(true);
		try {
			const response = await axios.post(`${configs["CREWAI_URL"]}/databases/rediscover`);
			setDatabases(response.data.databases || []);
			setSummary(response.data.summary || "");
		} catch (err) {
			setError(err.message);
		} finally {
			setLoading(false);
		}
	};

	const getDbIcon = (type) => {
		switch (type) {
			case "postgresql":
				return "🐘";
			case "mysql":
				return "🐬";
			case "sqlite":
				return "💾";
			default:
				return "🗄️";
		}
	};

	if (loading) {
		return (
			<div className="flex items-center justify-center p-8">
				<div className="animate-spin text-blue-400">
					<LuRefreshCw size={32} />
				</div>
			</div>
		);
	}

	if (error) {
		return (
			<div className="p-4 bg-red-500/20 border border-red-400/30 rounded-lg">
				<p className="text-red-300">Error loading databases: {error}</p>
			</div>
		);
	}

	return (
		<div className="w-full space-y-4">
			<div className="flex items-center justify-between">
				<h3 className="text-lg font-semibold text-gray-200 flex items-center gap-2">
					<LuDatabase size={20} />
					Discovered Databases ({databases.length})
				</h3>
				<button
					onClick={handleRediscover}
					className="p-2 hover:bg-gray-700 rounded-lg transition-colors"
					title="Rediscover databases"
				>
					<LuRefreshCw size={18} />
				</button>
			</div>

			{databases.length === 0 ? (
				<div className="p-6 bg-yellow-500/20 border border-yellow-400/30 rounded-lg text-center">
					<p className="text-yellow-300">No databases discovered</p>
				</div>
			) : (
				<div className="space-y-2">
					{databases.map((db, idx) => (
						<div
							key={idx}
							className="p-4 bg-gray-800/50 border border-gray-600/30 rounded-lg hover:border-blue-400/50 transition-colors cursor-pointer"
							onClick={() => onSelect && onSelect(db, idx)}
						>
							<div className="flex items-start gap-3">
								<span className="text-2xl">{getDbIcon(db.type)}</span>
								<div className="flex-1">
									<div className="flex items-center gap-2 mb-1">
										<span className="font-semibold text-gray-200 capitalize">
											{db.type}
										</span>
										{db.status === "available" && (
											<span className="flex items-center gap-1 text-green-400 text-xs">
												<LuCheck size={14} />
												Available
											</span>
										)}
									</div>
									{db.path && (
										<p className="text-sm text-gray-400 truncate">
											{db.path}
										</p>
									)}
									{db.output && (
										<p className="text-xs text-gray-500 mt-1">
											{db.output}
										</p>
									)}
								</div>
							</div>
						</div>
					))}
				</div>
			)}

			{summary && (
				<div className="p-3 bg-gray-800/30 border border-gray-600/30 rounded-lg">
					<p className="text-xs text-gray-400 font-mono">{summary}</p>
				</div>
			)}
		</div>
	);
}
