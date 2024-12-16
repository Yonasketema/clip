import os
import json
import requests
from crewai_tools import BaseTool
from openai import OpenAI
from typing import Any
from pathlib import Path
import pprint
import requests
from pexelsapi.pexels import Pexels


# class BaseT


class AppBaseTool(BaseTool):
    crew_id: str = ""
    pass


class PexelVideo(AppBaseTool):
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

    def _run(self, word: str, **kwargs: Any) -> str:

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        json_file_path = Path(__file__).parent.parent / \
            f"data/{self.crew_id}_data.json"

        pexel = Pexels(
            'qIscZgc6YaDnLvoozgmG9EeTpxqMImzTFjzyfmdrmV4QtWnSbWr78ZgW')
        search_videos = pexel.search_videos(word)
        pprint.pprint(search_videos.get('videos')[
            0].get('video_files')[0].get('link'))

        video_url = search_videos.get('videos')[0].get(
            'video_files')[0].get('link')
        # pexel = Pexels('API_KEY')
        # get_video = pexel.get_video(search_videos.get('videos')[0].get('id'))
        # print(get_video)

        image_response = requests.get(video_url)
        if image_response.status_code == 200:
            with open(f"tiktok/upload/{self.crew_id}_video.mp4", 'wb') as file:
                file.write(image_response.content)

        return json_file_path
