const { ipcRenderer } = require("electron");

document.addEventListener("DOMContentLoaded", () => {
  const dragHandle = document.getElementById("drag-handle");

  let isDragging = false;
  let startX, startY;

  // Start dragging
  dragHandle.addEventListener("mousedown", (e) => {
    isDragging = true;
    startX = e.screenX;
    startY = e.screenY;
    document.body.style.userSelect = "none"; // Prevent text selection while dragging
  });

  // Dragging
  document.addEventListener("mousemove", (e) => {
    if (!isDragging) return;

    const deltaX = e.screenX - startX;
    const deltaY = e.screenY - startY;

    // Send movement to the main process
    ipcRenderer.send("move-window", { deltaX, deltaY });

    startX = e.screenX;
    startY = e.screenY;
  });

  // Stop dragging
  document.addEventListener("mouseup", () => {
    isDragging = false;
    document.body.style.userSelect = ""; // Re-enable text selection
  });
});