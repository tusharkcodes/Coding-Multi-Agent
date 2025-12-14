# 🤖 Multi-Agent AI Software Development Framework (AutoGen)

## 📌 Overview

This project is a **Multi-Agent AI framework built using AutoGen**, where multiple specialized agents powered by **Mistral LLM (via Ollama)** collaboratively simulate a real-world software development lifecycle.

From a single natural-language requirement, the system generates:

* Structured requirements
* Production-ready Python code
* Code reviews and iterations
* Documentation
* Test cases
* Deployment instructions

---

## 🧠 Agents in the System

* **Requirement Analysis Agent** – Converts user input into structured software requirements
* **Coding Agent** – Generates clean and modular Python code
* **Code Review Agent** – Reviews code and approves or requests improvements
* **Documentation Agent** – Produces clear technical documentation
* **Test Case Generation Agent** – Creates unit and integration tests
* **Deployment Configuration Agent** – Generates setup and run instructions
* **Streamlit UI Agent** – Provides a UI to interact with the multi-agent pipeline

Agents are coordinated using **RoundRobinGroupChat** or **SelectorGroupChat** for iterative workflows.

---

## 🛠️ Tech Stack

* Python 3.10+
* AutoGen (Multi-Agent Orchestration)
* Mistral LLM (via Ollama)
* Streamlit (UI)
* AsyncIO

---

## 📂 Project Structure

```
Multi-Agent-Autogen/
│
├── agents/                 # All agent definitions
│   ├── requirement_agent.py
│   ├── coding_agent.py
│   ├── review_agent.py
│   ├── documentation_agent.py
│   ├── test_agent.py
│   └── deployment_agent.py
│
├── tools/                  # Optional tool definitions
│   └── file_tools.py
│
├── models.py               # LLM configuration (Ollama / Mistral)
├── app.py                  # Streamlit UI
├── main.py                 # GroupChat orchestration
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/multi-agent-autogen.git
cd multi-agent-autogen
```

---

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv multi-agent
source multi-agent/bin/activate  # macOS/Linux
# multi-agent\Scripts\activate  # Windows
```

---

### 3️⃣ Install Required Libraries

```bash
pip install --upgrade pip
pip install autogen-agentchat autogen-core autogen-ext
pip install asyncio tiktoken openai streamlit ollama
```

Or using `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🦙 Ollama & Mistral Setup

### 4️⃣ Install Ollama

Download and install Ollama from:

👉 [https://ollama.com/download](https://ollama.com/download)

---

### 5️⃣ Pull Mistral Model

```bash
ollama pull mistral
```

Ensure Ollama is running:

```bash
ollama serve
```

---

## 🚀 Running the Project

### Run Multi-Agent Pipeline

```bash
python main.py
```

---

### Run Streamlit UI

```bash
streamlit run app.py
```

Then open the browser at:

```
http://localhost:8501
```

---

## 🔁 Multi-Agent Flow

1. User enters requirement
2. Requirement agent structures it
3. Coding agent generates code
4. Review agent validates or requests changes
5. Documentation and tests are generated
6. Deployment instructions are produced

---

## 🎯 Key Highlights

* Fully local LLM inference using **Mistral + Ollama**
* Iterative agent collaboration
* Real-world software engineering simulation
* Clean separation of concerns
* Beginner-friendly AutoGen implementation

---


## 🏁 Conclusion

This project demonstrates how **LLM-powered agents can collaborate like a real engineering team**, making it a strong foundation for learning **multi-agent systems, AutoGen, and applied Generative AI**.
