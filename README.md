# AI-Powered PDF Chatbot

This AI-powered chatbot allows users to upload PDF documents and interact with them through a chat interface. The chatbot extracts text from PDFs and answers user queries based on the document's content using Google's Gemini AI model.

## Features
- Upload multiple PDF files.
- Extract text from PDFs automatically.
- Ask questions directly through a chat window.
- Persistent chat history for better conversation flow.
- AI-generated responses strictly based on the uploaded documents.

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/pdf-chatbot.git
   cd pdf-chatbot
   ```
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up the Gemini API key in your environment variables:
   ```sh
   export GEMINI_API_KEY="your_api_key_here"
   ```

### Running the Chatbot
Execute the following command:
```sh
streamlit run app.py
```

## API Documentation

### `extract_text_from_pdf(pdf_files)`
Extracts text from uploaded PDF documents.
- **Parameters:**
  - `pdf_files` (list): List of uploaded PDF files.
- **Returns:**
  - `str`: Extracted text from PDFs.

### `generate_response(question, context)`
Generates an AI response based on user queries and the extracted PDF content.
- **Parameters:**
  - `question` (str): The user's query.
  - `context` (str): Extracted text from the PDF.
- **Returns:**
  - `str`: AI-generated response.

## Contributing
Feel free to submit issues or contribute by creating a pull request.

## License
This project is licensed under the MIT License.

