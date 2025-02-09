# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY pdfchatbot.py .

# Make port 8501 available to the world outside this container (Streamlit's default port)
EXPOSE 8501  

# Define environment variable for Gemini API Key
ENV GOOGLE_API_KEY="AIzaSyA7fM9YjLbUNJSTgM_Wo6qSxMKbUbrEaw4"

# Run pdfchatbot.py when the container launches
CMD ["streamlit", "run", "pdfchatbot.py", "--server.enableCORS", "false"]