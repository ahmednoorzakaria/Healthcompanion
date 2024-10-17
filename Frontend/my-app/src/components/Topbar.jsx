import React from "react";
import '../css/component/topbar.css';
import { NotificationsNone, Mood, Settings } from "@material-ui/icons";

function Topbar() {
  return (
    <div className="topbar">
      <div className="topbarWrapper">
        
        {/* Left Side: Logo */}
        <div className="topLeft">
          <span className="logo">MoodTracker</span>
        </div>
        
        {/* Right Side: Notifications and Settings */}
        <div className="topRight">
          
          {/* Notification Icon for Mood Alerts */}
          <div className="topbarIconContainer">
            <NotificationsNone />
            <span className="topIconBadge">3</span>
          </div>
          
          {/* Mood Icon to Display Current Mood */}
          <div className="topbarIconContainer">
            <Mood />
            <span className="topIconBadge">Happy</span>
          </div>
          
          {/* Settings Icon */}
          <div className="topbarIconContainer">
            <Settings />
          </div>
          
          {/* Avatar */}
          <img
            src="https://images.pexels.com/photos/1526814/pexels-photo-1526814.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500"
            alt="User Avatar"
            className="topAvatar"
          />
        </div>
      </div>
    </div>
  );
}

export default Topbar;
