import React, { useState, memo } from "react";
import { ResponsiveBar } from "@nivo/bar";
import { ArraysToMap, isNumber } from "../../../../utils";
import classNames from "classnames";

const BarChart = memo(({ data }) => {
	// console.log(data)
	const columns = data?.columns;
	const rows = data?.rows;
	const yStart = data?.rows[0].findIndex((e) => isNumber(e));
	const mapData = ArraysToMap(columns, rows);
	const [axis, setAxis] = useState({
		x: 0,
		y: yStart,
	});

	return (
		<>
			<div className="bg-white/5 backdrop-blur-sm rounded-xl border border-white/10 p-6 mt-4">
				<div className="mb-6">
					<h3 className="text-white font-semibold text-lg mb-4">Data Visualization</h3>
					
					<div className="space-y-4">
						<div>
							<label className="block text-white/70 text-sm font-medium mb-2">Y-Axis (Values):</label>
							<div className="flex flex-wrap gap-2">
								{columns.map((col, idx) => (
									<button
										onClick={() => setAxis({ ...axis, y: idx })}
										className={classNames({
											"px-3 py-1 rounded-lg text-sm font-medium transition-colors": true,
											"bg-blue-500 text-white": axis["y"] === idx,
											"bg-white/10 text-white/80 hover:bg-white/20": axis["y"] !== idx,
										})}
										key={idx}
									>
										{col}
									</button>
								))}
							</div>
						</div>

						<div>
							<label className="block text-white/70 text-sm font-medium mb-2">X-Axis (Categories):</label>
							<div className="flex flex-wrap gap-2">
								{columns.map((col, idx) => (
									<button
										onClick={() => setAxis({ ...axis, x: idx })}
										className={classNames({
											"px-3 py-1 rounded-lg text-sm font-medium transition-colors": true,
											"bg-purple-500 text-white": axis["x"] === idx,
											"bg-white/10 text-white/80 hover:bg-white/20": axis["x"] !== idx,
										})}
										key={idx}
									>
										{col}
									</button>
								))}
							</div>
						</div>
					</div>
				</div>

				<div className="bg-slate-900/50 rounded-lg p-4" style={{ height: "400px" }}>
					<ResponsiveBar
						data={mapData}
						keys={[columns[axis["y"]]]}
						indexBy={columns[axis["x"]]}
						margin={{ top: 30, right: 30, bottom: 60, left: 80 }}
						padding={0.3}
						colors={["#3B82F6", "#8B5CF6", "#06B6D4", "#10B981", "#F59E0B"]}
						theme={{
							background: "transparent",
							text: {
								fill: "#FFFFFF",
								fontSize: 12,
								fontFamily: "Inter, sans-serif"
							},
							axis: {
								domain: {
									line: {
										stroke: "#374151",
										strokeWidth: 1
									}
								},
								ticks: {
									line: {
										stroke: "#374151",
										strokeWidth: 1
									},
									text: {
										fill: "#D1D5DB"
									}
								}
							},
							grid: {
								line: {
									stroke: "#374151",
									strokeWidth: 0.5
								}
							}
						}}
						labelSkipWidth={12}
						labelSkipHeight={12}
						labelTextColor="#FFFFFF"
						animate={true}
						motionConfig="wobbly"
					/>
				</div>
			</div>
		</>
	);
});

export default BarChart;
