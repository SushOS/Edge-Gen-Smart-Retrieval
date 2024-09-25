# RAG with ObjectBox

This project utilizes ObjectBox, a high-performance NoSQL database solution, ideal for edge computing and mobile applications. We store the documents in this vector database for efficient and reliable retrieval for RAG (Retrieval Augmented Generation)
.
## Why ObjectBox?

1. Open-source
2. No internet or cloud required
3. High resource efficiency on edge networks (mobile phones, IoT)
4. Smooth data availability
5. Works both online and offline

## Getting Started

### Prerequisites

- Python 3.10
- Conda (for environment management)
- LangChain API key
- Groq API key

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/SushOS/Edge-Gen-Smart-Retrieval.git
   ```

2. Create a local virtual environment:
   ```
   conda create -p venv python=3.10
   ```

3. Activate the environment:
   ```
   conda activate ./venv
   ```

4. Install required packages:
   ```
   pip install -r requirements.txt
   ```

### Configuration

1. Create a LangChain API key:
   - Sign up and create an API key at [https://www.langchain.com/](https://www.langchain.com/)

2. Set up your API keys:
   - Create a `.env` file in the project root
   - Add your LangChain and Groq API keys to the `.env` file:
     ```
     LANGCHAIN_API_KEY=your_langchain_api_key_here
     GROQ_API_KEY=your_groq_api_key_here
     ```

## Running the Application

To run the application, use the following command:

```
streamlit run app.py
```


## Acknowledgments

- ObjectBox for providing the database solution
- LangChain and Groq for their API services

