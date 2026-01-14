import React, { useState } from "react";
import { useParams } from "react-router-dom";

export default function Modal({ onSendMessage, input, clearInput, setShowModal }) {
	const [checked, setChecked] = useState(false);
	const { chatId } = useParams();
	
	const onConfirm = () => {
        setShowModal(!checked)
        onSendMessage(chatId, input, clearInput)
    };

	return (
		<div>
			<dialog id="confirm" className="modal">
				<div className="modal-box text-[#fff]">
					<h3 className="font-bold text-lg text-red-400">
						Confirmation
					</h3>
					<p className="py-4">
						Some models would harm your device. <br />
						Please check it again before sending your request
					</p>
					<label className="cursor-pointer label w-[34%] p-0">
						<input
							type="checkbox"
							className="checkbox checkbox-sm checkbox-info"
							checked={checked}
                            onChange={() => setChecked(prev => !prev)}
						/>
						<span className="label-text mt-[2px]">
							Don't show it again
						</span>
					</label>
					<div className="modal-action">
						<form method="dialog">
							{/* if there is a button in form, it will close the modal */}
							<button
								onClick={onConfirm}
								className="bg-[#71b190] hover:opacity-80 mx-3 text-white w-24 py-2 rounded-lg"
							>
								Send
							</button>
							<button className="w-24 bg-zinc-700 hover:opacity-80 py-2 rounded-lg">
								Cancel
							</button>
						</form>
					</div>
				</div>
			</dialog>
		</div>
	);
}
