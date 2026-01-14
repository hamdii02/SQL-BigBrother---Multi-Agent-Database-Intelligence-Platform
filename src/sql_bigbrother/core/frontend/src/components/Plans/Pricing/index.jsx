import React from "react";
import CheckSVG from "../../SVG/CheckSVG";
import CrossSVG from "../../SVG/CrossSVG";
import pricing from "../../../data/pricing.json";

const  Pricing = () => {
    return (
        <>
            <div
                className="pricing-cards max-w-[1200px] w-fit relative gap-4
                    flex flex-row items-stretch justify-center rounded-[1rem] my-[4rem]"
            >
                {/* Free */}
                <div
                    className="pricing-card free rounded-2xl w-full max-w-[24rem] bg-white/10 backdrop-blur-md border border-white/20
                        flex flex-col relative overflow-hidden hover:scale-105 transition-transform duration-300"
                >
                    <div className="pricing-image w-full h-[8rem] overflow-hidden relative">
                        <img
                            alt="free banner"
                            loading="lazy"
                            decoding="async"
                            data-nimg="fill"
                            sizes="(max-width: 767px) 0px, (max-width: 991px) 300px, 400px"
                            srcSet="https://imgix.uppbeat.io/images/pricing-card-free-v4.jpg?w=16&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 16w, https://imgix.uppbeat.io/images/pricing-card-free-v4.jpg?w=32&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 32w, https://imgix.uppbeat.io/images/pricing-card-free-v4.jpg?w=48&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 48w, https://imgix.uppbeat.io/images/pricing-card-free-v4.jpg?w=64&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 64w, https://imgix.uppbeat.io/images/pricing-card-free-v4.jpg?w=96&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 96w, https://imgix.uppbeat.io/images/pricing-card-free-v4.jpg?w=128&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 128w, https://imgix.uppbeat.io/images/pricing-card-free-v4.jpg?w=256&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 256w, https://imgix.uppbeat.io/images/pricing-card-free-v4.jpg?w=384&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 384w, https://imgix.uppbeat.io/images/pricing-card-free-v4.jpg?w=640&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 640w, https://imgix.uppbeat.io/images/pricing-card-free-v4.jpg?w=750&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 750w, https://imgix.uppbeat.io/images/pricing-card-free-v4.jpg?w=828&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 828w, https://imgix.uppbeat.io/images/pricing-card-free-v4.jpg?w=1080&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 1080w, https://imgix.uppbeat.io/images/pricing-card-free-v4.jpg?w=1200&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 1200w, https://imgix.uppbeat.io/images/pricing-card-free-v4.jpg?w=1920&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 1920w, https://imgix.uppbeat.io/images/pricing-card-free-v4.jpg?w=2048&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 2048w, https://imgix.uppbeat.io/images/pricing-card-free-v4.jpg?w=3840&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 3840w"
                            src="https://imgix.uppbeat.io/images/pricing-card-free-v4.jpg?w=3840&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress"
                            // style={"position: absolute; height: 100%; width: 100%; inset: 0px; color: transparent;"}
                        ></img>
                    </div>

                    <div className="pricing-body p-[2rem] relative">
                        <span className="top-details flex flex-col items-center justify-center">
                            <span className="max-w-full">
                                <h2 className="text-[2rem] text-center font-bold mb-3">{pricing["free"]?.label}</h2>
                                <p className="text-[0.875rem] text-center block mb-[1.8em] text-[#ccc]">
                                    {pricing["free"]?.desc}
                                </p>
                            </span>

                            <div className="plan-price flex items-baseline whitespace-nowrap relative mb-8 text-[#fff]">
                                <span className="text-[2rem]">$</span>
                                <span className="flex">
                                    <div className="text-[4rem]">{pricing["free"]?.price?.integer}</div>
                                    <div className="text-[2rem] mt-3">{pricing["free"]?.price?.decimal}</div>
                                </span>
                            </div>
                        </span>

                        <button
                            className="btn-free w-full rounded-xl mb-10 bg-[#2DCAE9] h-[2.5rem] cursor-pointer transition-opacity duration-200
                                min-w-[2.5rem] py-3 outline-none border border-transparent flex items-center justify-center"
                        >
                            <span className="text-center text-[0.875rem] truncate text-[#0b0c0c] font-extralight">
                                Start now
                            </span>
                        </button>

                        <ul className="block">
                            {pricing["free"]?.benefits?.map((bullet, index) => {
                                return (
                                    <li key={index} className="flex mb-3 items-center gap-3">
                                        {bullet.isChecked ? <CheckSVG /> : <CrossSVG />}
                                        <div className="text-[0.875rem] mt-1">{bullet.content}</div>
                                    </li>
                                );
                            })}
                        </ul>
                    </div>
                </div>

                {/* Premium */}
                <div
                    className="pricing-card premium rounded-2xl w-full max-w-[24rem] bg-gradient-to-b from-blue-600/20 to-purple-600/20 backdrop-blur-md border-2 border-blue-400/30
                        flex flex-col relative hover:scale-105 transition-transform duration-300 shadow-2xl"
                >
                    <div className="pricing-tag text-[0.8rem] text-[#fff] py-4 px-3">Popular with reseachers</div>
                    <div className="pricing-image w-full h-[8rem] overflow-hidden relative rounded-t-[0.75rem]">
                        <img
                            alt="premium banner"
                            loading="lazy"
                            decoding="async"
                            datanimg="fill"
                            sizes="(max-width: 767px) 0px, (max-width: 991px) 300px, 400px"
                            srcSet="https://imgix.uppbeat.io/images/pricing-card-premium-v4.jpg?w=16&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 16w, https://imgix.uppbeat.io/images/pricing-card-premium-v4.jpg?w=32&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 32w, https://imgix.uppbeat.io/images/pricing-card-premium-v4.jpg?w=48&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 48w, https://imgix.uppbeat.io/images/pricing-card-premium-v4.jpg?w=64&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 64w, https://imgix.uppbeat.io/images/pricing-card-premium-v4.jpg?w=96&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 96w, https://imgix.uppbeat.io/images/pricing-card-premium-v4.jpg?w=128&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 128w, https://imgix.uppbeat.io/images/pricing-card-premium-v4.jpg?w=256&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 256w, https://imgix.uppbeat.io/images/pricing-card-premium-v4.jpg?w=384&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 384w, https://imgix.uppbeat.io/images/pricing-card-premium-v4.jpg?w=640&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 640w, https://imgix.uppbeat.io/images/pricing-card-premium-v4.jpg?w=750&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 750w, https://imgix.uppbeat.io/images/pricing-card-premium-v4.jpg?w=828&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 828w, https://imgix.uppbeat.io/images/pricing-card-premium-v4.jpg?w=1080&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 1080w, https://imgix.uppbeat.io/images/pricing-card-premium-v4.jpg?w=1200&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 1200w, https://imgix.uppbeat.io/images/pricing-card-premium-v4.jpg?w=1920&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 1920w, https://imgix.uppbeat.io/images/pricing-card-premium-v4.jpg?w=2048&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 2048w, https://imgix.uppbeat.io/images/pricing-card-premium-v4.jpg?w=3840&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 3840w"
                            src="https://imgix.uppbeat.io/images/pricing-card-premium-v4.jpg?w=3840&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress"
                        />
                    </div>

                    <div className="pricing-body p-[2rem] relative">
                        <span className="top-details flex flex-col items-center justify-center">
                            <span className="max-w-full">
                                <h2 className="text-[2rem] text-center font-bold mb-3 flex flex-row justify-center gap-2 items-center">
                                    {pricing["premium"]?.label}
                                    <img
                                        alt="premium star"
                                        loading="lazy"
                                        width="33"
                                        height="33"
                                        decoding="async"
                                        datanimg="1"
                                        src="https://cdn.uppbeat.io/icons/static-icons/premium_star.svg"
                                    />
                                </h2>
                                <p className="text-[0.875rem] text-center block mb-[1.8em] text-[#ccc]">
                                    {pricing["premium"]?.desc}
                                </p>
                            </span>

                            <div className="plan-price flex items-baseline whitespace-nowrap relative mb-8 text-[#fff]">
                                <span className="text-[2rem]">$</span>
                                <span className="flex">
                                    <div className="text-[4rem]">{pricing["premium"]?.price?.integer}</div>
                                    <div className="text-[2rem] mt-3">{pricing["premium"]?.price?.decimal}</div>
                                </span>
                            </div>
                        </span>

                        <button
                            className="btn-premium w-full rounded-xl mb-10 bg-[#F23D75] h-[2.5rem] cursor-pointer transition-opacity duration-200
                                min-w-[2.5rem] py-3 outline-none border border-transparent flex items-center justify-center"
                        >
                            <span className="text-center text-[0.875rem] truncate text-[#0b0c0c] font-extralight">
                                Start now
                            </span>
                        </button>

                        <ul className="block">
                            {pricing["premium"]?.benefits?.map((bullet, index) => {
                                return (
                                    <li key={index} className="flex mb-3 items-center gap-3">
                                        {bullet.isChecked ? <CheckSVG /> : <CrossSVG />}
                                        <div className="text-[0.875rem] mt-1">{bullet.content}</div>
                                    </li>
                                );
                            })}
                        </ul>
                    </div>
                </div>

                {/* Business */}
                <div
                    className="pricing-card business rounded-2xl w-full max-w-[24rem] bg-white/10 backdrop-blur-md border border-white/20
                        flex flex-col relative overflow-hidden hover:scale-105 transition-transform duration-300"
                >
                    <div className="pricing-image w-full h-[8rem] overflow-hidden relative">
                        <img
                            alt="business banner"
                            loading="lazy"
                            decoding="async"
                            datanimg="fill"
                            sizes="(max-width: 767px) 0px, (max-width: 991px) 300px, 400px"
                            srcSet="https://imgix.uppbeat.io/images/pricing-card-business-v4.jpg?w=16&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 16w, https://imgix.uppbeat.io/images/pricing-card-business-v4.jpg?w=32&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 32w, https://imgix.uppbeat.io/images/pricing-card-business-v4.jpg?w=48&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 48w, https://imgix.uppbeat.io/images/pricing-card-business-v4.jpg?w=64&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 64w, https://imgix.uppbeat.io/images/pricing-card-business-v4.jpg?w=96&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 96w, https://imgix.uppbeat.io/images/pricing-card-business-v4.jpg?w=128&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 128w, https://imgix.uppbeat.io/images/pricing-card-business-v4.jpg?w=256&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 256w, https://imgix.uppbeat.io/images/pricing-card-business-v4.jpg?w=384&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 384w, https://imgix.uppbeat.io/images/pricing-card-business-v4.jpg?w=640&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 640w, https://imgix.uppbeat.io/images/pricing-card-business-v4.jpg?w=750&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 750w, https://imgix.uppbeat.io/images/pricing-card-business-v4.jpg?w=828&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 828w, https://imgix.uppbeat.io/images/pricing-card-business-v4.jpg?w=1080&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 1080w, https://imgix.uppbeat.io/images/pricing-card-business-v4.jpg?w=1200&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 1200w, https://imgix.uppbeat.io/images/pricing-card-business-v4.jpg?w=1920&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 1920w, https://imgix.uppbeat.io/images/pricing-card-business-v4.jpg?w=2048&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 2048w, https://imgix.uppbeat.io/images/pricing-card-business-v4.jpg?w=3840&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress 3840w"
                            src="https://imgix.uppbeat.io/images/pricing-card-business-v4.jpg?w=3840&amp;q=50&amp;fit=max&amp;auto=format%2Ccompress"
                        />
                    </div>

                    <div className="pricing-body p-[2rem] relative">
                        <span className="top-details flex flex-col items-center justify-center">
                            <span className="max-w-full">
                                <h2 className="text-[2rem] text-center font-bold mb-3">{pricing["business"]?.label}</h2>
                                <p className="text-[0.875rem] text-center block mb-[1.8em] text-[#ccc]">
                                    {pricing["business"]?.desc}
                                </p>
                            </span>

                            <div className="plan-price flex items-baseline whitespace-nowrap relative mb-8 text-[#fff]">
                                <span className="text-[2rem]">$</span>
                                <span className="flex">
                                    <div className="text-[4rem]">{pricing["business"]?.price?.integer}</div>
                                    <div className="text-[2rem] mt-3">{pricing["business"]?.price?.decimal}</div>
                                </span>
                            </div>
                        </span>

                        <button
                            className="btn-free w-full rounded-xl mb-10 bg-[#F0B62D] h-[2.5rem] cursor-pointer transition-opacity duration-200
                                min-w-[2.5rem] py-3 outline-none border border-transparent flex items-center justify-center"
                        >
                            <span className="text-center text-[0.875rem] truncate text-[#0b0c0c] font-extralight">
                                Start now
                            </span>
                        </button>
                        <h4 className="text-[1rem] text-[#fff] mb-4 leading-[1]">All the benefits of Premium, plus:</h4>

                        <ul className="block">
                            {pricing["business"]?.benefits?.map((bullet, index) => {
                                return (
                                    <li key={index} className="flex mb-3 items-center gap-3">
                                        {bullet.isChecked ? <CheckSVG /> : <CrossSVG />}
                                        <div className="text-[0.875rem] mt-1">{bullet.content}</div>
                                    </li>
                                );
                            })}
                        </ul>
                    </div>
                </div>
            </div>
        </>
    );
};

export default Pricing;