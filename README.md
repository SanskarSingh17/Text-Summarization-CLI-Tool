# Text Summarization CLI Tool

This CLI tool summarizes text input using the Ollama API with the Qwen2 0.5B model. You can provide text directly or specify a file containing the text to be summarized.

## Installation

1. Make a folder and open it in Visual studio code
  
2. Open terminal and Clone the repository:
    `git clone <repository-url>`
    `cd <repository-directory>`


3. Create and activate a virtual environment (if you haven't already):
    `python -m venv venv`
    `source venv/bin/activate`  # On Windows use `venv\Scripts\activate`

4. Install the required dependencies:
    `pip install -r requirements.txt`


## Usage

### Summarize Direct Text Input

Summarize text from a file: `python index.py "Your text input here"`

Summarize text using gile: `python index.py "path/to/your/textfile.txt" --file`

## Configuration
Make sure you have an .env file in the root directory with necessary environment variables for the Ollama API.