const { ipcRenderer } = require("electron");

document.addEventListener("DOMContentLoaded", () => {
  // Handle Dragging
  const controlDragHandle = document.getElementById("control-drag-handle");

  let isDraggingControl = false;
  let startXControl, startYControl;

  if (controlDragHandle) {
    // Start dragging
    controlDragHandle.addEventListener("mousedown", (e) => {
      isDraggingControl = true;
      startXControl = e.screenX;
      startYControl = e.screenY;
      document.body.style.userSelect = "none"; // Prevent text selection while dragging
      document.body.style.cursor = "grabbing"; // Visual cue for dragging
    });

    // Dragging
    document.addEventListener("mousemove", (e) => {
      if (!isDraggingControl) return;

      const deltaX = e.screenX - startXControl;
      const deltaY = e.screenY - startYControl;

      // Send movement to the main process
      ipcRenderer.send("move-window", { deltaX, deltaY });

      startXControl = e.screenX;
      startYControl = e.screenY;
    });

    // Stop dragging
    document.addEventListener("mouseup", () => {
      isDraggingControl = false;
      document.body.style.userSelect = ""; // Re-enable text selection
      document.body.style.cursor = ""; // Reset cursor style
    });
  }

  // Handle Time Display
  const currentTimeElement = document.getElementById("current-time");

  if (currentTimeElement) {
    setInterval(() => {
      const now = new Date(); // Get the current date and time
      const timeString = now.toLocaleTimeString(); // Format the time as HH:MM:SS
      currentTimeElement.textContent = timeString; // Update the time display
    }, 1000); // Update every second
  }

  // Handle Close Button
  const closeButton = document.getElementById("close-button");

  if (closeButton) {
    closeButton.addEventListener("click", () => {
      ipcRenderer.send("close-app"); // Send a signal to the main process to close the app
    });
  }
});