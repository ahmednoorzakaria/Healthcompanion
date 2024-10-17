import '../css/component/chart.css';
import {
  LineChart,
  Line,
  XAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Brush,
} from "recharts";
import moment from 'moment'; // Ensure moment.js is installed

// Custom Tooltip component
const CustomTooltip = ({ active, payload, label }) => {
  if (active && payload && payload.length) {
    return (
      <div className="custom-tooltip">
        <p className="label">{`${moment(label).format('MMM Do YYYY')}`}</p>
        <p className="intro">{`Mood: ${payload[0].value}`}</p>
        {payload[1] && <p>{`Energy: ${payload[1].value}`}</p>}
      </div>
    );
  }
  return null;
};

function Chart({ title, data, moodKey, energyKey, grid }) {
  return (
    <div className="chart">
      <h3 className="chartTitle">{title}</h3>
      <ResponsiveContainer width="100%" aspect={4 / 1}>
        <LineChart data={data}>
          {/* Formatting dates on XAxis */}
          <XAxis dataKey="date" stroke="#5550bd" tickFormatter={(date) => moment(date).format('MMM Do')} />
          
          {/* Mood Line with dynamic colors */}
          <Line 
            type="monotone" 
            dataKey={moodKey} 
            stroke={(dataPoint) => dataPoint.mood > 5 ? "#82ca9d" : "#ff6b6b"} 
            dot={false} 
          />

          {/* Optional energy line */}
          {energyKey && (
            <Line 
              type="monotone" 
              dataKey={energyKey} 
              stroke="#8884d8" 
              dot={false} 
            />
          )}

          {/* Custom tooltip */}
          <Tooltip content={<CustomTooltip />} />

          {/* Grid */}
          {grid && <CartesianGrid stroke="#e0dfdf" strokeDasharray="5 5" />}

          {/* Zoom with Brush */}
          <Brush dataKey="date" height={30} stroke="#8884d8" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default Chart;
