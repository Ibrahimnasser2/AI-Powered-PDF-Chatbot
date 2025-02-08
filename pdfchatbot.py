import streamlit as st
import pymupdf  # PyMuPDF
import google.generativeai as genai

# Configure Gemini API key (ensure you set this in a secure way)
genai.configure(api_key="AIzaSyA7fM9YjLbUNJSTgM_Wo6qSxMKbUbrEaw4")

# Model generation configuration
generation_config = {
    "temperature": 0.7,  # Controls randomness in responses
    "top_p": 0.9,  # Controls probability mass for sampling
    "top_k": 30,  # Limits number of highest probability candidates considered
    "max_output_tokens": 1024,  # Maximum tokens in response
    "response_mime_type": "text/plain",
}

# Load Gemini-2.0-Flash model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config,
)

def extract_text_from_pdf(pdf_files):
    """
    Extracts text from uploaded PDF files.
    Args:
        pdf_files (list): List of uploaded PDF files.
    Returns:
        str: Extracted text from all PDFs combined.
    """
    text = ""
    for pdf in pdf_files:
        try:
            doc = pymupdf.open(stream=pdf.read(), filetype="pdf")
            for page in doc:
                text += page.get_text("text") + "\n"
        except Exception as e:
            st.error(f"Error processing PDF {pdf.name}: {e}")  # Handle potential errors
            return None  # Return None to signal an error
    return text

def generate_response(question, context):
    """
    Generates an AI response based on a provided question and context.
    Args:
        question (str): User's query.
        context (str): Extracted text from PDF.
    Returns:
        str: AI-generated response.
    """
    input_prompt = f"""You are a helpful assistant that answers questions based on the provided PDF context. 
    You must ONLY use the information provided in the context.
    If the answer is not found in the context, respond with \"I'm sorry, but I cannot answer this question based on the provided document.\"
    Be concise and to the point in your answers.

    Context:
    {context}

    Question: {question}
    """
    try:
        response = model.generate_content(input_prompt)
        return response.text if response.text else "I'm sorry, but I cannot answer this question based on the provided document."
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return "An error occurred while generating the response."

# Streamlit UI Configuration
st.set_page_config(page_title="PDF Chatbot", layout="wide")
st.title("📄 AI-Powered PDF Chatbot")

# Sidebar for PDF Upload
st.sidebar.header("Upload PDF Documents")
uploaded_files = st.sidebar.file_uploader("Choose PDF files", accept_multiple_files=True, type=["pdf"])

if uploaded_files:
    st.sidebar.success("PDFs uploaded successfully!")
    extracted_text = extract_text_from_pdf(uploaded_files)
    
    if extracted_text is not None:  # Proceed only if extraction was successful
        # Initialize chat history if not already present
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        
        st.subheader("Chat with your PDF")
        
        # Display previous chat messages
        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]):
                st.write(chat["content"])
        
        # Capture user input in chat format
        user_question = st.chat_input("Ask a question about the PDFs...")
        if user_question:
            # Append user message to chat history
            st.session_state.chat_history.append({"role": "user", "content": user_question})
            with st.chat_message("user"):
                st.write(user_question)
            
            # Generate AI response and append to chat history
            answer = generate_response(user_question, extracted_text)
            st.session_state.chat_history.append({"role": "assistant", "content": answer})
            with st.chat_message("assistant"):
                st.write(answer)
    else:
        st.error("PDF extraction failed. Please check the PDFs and try again.")
else:
    st.info("Upload PDF documents to start.")
