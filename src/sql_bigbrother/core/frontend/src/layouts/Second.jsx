import React from "react";
import { Outlet } from "react-router-dom";


export default function SecondLayout() {
	return (
		<>
			<main className="main w-[100vw] min-h-[100svh] bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
				<Outlet />
			</main>
		</>
	);
}
