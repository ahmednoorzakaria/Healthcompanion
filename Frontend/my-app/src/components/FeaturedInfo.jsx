import '../css/component/featuredInfo.css';
import { ArrowUpward, ArrowDownward } from "@material-ui/icons";
import React from 'react';

function FeaturedInfo({ currentMood, lastJournalEntry, nextSteps }) {
  return (
    <div className="featured">
      {/* Current Mood Section */}
      <div className="featuredItem">
        <span className="featuredTitle">Current Mood</span>
        <div className="featuredMoneyContainer">
          <span className="featuredMoney">{currentMood || "Unknown"}</span>
          {currentMood === "Happy" ? (
            <ArrowUpward className="featuredIcon positive" />
          ) : (
            <ArrowDownward className="featuredIcon negative" />
          )}
        </div>
        <span className="featuredSub">Based on your last mood log</span>
      </div>

      {/* Last Journal Entry */}
      <div className="featuredItem">
        <span className="featuredTitle">Last Journal Entry</span>
        <div className="featuredMoneyContainer">
          <span className="featuredMoney">{lastJournalEntry || "No entries yet"}</span>
        </div>
        <span className="featuredSub">Reflecting your thoughts</span>
      </div>

      {/* Suggested Next Steps */}
      <div className="featuredItem">
        <span className="featuredTitle">Suggested Next Steps</span>
        <div className="featuredMoneyContainer">
          <span className="featuredMoney">{nextSteps || "No suggestions at this time"}</span>
        </div>
        <span className="featuredSub">Tailored actions for your well-being</span>
      </div>
    </div>
  );
}

export default FeaturedInfo;
