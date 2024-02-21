# Intelligent Email Assistant

## 1. Background and Problem Statement

In the modern professional environment, managing a large influx of emails can be overwhelming, leading to decreased productivity and missed opportunities. The challenge lies in efficiently organizing, prioritizing, and responding to emails while extracting valuable insights for decision-making. Traditional email clients offer limited assistance in managing the complexity and volume of modern email communication.

## 2. The Solution

 This is an innovative email assistant that revolutionizes how individuals and organizations manage their email ecosystems. By leveraging advanced artificial intelligence (AI) and natural language processing (NLP) technologies, EmailFlux offers a suite of features designed to simplify email management, enhance decision-making, and provide actionable statistics. Key functionalities include smart categorization, priority filtering, sentiment analysis, and comprehensive email analytics, and even email responses suggestions.

## 3. Overview

### System's Architecture

![Untitled-2024-01-10-1001](https://github.com/Yassmine2020/EmailAssistant/assets/85367800/ef6098af-37d6-4086-9a61-13fb22592c84)

## 5. Project Structure

The project is organized as follows to ensure easy navigation and development

```
├─utils
│ ├─best_answer
│ ├─categorizer
│ ├─classify_review
│ ├─importance_classifier
│ ├─text_to_sentiment
│ ├─text_to_speech
│ ├─text_to_summary
│ ├─translate_to_english
├─app.py
├─requirements.txt
```

## 6. Usage

Here's how you can set the project up:

```bash
# Clone the repository
git clone https://github.com/Yassmine2020/EmailAssistant.git

# Install dependencies
pip install -r requirements.txt

# Create an API Keys File
	" Navigate to the utils directory within the Email Assistant project.
		Create a new file named keys.py.
		Inside keys.py, add your OpenAI and ElevenLabs API keys in the following format:
		api_key of openai
		api_key of elevenlabs "

openai_api_key = "your_openai_api_key_here"
elevenlabs_api_key = "your_elevenlabs_api_key_here"

# Start the application
python app.py

# Test the api
"Now that the application is running, you can test its functionality by sending a POST request to the /predict endpoint. This request must include a JSON body containing the email content you wish to process. Here's an example of how to format your request:"

{
  "input": "Your email content here"
}
```
