# T-SQL to Redshift Code Converter

A web application that converts T-SQL code to Redshift-compatible PL/pgSQL code and provides code summaries.

## Features

- Upload T-SQL code in DOCX format
- Generate code summaries
- Convert T-SQL to Redshift-compatible PL/pgSQL
- Side-by-side code comparison
- User-friendly web interface

## Prerequisites

- Python 3.8 or higher
- GROQ API key

## Setup

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
# OR
.\venv\Scripts\activate  # For Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your GROQ API key:
```
GROQ_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit app:
```bash
cd frontend
streamlit run app.py
```

2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)
3. Upload a DOCX file containing T-SQL code
4. View the code summary
5. Click "Convert to Redshift PL/pgSQL" to generate the converted code

## Project Structure

```
├── backend/
│   └── llm_utils.py    # LLM integration and text processing
├── frontend/
│   └── app.py          # Streamlit web interface
├── images/
│   └── CT_Logo.png     # Application logo
├── .env                # Environment variables
└── README.md          # Project documentation
```

## Dependencies

- streamlit
- langchain-groq
- python-docx
- python-dotenv

## License

MIT License