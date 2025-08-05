# 🤖 AI Web Scraper Pro

<div align="center">

**An intelligent web scraping application that uses large language models to extract structured data from any website.**

</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Streamlit-1.35%2B-orange?style=for-the-badge&logo=streamlit" alt="Streamlit Version">
  <img src="https://img.shields.io/badge/Framework-LangChain-green?style=for-the-badge" alt="LangChain">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge" alt="License">
</p>

---

AI Web Scraper Pro is a powerful tool that combines advanced web scraping capabilities with the analytical power of large language models (LLMs). It allows users to not only fetch content from dynamic, JavaScript-heavy websites but also to ask natural language questions to parse and extract the exact information they need, turning unstructured web content into clean, structured data.

## ✨ Key Features

-   **Intelligent Scraping**: Utilizes **Bright Data's Scraping Browser** and **Selenium** to handle complex websites, including those with CAPTCHAs and dynamic content loading.
-   **AI-Powered Parsing**: Leverages **Ollama** and **LangChain** to understand user queries and intelligently extract relevant information from raw HTML content.
-   **User-Friendly Interface**: A clean, professional, and interactive web interface built with **Streamlit**, designed for ease of use.
-   **Dynamic & Interactive**: Features real-time progress indicators, status updates, and interactive data tables for a smooth user experience.
-   **Structured Output**: Delivers extracted data in a clean, organized format, with options to download for further analysis.

---

## ⚙️ Technology Stack

| Technology                               | Purpose                                      |
| :--------------------------------------- | :------------------------------------------- |
| **Python** | Core programming language                    |
| **Streamlit** | Building the interactive web application     |
| **Selenium** | Automating web browser interaction           |
| **Bright Data** | Robust, proxy-powered scraping infrastructure|
| **Ollama (Gemma)** | Local LLM for content analysis and parsing   |
| **LangChain** | Framework for building LLM-powered applications |
| **BeautifulSoup** | HTML parsing and content cleaning            |
| **Pandas** | Data manipulation and display (future use)   |

---

## 🚀 How It Works

The application follows a simple yet powerful workflow to turn a URL into structured data.

<div align="center">

**[Enter URL]** `->` **[Scrape with Selenium & Bright Data]** `->` **[Clean with BeautifulSoup]** `->` **[User Query]** `->` **[Parse with Ollama & LangChain]** `->` **[Display Results]**

</div>

1.  **Input**: The user provides a target website URL.
2.  **Scraping**: Selenium, connected to Bright Data's Scraping Browser, navigates to the URL, solves any CAPTCHAs, and fetches the full page source code.
3.  **Cleaning**: BeautifulSoup removes scripts, styles, and other noise, leaving only the meaningful text content.
4.  **Query**: The user describes in natural language what information they want to extract (e.g., "Extract all job titles and their locations").
5.  **AI Parsing**: The cleaned content and the user's query are sent to a local LLM via LangChain and Ollama. The AI analyzes the text and extracts the requested data.
6.  **Output**: The final, structured data is displayed in the Streamlit app, ready for viewing or download.

---

## 🛠️ Getting Started

Follow these steps to set up and run the project on your local machine.

### 1. Prerequisites

-   Python 3.9 or higher
-   [Ollama](https://ollama.com/) installed and running locally.
-   A [Bright Data](https://brightdata.com/) account and a Scraping Browser API key.

### 2. Clone the Repository

```bash
git clone [https://github.com/your-username/ai-web-scraper-pro.git](https://github.com/your-username/ai-web-scraper-pro.git)
cd ai-web-scraper-pro
```

### 3. Install Dependencies

It's recommended to use a virtual environment.

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the required packages
pip install -r requirements.txt
```
*(Note: You will need to create a `requirements.txt` file containing streamlit, pandas, beautifulsoup4, selenium, python-dotenv, langchain-ollama, and langchain-core.)*

### 4. Set Up Environment Variables

Create a file named `.env` in the root directory of the project and add your Bright Data Scraping Browser API key:

```.env
# .env file
SBR_WEBDRIVER="wss://your-brightdata-api-key"
```

### 5. Pull the LLM Model

Open your terminal and pull the Gemma model for Ollama:

```bash
ollama pull gemma
```

---

## ▶️ Usage

Once the setup is complete, run the Streamlit application from your terminal:

```bash
streamlit run main.py
```

This will open the AI Web Scraper Pro application in your default web browser.

---

## 📂 Project Structure

```
.
├── main.py         # Main Streamlit application file (UI and workflow)
├── scrape.py       # Functions for scraping websites with Selenium and Bright Data
├── parse.py        # Functions for parsing content with Ollama and LangChain
├── .env            # Environment variables (API keys)
├── requirements.txt# Project dependencies
└── README.md       # This file
```

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
`
