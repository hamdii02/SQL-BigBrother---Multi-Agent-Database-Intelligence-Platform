import React from "react";
import { isNumber } from "../../../utils";

const Table = ({ data, columns }) => {
	// console.log(columns)
	return (
		<div className="overflow-x-auto p-[8px]">
			<table className="table bg-[#2d2d2d] rounded-none">
				{/* head */}
				<thead className="bg-[#bdc] text-zinc-800 font-bold">
					<tr>
						{columns?.map((col, idx) => {
							return <th key={idx}>{col}</th>;
						})}
					</tr>
				</thead>
				<tbody>
					{data?.map((row, rowIndex) => (
						<tr className="border-0" key={rowIndex}>
							{row.map((cell, cellIndex) => {
								const isNum = isNumber(cell);
								return !isNum ? (
									<td
										className="text-[#F6F5F5] text-xs"
										key={cellIndex}
									>
										{cell}
									</td>
								) : (
									<td
										className="text-[#71b190] text-xs"
										key={cellIndex}
									>
										{cell}
									</td>
								);
							})}
						</tr>
					))}
				</tbody>
			</table>
		</div>
	);
};

export default Table;
