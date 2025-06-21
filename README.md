# 📰 News Delivery Agent (No OpenAI)

A simple Python-based web application that fetches and filters news articles from NewsAPI based on user-defined interests, then displays them in a clean web interface using Flask.

---

## 🚀 Features

- Fetches real-time news using **NewsAPI**
- Filters articles based on keywords (your interests)
- Displays clean summaries on a local web page
- No OpenAI or paid APIs required — 100% free

---

## 📁 Project Structure

news_agent/
├── app.py # Main Flask application
├── .env # Stores your NewsAPI key
├── interests.txt # List of topics you care about
├── templates/
│ └── index.html # News web page template
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🧪 Requirements

Install the necessary packages:

```bash
pip install flask python-dotenv requests
🔐 Setup
Get a free NewsAPI key:
https://newsapi.org/register

Create a .env file in your project folder:

env
Copy
Edit
NEWS_API_KEY=your_newsapi_key_here
Add your topics of interest in interests.txt (one per line):

mathematica
Copy
Edit
AI
Cybersecurity
Space
Python
▶️ Running the App
bash
Copy
Edit
python app.py
Visit: http://localhost:5000

🌟 Future Enhancements
Email daily top news to users

Add dark/light mode to the UI

Integrate text-to-speech for each article

Host as a public website or Telegram bot

📸 Screenshot
(add your screenshot here)

🧑‍💻 Built With
Python 3

Flask

HTML + CSS

NewsAPI.org

📬 Contact
Archana – archanasrprajna@gmail.com
Project created as part of the Mini Hackathon (AI Agents Workshop).