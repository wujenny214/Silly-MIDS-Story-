# NLP In-Class Exercise: LLMs with APIs
#### Jenny Wu and Lilah DuBoff
---
### Story & Image Generator using Gemini API
This project demonstrates how to use the Google Gemini API to generate a children’s story and create an accompanying image based on the story’s content. The script performs three main tasks. First, it connects to the Gemini API using a private key, then generates a children’s story based on the user prompt. The current prompt is for it to write about the MIDS program. The script then saves the story to a text file, and generates an image inspired by the story. The image then gets saved locally.

### Requirements
The script used the following dependencies:
- Python 3.9+
- google-genai (Gemini client library)
- python-dotenv
- Pillow for image handling

### Setup
In order to use this project, follow the steps below:
1. Clone or download this project.
2. Create a .env file in the project directory.
3. Add your Gemini API key to the .env file
4. Run the main.py file

### Output Files
- story_output.txt – Contains the generated children’s story
- generated_story_image.png – A 1:1 colorful image reflecting the story