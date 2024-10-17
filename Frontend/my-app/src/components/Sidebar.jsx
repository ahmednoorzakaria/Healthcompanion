import '../css/component/sidebar.css';
import {
  LineStyle,
  Mood,
  EmojiEmotions,
  Notes,
  BarChart,
  Insights,
  Feedback,
  Report,
  ChatBubbleOutline,
  Journal,
} from "@material-ui/icons";
import { Link } from "react-router-dom";

function Sidebar() {
  return (
    <div className="sidebar">
      <div className="sidebarWrapper">
        
        {/* Dashboard Section */}
        <div className="sidebarMenu">
          <h3 className="sidebarTitle">Dashboard</h3>
          <ul className="sidebarList">
            <Link to="/" className="link">
              <li className="sidebarListItem active">
                <LineStyle className="sidebarIcon" />
                Overview
              </li>
            </Link>
            <li className="sidebarListItem">
              <Mood className="sidebarIcon" />
              Mood Tracker
            </li>
            <li className="sidebarListItem">
              <EmojiEmotions className="sidebarIcon" />
              Emotion State
            </li>
          </ul>
        </div>

        {/* Quick Access Menu */}
        <div className="sidebarMenu">
          <h3 className="sidebarTitle">Quick Access</h3>
          <ul className="sidebarList">
            <Link to="/journal" className="link">
              <li className="sidebarListItem">
                <Notes className="sidebarIcon" />
                Journal Entry
              </li>
            </Link>
            <li className="sidebarListItem">
              <Insights className="sidebarIcon" />
              Mood Insights
            </li>
            <li className="sidebarListItem">
              <BarChart className="sidebarIcon" />
              Mood Trends
            </li>
          </ul>
        </div>

        {/* Support Section */}
        <div className="sidebarMenu">
          <h3 className="sidebarTitle">Support</h3>
          <ul className="sidebarList">
            <li className="sidebarListItem">
              <Feedback className="sidebarIcon" />
              Feedback
            </li>
            <li className="sidebarListItem">
              <ChatBubbleOutline className="sidebarIcon" />
              Messages
            </li>
          </ul>
        </div>

        {/* Additional Options */}
        <div className="sidebarMenu">
          <h3 className="sidebarTitle">Other</h3>
          <ul className="sidebarList">
            <li className="sidebarListItem">
              <Journal className="sidebarIcon" />
              My Journal
            </li>
            <li className="sidebarListItem">
              <Report className="sidebarIcon" />
              Reports
            </li>
          </ul>
        </div>

      </div>
    </div>
  );
}

export default Sidebar;
