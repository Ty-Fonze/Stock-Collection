import React from "react";
import GridLayout from "react-grid-layout";
import "react-grid-layout/css/styles.css";

const Dashboard = () => {
  const layout = [
    { i: "tradingView", x: 0, y: 0, w: 6, h: 4 },
    { i: "plotlyChart", x: 6, y: 0, w: 6, h: 4 },
    { i: "newsFeed", x: 0, y: 4, w: 12, h: 4 }
  ];

  return (
    <GridLayout
      className="layout"
      layout={layout}
      cols={12}
      rowHeight={30}
      width={1200}
      draggableHandle=".widget-header"
    >
      <div key="tradingView" className="widget">
        <div className="widget-header">Live Market Data</div>
        <iframe
          src="https://s.tradingview.com/embed-widget/mini-symbol-overview/?locale=en&symbol=SPY&interval=D&theme=dark"
          style={{ width: "100%", height: "100%" }}
        />
      </div>
      <div key="plotlyChart" className="widget">
        <div className="widget-header">Technical Analysis</div>
        {/* Plotly chart would go here */}
      </div>
      <div key="newsFeed" className="widget">
        <div className="widget-header">Real-Time News Alerts</div>
        {/* News feed component would go here */}
      </div>
    </GridLayout>
  );
};

export default Dashboard;