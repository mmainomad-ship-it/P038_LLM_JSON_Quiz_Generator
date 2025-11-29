# 📝 P038: LLM-Powered Quiz Generator (Strict JSON Output)

## ✨ Description
This project demonstrates a core AI Engineering skill: **forcing a Large Language Model (LLM)** to produce a strictly formatted output, specifically a **valid JSON object**, which can be reliably parsed by a downstream Python application. It generates multiple-choice quizzes on any topic using a local model (Llama 3 via Ollama).

---

## 🔑 Key Features & Constraints

* **Strict JSON Schema Enforcement:** Uses a detailed System Prompt to ensure the LLM outputs a single, clean JSON string.
* **Local LLM Integration:** Communicates with Llama 3 running via **Ollama** on a local machine.
* **Robust Parsing:** Implements **error handling** using `try...except json.JSONDecodeError` to gracefully manage potential LLM output failures.

---

## 💻 Technology Stack

* **Language:** Python 3
* **LLM Framework:** Ollama
* **Model:** Llama 3 (or equivalent local model)

---

## 🚀 Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd P038_LLM_JSON_Quiz_Generator
    ```
2.  **Setup Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Start Local LLM:**
    * Ensure **Ollama** is installed and running.
    * Pull the required model (e.g., Llama 3): `ollama pull llama3`
5.  **Run the Script:**
    ```bash
    python quiz_maker.py
    ```

---

## 👨‍💻 Author

* **Author:** mmainomad-ship-it
* **GitHub:** https://github.com/mmainomad-ship-it