# Text Summarization CLI Tool

This CLI tool summarizes text input using the Ollama API with the Qwen2 0.5B model. You can provide text directly or specify a file containing the text to be summarized.

## Installation

1. Make a folder and open it in Visual studio code

2. Create and activate a virtual environment (if you haven't already):
    - # On Windows use `venv\Scripts\activate`
    - # On macOS `source venv/bin/activate` 
  
3. Open terminal and Clone the repository:
    `git clone https://github.com/SanskarSingh17/Text-Summarization-CLI-Tool`
    change directory `cd Text-Summarization-CLI-Tool`

4. Install the required dependencies:
    `pip install -r requirements.txt`


## Usage

### Summarize Direct Text Input

Summarize text from a file: `python index.py "Your text here"`

Summarize text using gile: `python index.py "path/to/your/textfile.txt" --file`

## Configuration
Make sure you have an .env file in the root directory with necessary environment variables for the Ollama API.
