import requests  # Library for making HTTP requests
import pdfplumber  # Library for extracting text from PDF files
from googleapiclient.discovery import build  # Library for building Google API service
from transformers import AutoTokenizer, AutoModel  # Hugging Face library for NLP models

# Google Custom Search API credentials
API_KEY = 'YOUR_API_KEY_HERE'  # Google API key
CX = 'YOUR_CUSTOM_SEARCH_ENGINE_ID_HERE'  # Google Custom Search Engine ID

# Pegasus-XSUM model
API_URL = "https://api-inference.huggingface.co/models/google/pegasus-xsum"  # Endpoint for Pegasus-XSUM model API
HEADERS = {"Authorization": "Bearer YOUR_HUGGING_FACE_API_TOKEN_HERE"}  # Authorization headers for Hugging Face API

# Load the Pegasus-XSUM model
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("google/pegasus-xsum")  # Loading tokenizer
    model = AutoModel.from_pretrained("google/pegasus-xsum")  # Loading the model
    return tokenizer, model

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:  # Open PDF file
            text = ''
            for page in pdf.pages:  # Iterate over pages
                text += page.extract_text()  # Extract text from each page
        return text
    except FileNotFoundError:
        print(f"PDF file '{pdf_path}' not found.")  # Handle file not found error
        return None
    except pdfplumber.PDFSyntaxError:
        print(f"Error: Syntax error while parsing PDF file '{pdf_path}'.")  # Handle syntax error in PDF
        return None
    except pdfplumber.PDFTextExtractionNotAllowed:
        print(f"Error: Text extraction not allowed in PDF file '{pdf_path}'.")  # Handle text extraction not allowed
        return None
    except Exception as e:
        print(f"Error extracting text from PDF: {str(e)}. File: {pdf_path}")  # Log error
        return None  # Handle other errors

# Function to fetch articles from the web based on a search query
def fetch_articles_from_web(query, num_results=5):
    try:
        service = build("customsearch", "v1", developerKey=API_KEY)  # Build Google Custom Search service
        result = service.cse().list(q=query, cx=CX, num=num_results).execute()  # Execute search query
        articles = [item['link'] for item in result.get('items', [])]  # Extract article links from search results
        return articles
    except Exception as e:
        print(f"Error fetching articles from web: {str(e)}")  # Log error
        return []  # Returning empty list if error occurs

# Function to generate summary using Pegasus-XSUM model
def summary_gen(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)  # Sending POST request to model API
    result = response.json()  # Parse JSON response
    if isinstance(result, list) and len(result) > 0 and isinstance(result[0], dict):
        summary_text = result[0].get('summary_text', '')  # Extract summary text from response
        return summary_text
    return None

# Entry point of the script
if __name__ == "__main__":
    pdf_path = '/path/to/your/pdf/file.pdf'  # Path to the PDF file

    # Load the model
    tokenizer, model = load_model()

    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_path)

    if pdf_text is None:
        print("Failed to extract text from PDF. Please check the file path and try again.")  # Display error message if text extraction fails
    else:
        # Generate summary using Pegasus-XSUM model
        summary = summary_gen(pdf_text)

        if summary is None:
            print("Failed to generate summary. Please try again later.")  # Display error message if summary generation fails
        else:
            # Fetch articles from the web based on the summary
            articles = fetch_articles_from_web(summary, num_results=5)

            if not articles:
                print("No articles found based on the summary.")  # Display message if no articles found
            else:
                print("Related Articles:")
                for url in articles:
                    print(url)  # Display related articles
