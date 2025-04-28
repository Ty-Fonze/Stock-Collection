const { app, BrowserWindow, ipcMain } = require("electron");
const path = require("path");

let mainWindow, controlWindow;

app.on("ready", () => {
  // Main Widget
  mainWindow = new BrowserWindow({
    width: 300,
    height: 400,
    frame: false,
    transparent: true,
    alwaysOnTop: true,
    resizable: false,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  });
  mainWindow.loadFile(path.join(__dirname, "src", "index.html"));

  // Control Widget
  console.log("Creating control widget...");
  controlWindow = new BrowserWindow({
    width: 200,
    height: 100,
    frame: false,
    transparent: true,
    alwaysOnTop: true,
    resizable: false,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  });

  controlWindow.loadFile(path.join(__dirname, "src", "control.html"))
    .then(() => {
      console.log("control.html loaded successfully!");
    })
    .catch((err) => {
      console.error("Failed to load control.html:", err);
    });

  controlWindow.setBounds({ x: 100, y: 100, width: 200, height: 100 }); // Set initial position
});

// Handle Dragging
ipcMain.on("move-window", (event, { deltaX, deltaY }) => {
  const focusedWindow = BrowserWindow.getFocusedWindow();
  if (focusedWindow) {
    const bounds = focusedWindow.getBounds();
    focusedWindow.setBounds({
      x: bounds.x + deltaX,
      y: bounds.y + deltaY,
      width: bounds.width,
      height: bounds.height,
    });
  }
});

// Handle Close Button
ipcMain.on("close-app", () => {
  if (mainWindow) mainWindow.close();
  if (controlWindow) controlWindow.close();
  app.quit();
});