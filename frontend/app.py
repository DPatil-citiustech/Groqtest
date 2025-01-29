import streamlit as st
import sys
import os
import time

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.llm_utils import extract_text_from_docx, convert_to_redshift_plpgsql, summarize_code

# Streamlit app
st.set_page_config(page_title="Code Converter", page_icon=":robot_face:", layout="wide")

st.image("images\CT_Logo.png", width=200)
st.title("Code Converter")

uploaded_file = st.file_uploader("Upload a TSQL code DOCX file", type="docx")

if uploaded_file is not None:
    extracted_text = extract_text_from_docx(uploaded_file)
    
    with st.spinner("Generating summary..."):
        start_time = time.time()
        code_summary = summarize_code(extracted_text)
        end_time = time.time()
        st.write(f"Summary generated in {end_time - start_time:.2f} seconds")
    
    st.subheader("Code Summary")
    st.text_area("", code_summary, height=200)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("TSQL Code")
        st.text_area("", extracted_text, height=400)
    
    if st.button("Convert to Redshift PL/pgSQL"):
        with st.spinner("Converting..."):
            start_time = time.time()
            converted_code = convert_to_redshift_plpgsql(extracted_text)
            end_time = time.time()
            st.write(f"Conversion completed in {end_time - start_time:.2f} seconds")
        
        with col2:
            st.subheader("Converted Redshift Compatible Code")
            st.text_area("", converted_code, height=400)
