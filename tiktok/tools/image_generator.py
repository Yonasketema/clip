import os
import json
import requests
from crewai_tools import BaseTool
from openai import OpenAI
from typing import Any
from pathlib import Path


# class BaseT


class AppBaseTool(BaseTool):
    crew_id: str = ""
    pass


class ImageGenerator(AppBaseTool):
    name: str = "image_generator"
    description: str = """
        Generate image for a given full script !
        Using the OpenAI image generation API,
        saves it in the current images folder.


        Args:
           self: self is not required positional argument: 'self' is the instance of a python class
           script:  the product script as a string.
        Returns:
            The extracted Image path as a string, or None if the URL is invalid.
        """

    def __init__(self, crew_id, **kwargs):
        super().__init__(**kwargs)
        if crew_id is not None:
            self.crew_id = crew_id

    def _run(self, script: str, **kwargs: Any) -> str:

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        json_file_path = Path(__file__).parent.parent / \
            f"data/{self.crew_id}_data.json"

        with open(json_file_path, "r") as file:
            # Load the JSON data from the file
            split_text_into_lines = json.load(file)

        for index, textJSON in enumerate(split_text_into_lines):

            filepath = Path(__file__).parent.parent / \
                f"images/{self.crew_id}_image_{index}.png"

            prompt_response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"""
                      Generate a prompt used for  image generate
                      You have a full script and you will be 
                      generate prompt for a given part of script
                                     
                      depending on the subject of a video.
                      full_script: {script}
                      part of script : {textJSON['word'].strip()}
                     
                      Instructions:

                      Make it detailed and comprehensive
                      Use as many adjectives as possible
                      Define the style
                       
                       

                
                      YOU MUST ONLY RETURN THE PROMPT.
                      YOU MUST NOT RETURN ANYTHING ELSE.
                      
                  
                      """}],
            ).choices[0].message.content

            response = client.images.generate(
                model="dall-e-3",
                prompt=f"photo of  {prompt_response}",
                size="1024x1792",
                quality="standard",
                n=1,
            )

            # client = Client()

            image_url = response.data[0].url
            # words = script.split()[:5]
            # safe_words = [re.sub(r'[^a-zA-Z0-9_]', '', word) for word in words]
            # filename = "_".join(safe_words).lower() + ".png"
            # filepath = os.path.join(os.getcwd(), filename)
            # filepath = Path(__file__).parent / f"images/{filename}"

            # Download the image from the URL
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                with open(filepath, 'wb') as file:
                    file.write(image_response.content)

                # return filepath
            else:
                print("> Failed to download the image.")
                return "Failed to download the image."

        return script
