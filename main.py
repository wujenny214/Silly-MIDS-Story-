import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO 

#connect to the API
load_dotenv()
client = genai.Client(api_key=os.getenv("GEM_api_key"))

#define the prompt for the story
story_response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Write me a goofy children's story about a student in the Interdisciplinary Data Science Studies program"
)
print(story_response.text)

# Save the generated story to a text file
def save_story_to_txt(text_content, filename="story_output.txt"):
    """Saves the generated story to a text file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text_content)
        print(f"Story successfully saved to '{filename}'")
    except IOError as e:
        print(f"Error saving file: {e}")

save_story_to_txt(story_response.text)

#second prompt to generate an image based on the story
image_prompt = (
    f"Create 1 photo that represents key points of the following story: {story_response.text}. The photo style should be childlike, colorful, and highly detailed."
)

image_response = client.models.generate_images(
    model="imagen-4.0-generate-001", 
    prompt=image_prompt,
    config=types.GenerateImagesConfig(
        number_of_images=1,
        aspect_ratio="1:1" 
    )
)


# Save the generated image 
if image_response.generated_images:
    generated_image = image_response.generated_images[0].image
    image_bytes = generated_image.image_bytes
    image = Image.open(BytesIO(image_bytes))
    image.save("generated_story_image.png")
    print("Image successfully generated and saved as 'generated_story_image.png'")
