
# 🤖 AI Financial Advisor and Web Researcher

An **AI-powered system** for **financial advising** and **web research**, utilizing **Groq** models and **Phi** framework. Integrates **YFinance** for financial data, including stock prices and analyst recommendations, and **DuckDuckGo** for web research. Built with a **FastAPI** backend and **Streamlit** frontend.

**Python** FastAPI | Streamlit | Phi | Groq | YFinance | DuckDuckGo

---

## 📚 Table of Contents

- ✨ [Features](#✨-features)
- 📸 [Preview](#📸-preview)
- 🚀 [Getting Started](#🚀-getting-started)
- 📁 [Project Structure](#📁-project-structure)
- 🤖 [Supported Models](#🤖-supported-models)
- 📜 [License](#📜-license)
- 🤝 [Contributions](#🤝-contributions)

---

## ✨ Features

- 🔗 **Powered by Groq** for model inference.
- 📊 **Financial Advisor** agent for real-time stock prices, analyst recommendations, and stock fundamentals using **YFinance**.
- 🌐 **Web Researcher** agent for retrieving web data using **DuckDuckGo**, including source citation.
- ⚙️ **Backend**: FastAPI for managing API requests.
- 🎨 **Frontend**: Streamlit UI for interactive querying and results display.
- 🛠️ Modular and easy to extend with additional agents or tools.

---


**UI Preview**

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ai-financial-advisor.git
cd ai-financial-advisor
```

### 2. Install dependencies

It’s recommended to use a virtual environment:

```bash
pip install -r requirements.txt
```

### 3. Setup environment variables

Create a `.env` file:

```ini
GROQ_API_KEY=your_groq_api_key
```

Alternatively, you can use the provided example:

```bash
cp .env.example .env
```

### 4. Run the backend server

```bash
uvicorn backend:app --reload --port 9998
```

### 5. Run the frontend

```bash
streamlit run frontend.py
```

---

## 📁 Project Structure

| File/Folder          | Purpose                                                |
|----------------------|--------------------------------------------------------|
| `playground.py`       | Main entry point for initializing agents and serving the app |
| `financial_advisor.py`| Logic for financial advisor and web researcher agents |
| `backend.py`          | FastAPI server for handling requests                  |
| `frontend.py`         | Streamlit UI for user interaction                     |
| `requirements.txt`    | Python dependencies                                    |
| `.env.example`        | Sample environment configuration (API keys)           |
| `assets/`             | Screenshots and media                                 |

---

## 🤖 Supported Models

- **Groq**:  
  - `meta-llama/llama-4-maverick-17b-128e-instruct`
- **Other Models**:  
  - Extendable to include other LLMs as required.

---

## 📜 License

This project is open-source and licensed under the **MIT License**.

---

## 🤝 Contributions

Have an idea? Found a bug? Want to add a feature?

Feel free to open an issue or submit a pull request!  
⭐ Star this repo to support the project!

---

### About

AI-powered **financial advisor** and **web researcher** built using **Groq**, **YFinance**, **DuckDuckGo**, **Phi**, and **FastAPI**.

---

### Topics

openai, fastapi, groq, streamlit, ai-chatbot, financial-advisor, phi, yfinance, duckduckgo
