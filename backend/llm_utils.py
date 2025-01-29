from langchain_groq import ChatGroq
from docx import Document
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=100,
    timeout=None,
    max_retries=3
)

# Function to extract text from a docx file
def extract_text_from_docx(file):
    doc = Document(file)
    full_text = "\n".join([para.text for para in doc.paragraphs])
    return full_text

# Function to convert TSQL to Redshift PL/pgSQL
def convert_to_redshift_plpgsql(extracted_text):
    return llm.invoke(f"""{extracted_text} You are a SQL language to Redshift compliant PL-SQL language convertor.
    As a T-SQL to PL-SQL language converter, your task is to translate provided T-SQL code into Redshift compatible PL-SQL language.
    Reverse engineer the T-SQL script and figure out the corresponding Redshift PL-SQL code block by block. If equivalent code is not available add a comment stating the same and create a placeholder if possible
    Ensure the converted code is syntactically accurate.
    Only present the converted PL-SQL code without any additional notes or data before or after the conversion.
    Additionally, calculate the code conversion rate based on the number of functions in the original file and the converted output, and include this information as a comment in the converted file.
    Provide only the SQL output without ``` or any other indicator and nothing else outside of it.""").content

# Function to summarize the TSQL code
def summarize_code(extracted_text):
    return llm.invoke(f"{extracted_text} you are a SQL developer and you are tasked to summarize about what code does and provide analysis on the code.").content
