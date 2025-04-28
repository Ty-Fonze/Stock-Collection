import React, { useState } from "react";
import Draggable from "react-draggable"; // Import draggable library
import "./animations.css"; // Import CSS for animations

const DynamicWidgets = () => {
  const [mentorResponses, setMentorResponses] = useState([]);
  const [userQuery, setUserQuery] = useState("");
  const [isBreathing, setIsBreathing] = useState(false); // State for breathing animation
  const [isGlowing, setIsGlowing] = useState(false); // State for glowing animation

  const handleQuerySubmit = (e) => {
    e.preventDefault();
    if (userQuery.trim() !== "") {
      setIsBreathing(false); // Stop breathing animation

      // Simulate mentor output with a delay
      setIsGlowing(true); // Start glowing animation
      const newResponse = `Mentor says: "${userQuery}"`; // Placeholder for actual AI logic
      setTimeout(() => {
        setMentorResponses([...mentorResponses, newResponse]);
        setIsGlowing(false); // Stop glowing animation after response
      }, 1000);

      setUserQuery(""); // Clear input field
    }
  };

  const handleInputChange = (e) => {
    setUserQuery(e.target.value);
    setIsBreathing(e.target.value.trim() !== ""); // Start breathing animation while typing
  };

  return (
    <Draggable>
      <div
        style={{
          position: "absolute",
          backgroundColor: "transparent", // Fully transparent background
          padding: "10px",
          borderRadius: "10px",
          display: "inline-block",
          textAlign: "center",
          cursor: "move", // Make it clear it's draggable
        }}
      >
        {/* Logo with dynamic animations */}
        <div
          className={`logo-container ${
            isBreathing ? "breathing" : ""
          } ${isGlowing ? "glowing" : ""}`}
        >
          <img
            src="/assets/adeptus_mechanicus_logo.png"
            alt="AI Mentor Logo"
            style={{ width: "150px", height: "150px", marginBottom: "10px" }}
          />
        </div>
        {/* Input Field and Submit Button */}
        <form onSubmit={handleQuerySubmit}>
          <input
            type="text"
            value={userQuery}
            onChange={handleInputChange}
            placeholder="Ask your Mentor..."
            style={{
              width: "80%",
              padding: "10px",
              borderRadius: "5px",
              border: "1px solid rgba(255, 255, 255, 0.5)", // Semi-transparent border
              backgroundColor: "#333", // Solid background color
              color: "white", // White text color
              marginBottom: "10px",
            }}
          />
          <button
            type="submit"
            style={{
              padding: "10px 20px",
              border: "none",
              borderRadius: "5px",
              backgroundColor: "rgba(85, 85, 85, 0.5)", // Semi-transparent button background
              color: "white",
              cursor: "pointer",
              opacity: "0.9", // Slight transparency
            }}
          >
            Submit
          </button>
        </form>
      </div>
    </Draggable>
  );
};

export default DynamicWidgets;