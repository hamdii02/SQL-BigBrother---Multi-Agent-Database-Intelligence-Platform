import classNames from "classnames";
import React, { useEffect } from "react";
import { useState } from "react";

const FAQs = () => {
   const [activeTab, setActiveTab] = useState(0);
   
   return (
      <>
         <div
            onClick={() => {
               setActiveTab(0);
            }}
            className={classNames({
               "collapse collapse-plus bg-[#232525] rounded-b-none px-4": true,
               active: activeTab === 0,
            })}
         >
            <input type="radio" name="my-accordion-3" defaultChecked />
            <div className="collapse-title text-lg font-medium my-4">
               Where can I use Uppbeat music & sound effects?
            </div>
            <div className="collapse-content text-sm text-[#BEC6C6]">
               <p className="mb-5">
                  Uppbeat is for creators. You can use our music & sound effects in content you're sharing on YouTube,
                  social media, live streams, websites and anywhere online!
               </p>
               <p className="mb-5">
                  You can use Uppbeat for monetized, sponsored, affiliated and pay-to-access content such as videos on
                  Patreon. If you're looking to use Uppbeat music or sound effects in paid advertising or for a business
                  or organization, Uppbeat Business is the plan you'll need.
               </p>
            </div>
         </div>
         <div
            onClick={() => {
               setActiveTab(1);
            }}
            className={classNames({
               "collapse collapse-plus bg-[#232525] rounded-none px-4": true,
               active: activeTab === 1,
            })}
         >
            <input type="radio" name="my-accordion-3" />
            <div className="collapse-title text-lg font-medium my-4">Which plan is best for me?</div>
            <div className="collapse-content text-sm text-[#BEC6C6]">
               <p className="mb-5">
                  <strong>Uppbeat Free</strong> is great if you're getting started as a creator. It's for individual
                  creators, provides access to 30% of the catalog and gives you an allowance of 3 downloads which tops
                  up by 1 every month.
               </p>
               <p className="mb-5">
                  <strong>Uppbeat Premium</strong> is for individuals and ‘micro organizations’ (5 employees or less).
                  It offers unlimited downloads, access to all premium tracks and sound effects, as well as copyright
                  whitelisting for up to 3 YouTube channels. You'll also enjoy ad-free browsing!
               </p>
               <p className="mb-5">
                  <strong>Uppbeat Business</strong> caters for businesses of any size and includes clearance for online
                  paid advertising and client content. It includes all the features of Premium plus whitelisting for up
                  to 10 YouTube channels.
               </p>
            </div>
         </div>
         <div
            onClick={() => {
               setActiveTab(2);
            }}
            className={classNames({
               "collapse collapse-plus bg-[#232525] rounded-none px-4": true,
               active: activeTab === 2,
            })}
         >
            <input type="radio" name="my-accordion-3" />
            <div className="collapse-title text-lg font-medium my-4">Is the music copyright free?</div>
            <div className="collapse-content text-sm text-[#BEC6C6]">
               <p className="mb-4">
                  Yes! You won’t have any copyright issues when using Uppbeat music correctly. If you’re a free user,
                  this simply means including Uppbeat Credits in your video descriptions, and if you’re a Premium or
                  Business subscriber you can whitelist your channels to make life even easier!
               </p>
            </div>
         </div>
         <div
            onClick={() => {
               setActiveTab(3);
            }}
            className={classNames({
               "collapse collapse-plus bg-[#232525] rounded-t-none px-4": true,
               active: activeTab === 3,
            })}
         >
            <input type="radio" name="my-accordion-3" />
            <div className="collapse-title text-lg font-medium my-4">How do artists get paid?</div>
            <div className="collapse-content text-sm text-[#BEC6C6]">
               <p className="mb-4">
                  Everytime you download our artists’ music, whether that’s for free or with an Uppbeat Premium account,
                  we pay them from a pool of Uppbeat Premium subscriptions and other revenue.
               </p>
               <p className="mb-4">
                  Artists are the beating heart of Uppbeat, and we’re committed to providing a great platform for them.
                  That’s why all of our artists also keep total control and ownership of their music.
               </p>
            </div>
         </div>
      </>
   );
};

export default FAQs;