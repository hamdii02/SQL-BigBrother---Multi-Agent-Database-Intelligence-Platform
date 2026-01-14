import React, { useCallback } from "react";
import { useAuthContext } from "../../../../contexts/AuthProvider";
import useLogout from "../../../../hooks/useLogout";
import { useNavigate } from "react-router-dom";

export default function UserOptions({ handleToggleDatabase }) {
	const { user, setUser } = useAuthContext();
	const { logout } = useLogout();
	const navigate = useNavigate();

	const onLogout = useCallback(async () => {
		const clearUser = () => {
			setUser(null);
			localStorage.clear();
		};

		await logout();
		clearUser();
		navigate("/login");
	}, [user]);

	return (
		<div className="dropdown dropdown-hover dropdown-bottom dropdown-end">
			<div
				tabIndex={0}
				role="button"
				className="rounded-full hover:bg-zinc-600 cursor-pointer flex items-center gap-3 text-sm"
			>
				<img className="rounded-full" width={40} src={user.avatar} />
			</div>
			<ul
				tabIndex={0}
				className="mr-[-10px] dropdown-content menu bg-zinc-800 rounded-box z-[1] w-52 p-2 shadow"
			>
				<li onClick={handleToggleDatabase}>
					<a>Minimize</a>
				</li>
				<li onClick={onLogout}>
					<a className="text-red-400">Logout</a>
				</li>
			</ul>
		</div>
	);
}
