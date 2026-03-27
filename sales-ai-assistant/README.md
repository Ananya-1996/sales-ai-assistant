# 🤖 Sales AI Assistant (Cloud Run + GenAI + Calendar Integration)

A production-ready AI-powered Sales Assistant that intelligently schedules meetings based on real-time weather conditions, priority detection, and smart decision logic.

---

## 🚀 Live Demo
👉 https://weather-agent-593321241935.us-central1.run.app/

---

## 🧠 Features

### 💬 ChatGPT-style UI
- Modern conversational interface
- Auto-resizing input box
- Typing indicator
- Smooth scrolling UX

### 🌤 Real-Time Weather Intelligence
- Integrated with OpenWeather API
- Fetches live temperature & wind data
- Dynamic decision making

### 🧠 Smart Decision Engine
- Suggests **ONLINE vs OFFLINE meetings**
- Based on weather conditions:
  - Extreme heat / cold → ONLINE
  - Pleasant weather → OFFLINE

### 📅 Smart Scheduling
- Business-hour aware scheduling
- Avoids late-night meetings
- Auto-adjusts to next valid slot

### 📊 Priority Detection
- Detects urgency from query:
  - 🔥 VIP → High priority
  - ⚡ Client → Medium
  - 🟢 Default → Normal

### 📍 NLP-based City Detection
- Extracts location from natural queries
- Works even with incomplete inputs

### 📅 Google Calendar Integration
- Automatically creates events
- Generates shareable event link
- Uses secure Cloud Run authentication

---

## 🏗️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** FastAPI (Python)
- **AI Logic:** Custom NLP + Rule Engine
- **APIs:**
  - OpenWeather API
  - Google Calendar API
- **Cloud:** Google Cloud Run

---

## 📁 Project Structure
