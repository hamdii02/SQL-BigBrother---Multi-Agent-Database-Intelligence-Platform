import { LuPhoneCall, LuYoutube } from 'react-icons/lu';
import { RiMessengerLine } from 'react-icons/ri';
import { SiZalo } from 'react-icons/si';

export default function SocialWidgets() {
  return (
    <div
      className="fixed-contact flex flex-col items-center justify-center
        bg-[#202020] fixed z-100 right-0 top-[50%] translate-y-[-50%]
        transition-all duration-300 rounded-l-[30px] px-2 py-4"
    >
      <a
        className="phone-ring w-[36px] h-[36px] leading-[36px] rounded-[30px]
          bg-[#202020] relative my-1 flex items-center justify-center
          hover:text-[#71B190]"
        href="#"
        target="_blank"
      >
        <LuPhoneCall size="23" />
      </a>
      <a
        className="w-[36px] h-[36px] leading-[36px] rounded-[30px]
          bg-[#202020] relative my-1 flex items-center justify-center
          hover:text-[#9F33FF] hover:translate-y-[-4px] transition-all duration-300 ease"
        href="https://m.me/101213069498192"
        target="_blank"
      >
        <RiMessengerLine size="25" />
      </a>
      <a
        className="w-[36px] h-[36px] leading-[36px] rounded-[30px]
          bg-[#202020] relative my-1 flex items-center justify-center
          hover:text-[#5FBDFF] hover:translate-y-[-4px] transition-all duration-300 ease"
        href="#"
        target="_blank"
      >
        <SiZalo size="25" />
      </a>
      <a
        className="w-[36px] h-[36px] leading-[36px] rounded-[30px]
          bg-[#202020] relative my-1 flex items-center justify-center
          hover:text-[#FF304F] hover:translate-y-[-4px] transition-all duration-300 ease"
        href="#"
        target="_blank"
      >
        <LuYoutube size="25" />
      </a>
    </div>
  );
}
