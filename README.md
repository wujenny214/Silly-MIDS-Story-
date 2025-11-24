# NLP In-Class Exercise: LLMs with APIs
#### Jenny Wu and Lilah DuBoff
---
### Story & Image Generator using Gemini API
This project demonstrates how to use the Google Gemini API to generate a children’s story and create an accompanying image based on the story’s content. The script performs three main tasks. First, it connects to the Gemini API using a private key, 
Generates a children’s story
Saves the story to a text file
Creates an image inspired by the story and saves it locally

### Requirements
Make sure you have the following installed:
Python 3.9+
google-genai (Gemini client library)
python-dotenv
Pillow for image handling
Install required packages:

### Setup
Clone or download this project.
Create a .env file in the project directory.
Add your Gemini API key to the .env file:

Output Files
story_output.txt – Contains the generated children’s story
generated_story_image.png – A 1:1 colorful image reflecting the story