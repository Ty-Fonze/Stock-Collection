import React from "react";
import ReactDOM from "react-dom";
import DynamicWidgets from "./DynamicWidgets"; // Import the updated mentor widget
import "./index.css"; // Your global styles

ReactDOM.render(
  <React.StrictMode>
    <DynamicWidgets />
  </React.StrictMode>,
  document.getElementById("root")
);