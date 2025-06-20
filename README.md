# 🧠 Saluto AI Bot

This is a lightweight AI-powered web application that answers user questions and generates concise summaries using **CrewAI agents**. Built with **Flask**, this app delivers interactive, accurate responses in real-time via a clean and responsive web interface—ideal for learners, developers, and anyone exploring multi-agent systems with GenAI.

---

## 🧰 Project Description

This project integrates **Flask** for the web interface and **CrewAI** for orchestrating multi-step reasoning using agents. It allows a user to:

- Ask any question
- Get a full-length detailed answer from one AI agent
- Get a summarized version (in bullet points) from another AI agent
- View multiple past responses in a chat-like history layout

The app uses **Ngrok** for public tunneling during development so it can be accessed and shared remotely.

---

## ✨ Features

- 💬 Asks anything—natural language query input  
- 🧠 Powered by CrewAI with multiple task agents  
- 📄 Generates detailed answers and short summaries  
- 🕓 Maintains full response history on the same page  
- 🌐 Hosted locally with Ngrok for live preview  

---

## 📁 Project Structure

```bash
Flask-CrewAI-Chat/
├── app.py                # Main Flask app with agent integration
├── templates/            # HTML templates (inlined with render_template_string)
├── static/               # (Optional) CSS/JS if separated later
├── requirements.txt      # Python dependencies
```
---

## ⚙️ Requirements

- 🐍 Python 3.8+
- 🌐 Flask
- 🛠 pyngrok
- 🧠 CrewAI

---

## 📦 Installation Guide
1. Clone the Repository
```bash
git clone https://github.com/yourusername/Flask-CrewAI-Chat.git
```
```bash
cd Flask-CrewAI-Chat
```
2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
```
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
Make sure you have access to OpenAI API and CrewAI (from PyPI or GitHub).

---

## 🚀 Running the App
```bash
python app.py
```
Once running, Ngrok will expose the app to the internet, and you’ll see a public link in your terminal:
```bash
🔗 Public URL: https://xyz123.ngrok.io
```
Open the link in your browser to interact with the AI chat app.

---

## 🧠 How It Works
- You submit a query using the web form
- Agent 1 (Answer Expert) generates a full answer
- Agent 2 (Summarizer) takes that and produces bullet points
- Both results are displayed below the question, stacked in history
- Agents are orchestrated using the Crew object in sequential mode.

---

## 💡 Use Cases
- 🔍 Quick research or info lookup
- 📚 Educational tool for AI and NLP learning
- 🧪 Demo for CrewAI and multi-agent reasoning
- 📢 FAQ or support chatbot for projects

---

## 🛠 Troubleshooting
### 🔑 OpenAI API Key error
→ Ensure your environment variable OPENAI_API_KEY is set correctly.

### 🌐 Ngrok token error
→ Run ngrok config add-authtoken YOUR_TOKEN from the terminal once before use.

### 🐍 ModuleNotFoundError
→ Recheck if crewai, flask, and pyngrok are installed properly.

---

## 📜 License

This project is licensed under the MIT License.

---
