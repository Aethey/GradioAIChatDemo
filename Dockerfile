# Use Python 3.10 as the base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy all files from the current directory to the working directory
COPY . .

# Install all Python libraries listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port used by Gradio
EXPOSE 7860

# Set the environment variable for Gradio server
ENV GRADIO_SERVER_NAME="0.0.0.0"

# Set the command to run when the container starts
CMD ["python", "omrm_streaming_gpt_chart.py"]
