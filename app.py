import os
import streamlit as st
from dotenv import load_dotenv
from firecrawl import FirecrawlApp
from google import genai as google_genai

current_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_dir, ".env")

load_dotenv(dotenv_path)

FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not FIRECRAWL_API_KEY:
    st.error("Firecrawl API Key is missing! Check your .env file name and content.")
    st.stop()

firecrawl = FirecrawlApp(api_key=FIRECRAWL_API_KEY)
client = google_genai.Client(api_key=GEMINI_API_KEY)

@st.cache_data(show_spinner=False)
def process_legal_page(url):
    with st.status("Analyzing with Gemini...", expanded=True) as status:
        # 1. Firecrawl: Extract text
        st.write("Step 1: Scraping website...")
        scrape_result = firecrawl.scrape(url, formats=['markdown'])
        raw_text = scrape_result.markdown if hasattr(scrape_result, 'markdown') else "No text found."

        st.write("Step 2: Simplifying legal language...")
        translator_response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=raw_text,
            config={'system_instruction': "You are a legal translator. Convert the following text into simple, easy-to-read English for a 12 year old. Limit your response to a maximum of 10 bullet points and use no more than 15 words per point."}
        )
        plain_text = translator_response.text

        st.write("Step 3: Distilling core facts...")
        distiller_response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=plain_text,
            config={'system_instruction': "You are a minimalist editor. Remove all greetings, introductions, and filler. Output ONLY a concise bulleted list of the most important facts and warnings. No extra talk."}
        )
        final_content = distiller_response.text
        
        status.update(label="Simplification Complete", state="complete", expanded=False)
    
    return final_content

st.title("Gemini Legal Simplifier")
url_input = st.text_input("Enter Legal URL:")
if st.button("Simplify Now") and url_input:
    try:
        result = process_legal_page(url_input)
        st.markdown(result)
    except Exception as e:
        st.error(f"Error: {e}")