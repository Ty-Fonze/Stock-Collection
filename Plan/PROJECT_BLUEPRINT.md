# **Project Blueprint**

## **Overview**
This project consists of a trading assistant system with both web-based and desktop-based frontends, supported by an interactive backend. Archived components from older versions are stored for reference or potential reuse.

---

## **Active Components**

### **1. Frontend**

#### **AI_Battle_Center**
- **Purpose**: A web-based trading dashboard with movable widgets.
- **Framework**: React.
- **Key Features**:
  - Uses React and React Grid Layout for dynamic and interactive UI components.
  - Development tools include Webpack and Babel for building the app.
- **Relevant File**: `package.json` in the AI_Battle_Center folder.

#### **my-desktop-widgets**
- **Purpose**: A desktop widget application for trading insights.
- **Framework**: Electron.
- **Key Features**:
  - Desktop application for Windows, Mac, and Linux.
  - Built with Electron and packaged using `electron-builder`.
- **Relevant File**: `package.json` in the my-desktop-widgets folder.

---

### **2. Backend**

#### **AI_Battle_Center Backend**
- **Purpose**: Provides an interactive trading assistant dashboard.
- **Framework**: Dash (built on Flask).
- **Key Features**:
  - Uses the `DynamicWidgets` component for rendering interactive widgets.
  - Runs as a Dash application with a simple, interactive layout.
- **Relevant File**: `app.py` in the AI_Battle_Center folder.

---

## **Archived Components**

### **1. Old Stock Collection**
- **Purpose**: Contains older or unused frontend components for reference.
- **Contents**:
  - `package.json` from the users folder (legacy React-based frontend).

### **2. Environment Folder**
- **Purpose**: Contains older backend components for reference.
- **Contents**:
  - `app.py` with a simple Flask API returning static JSON data.

---

## **Next Steps**
1. **Testing**:
   - Ensure both frontends (React and Electron) integrate well with the active backend.
   - Conduct platform-specific testing for the Electron app.
2. **Deployment**:
   - Deploy the Dash app for the web-based assistant.
   - Package and distribute the Electron app for desktop users.
3. **Documentation**:
   - Write clear setup and usage instructions for both components.
   - Include contribution guidelines for future development.
4. **Enhancements**:
   - Add more functionality to the `DynamicWidgets` component in the Dash app.
   - Explore additional trading insights or widgets for both frontends.

---

## **Folder Structure**
```
Project Root/
│
├── AI_Battle_Center/
│   ├── app.py             # Dash backend for the trading assistant.
│   ├── package.json       # Web-based frontend setup.
│   └── ... (other files)
│
├── my-desktop-widgets/
│   ├── package.json       # Electron desktop app setup.
│   └── ... (other files)
│
├── Old Stock Collection/
│   ├── package.json       # Archived legacy files.
│   └── ... (other files)
│
└── Environment/
    ├── app.py             # Archived Flask backend.
    └── ... (other files)
```

---

## **Author**
- **Ty-Fonze**