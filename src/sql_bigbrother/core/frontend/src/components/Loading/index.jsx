import React from 'react'

export default function Loading() {
  return (
    <div className='fixed z-[1000] w-full h-[100svh] bg-zinc-800 opacity-70 flex items-center justify-center'>
        <span className="loading loading-spinner w-[50px] text-[#71b190]"></span>
    </div>
  )
}
