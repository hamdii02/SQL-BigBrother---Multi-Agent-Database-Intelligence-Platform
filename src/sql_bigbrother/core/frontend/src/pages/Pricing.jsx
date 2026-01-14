import React from "react";

import Pricing from "../components/Plans/Pricing";
import CheckCircleSVG from "../components/SVG/CheckCircleSVG";
import { LuLock, LuShieldCheck, LuUnlink } from "react-icons/lu";


const PricingPage = () => {
    return (
        <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 text-white">
            <div className="pricing-title flex items-center flex-col text-center py-16 px-8">
                <h1 className="text-5xl font-bold mb-4">
                    SQL <span className="text-blue-400">BigBrother</span> Plans
                </h1>
                <p className="text-xl text-white/70 max-w-2xl">Choose the perfect plan for your SQL analysis needs</p>
            </div>

            <div className="pricing-plan px-6 pb-16 flex flex-col items-center justify-center">
                <Pricing />

                <div className="max-w-4xl mx-auto text-center mt-8 space-y-2 text-white/60">
                    <p className="text-sm">*Free users have a limit of 10 queries per day, refreshed daily.</p>
                    <p className="text-sm">**Enterprise plans include dedicated support and custom integrations.</p>
                </div>
            </div>

            <div className="pricing-payments py-16 px-8">
                <div className="payments-pill flex flex-wrap items-center justify-center gap-6 max-w-4xl mx-auto">
                    <div className="text-white/80 flex items-center text-sm font-medium">
                        <CheckCircleSVG />
                        <div className="flex-1 text-center px-3">Advanced SQL Analytics</div>
                    </div>
                    <div className="text-white/80 flex items-center text-sm font-medium">
                        <CheckCircleSVG />
                        <div className="flex-1 text-center px-3">Real-time Query Optimization</div>
                    </div>
                    <div className="text-white/80 flex items-center text-sm font-medium">
                        <CheckCircleSVG />
                        <div className="flex-1 text-center px-3">Enterprise Security</div>
                    </div>
                </div>

                <div className="payments-info flex justify-center p-8">
                    <div
                        className="payment-info-section border-r border-[#4e5152]
                    flex flex-col justify-start px-8 max-w-[20rem]"
                    >
                        <div className="payment-info-header flex items-center font-medium mb-2 text-[0.825rem] gap-2 text-[#A1A8AA]">
                            <LuShieldCheck size={20} />
                            <span>Payment Methods</span>
                        </div>
                        <div className="payment-info-body flex gap-1 text-[0.8rem]">
                            <img className="max-w-12 max-h-8 mt-1" src="/visa.png" />
                            <img className="max-w-12 max-h-8 mt-1" src="/mastercard.png" />
                            <img className="max-w-12 max-h-8 mt-1" src="/amex.png" />
                        </div>
                    </div>

                    <div
                        className="payment-info-section border-r border-[#4e5152]
                    flex flex-col justify-start px-8 max-w-[20rem]"
                    >
                        <div className="payment-info-header flex items-center font-medium mb-2 text-[0.825rem] gap-2 text-[#A1A8AA]">
                            <LuUnlink size={19} />
                            <span>Cancel Anytime</span>
                        </div>
                        <div className="payment-info-body flex gap-1 text-[0.7rem] text-[#A1A8AA]">
                            <p>No tie-ins, just simple plans which you can cancel at any time.</p>
                        </div>
                    </div>

                    <div
                        className="payment-info-section]
                    flex flex-col justify-start px-8 max-w-[20rem]"
                    >
                        <div className="payment-info-header flex items-center font-medium mb-2 text-[0.825rem] gap-2 text-[#A1A8AA]">
                            <LuLock size={19} />
                            <span>Secure Payment</span>
                        </div>
                        <div className="payment-info-body flex gap-1 text-[0.7rem] text-[#A1A8AA]">
                            <p>Transactions are encrypted and secured.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default PricingPage;