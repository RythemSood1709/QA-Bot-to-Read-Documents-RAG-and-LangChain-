# PDF QA Bot using RAG & IBM Watsonx

A modular Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask natural language questions about their content. The application processes the document, creates a semantic vector database, and uses IBM's Granite LLM to generate precise answers based solely on the uploaded text.

## 🚀 Features

* **PDF Processing:** Automatically loads and parses uploaded PDF files.
* **Smart Text Splitting:** Uses recursive character splitting to break down large documents into manageable, semantically meaningful chunks.
* **Local Vector Storage:** Utilizes ChromaDB to store and quickly retrieve document embeddings.
* **Enterprise AI:** Powered by IBM Watsonx (`granite-3-2-8b-instruct` for generation, `slate-125m-english-rtrvr` for embeddings).
* **Interactive UI:** A clean, easy-to-use web interface built with Gradio.

## 🛠️ Tech Stack

* **Language:** Python 3.11
* **Framework:** LangChain
* **LLM & Embeddings:** IBM Watsonx.ai
* **Vector Database:** Chroma
* **Frontend:** Gradio

## 📁 Project Structure

The codebase is modularized for better maintainability and separation of concerns:

```text
qabot_project/
│
├── data_processing.py      # Handles PyPDF loading and recursive text splitting
├── models.py               # Configures Watsonx LLM and Embedding models
├── rag_engine.py           # Core logic: builds ChromaDB and defines the RetrievalQA chain
├── main.py                 # Entry point: builds the Gradio UI and launches the server
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```
## ⚙️ Installation & Setup

### 1. Prerequisites
* **Python 3.11** installed on your system.
* An active **IBM Cloud / Watsonx Account** (or IBM Academic Initiative trial) for API access.

### 2. Create a Virtual Environment
It is highly recommended to run this project inside an isolated virtual environment.
```bash
py -3.11 -m venv venv311
source venv311/Scripts/activate  # On Windows Git Bash
```

### 3. Install Dependencies
Ensure your virtual environment is activated, then install the required packages:
```bash
pip install langchain langchain-ibm langchain-community chromadb pypdf gradio huggingface_hub
```

### 4. Configure Environment Variables
The application requires your IBM Watsonx API key to authenticate. Export it in your terminal before running the app:

```bash
export WATSONX_APIKEY="your_actual_api_key_here"
```

### 5.💻 Usage
Activate your virtual environment.

Run the main application script:

```bash
python main.py
```

