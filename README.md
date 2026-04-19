# LegalEase-AgenticAI
An agentic ai which fetches text from legal documents from user inputted URLs and processes them to convert to human readable text.
This agentic ai fetches text from a URL with firecrawl, this data is sent to gemini for processing and translating, this response is again sent to gemini for post processing and stripping text that is not required.

 ************************************
 |       RUNNING THE PROGRAM        |
 |       RUNNING THE PROGRAM        |
 |       RUNNING THE PROGRAM        |
 |       RUNNING THE PROGRAM        |
 ************************************

 Step 1: Create a file named ".env"
 Step 2: Open the file in notepad, generate your gemini and firecrawl api keys
 Step 3: Type down(do not include curly braces):
 GEMINI_API_KEY={YOUR GEMINI API KEY}
 FIRECRAWL_API_KEY={YOUR FIRECRAWL API KEY}
 Step 4: Since this is a streamlit file, open terminal, change to the directory with app.py alongside .env, and run "streamlit run app.py"

 (OR)

 Visit either of the following websites for the pre-built tool
 [Visit LegalEase (Main)](https://sep.satronic.org)
 https://satronic-sep.netlify.app
 https://legalease-agenticai.streamlit.app
