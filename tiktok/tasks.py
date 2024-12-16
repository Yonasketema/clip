from textwrap import dedent
from crewai import Task
from crewai_tools import SeleniumScrapingTool
from fastapi import HTTPException
import os
from pathlib import Path
from urllib.parse import urljoin
from tools.voice_generator import VoiceGenerator
from tools.image_generator import ImageGenerator
from tools.video_maker import VideoMakerGenerator

import requests

from crewai_tools import ScrapeWebsiteTool


from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()


# scrape_website_tool = SeleniumScrapingTool(
#     website_url='https://kalodata.com/product')


class TiktokTasks():

    def __init__(self, crew_id, url, ProductName, description, page):

        self.crew_id = crew_id
        self.scrape_website_tool = ScrapeWebsiteTool(website_url=f'{url}')
        self.description = description
        self.ProductName = ProductName
        self.url = url
        self.page = page

        self.generate_voice_tool = VoiceGenerator(self.crew_id)
        self.generate_image_tool = ImageGenerator(self.crew_id)
        self.videoMaker_tool = VideoMakerGenerator(
            self.crew_id, self.ProductName)

    def update_info(self, event_message):
        # todo : update database here
        # print(f'--> {event_message}')

        message = event_message.raw_output
        status = "WORKING"
        finally_data = {}

        if os.path.isfile(message):

            path = Path(message)
            if path.suffix == '.mp3':
                message = f'http://localhost:8000/audios/{path.stem}{path.suffix}'
            elif path.suffix == '.png':
                message = f'http://localhost:8000/images/{path.stem}{path.suffix}'
            elif path.suffix == '.mp4':

                message = f'http://localhost:8000/videos/{path.stem}{path.suffix}'
                status = "END"

                if all(string for string in [self.ProductName, self.description, self.url]):

                    finally_data = {
                        "productName": f"{self.ProductName}",
                        "description": f"{self.description}",
                        "productWebsite ": f"{self.url}",
                        "videoUrl": f"{message}",
                        "page": f'{self.page}'
                    }

                else:

                    finally_data = {
                        "videoUrl": f"{message}",
                        "page": f'{self.page}'
                    }

                try:
                    response = requests.post(
                        f'http://localhost:3000/api/created_video/{self.crew_id}', json=finally_data)
                    response.raise_for_status()
                    return response.json()
                except requests.exceptions.RequestException as e:
                    raise HTTPException(status_code=500, detail=str(e))

        data = {
            "status": status,
            "event_message": message,
            "output": ""
        }

        try:

            response = requests.post(
                f'http://localhost:3000/api/{self.crew_id}', json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=str(e))

    def product_list(self, agent):

        if all(string for string in [self.ProductName, self.description, self.url]):
            desc = f"""\
			You are helping create a product summary of description,these are the instructions:

			Instructions
			------------
			 Description:{self.description}
             ProductName:{self.ProductName}
             Url:{self.url}

			Using the given description , productName and url you got, scrap and gather every information about
            the product and create product description

            
			

			Your Final answer must be the full summary of product description
			"""
        else:
            desc = "You will select best product"

        return Task(
            description=desc,
            expected_output='The name of the product and a product summary of description of the product.',
            agent=agent,
            callback=self.update_info,
            tools=[self.scrape_website_tool, search_tool]
        )

    def write_script(self, agent, task: Task):
        return Task(
            description="""
            Based on Product Researcher result, write script about the product for TikTok Shop Affiliate short video .
            Start the script with emotionally world like ! .  
            Don't use any emoji.
            Don't include any greeting Like -Hi,tiktok fan !
            avoid complex words so it doesn't sound like A !.
            """,
            expected_output="""
            script about the product under 150 word !
            separated the script with newline !
                         
            """,
            agent=agent,
            callback=self.update_info,
            context=[task]
        )

    def generate_voice(self, agent, task: Task):

        return Task(
            description="Based on Product Script Writer result, generate the script voice ",
            expected_output="file path url .mp3 files",
            agent=agent,
            callback=self.update_info,
            context=[task],
            tools=[self.generate_voice_tool],

        )

    def generate_image(self, agent, task: Task):
        return Task(
            description="Based on Product Script Writer result, Generate image for the script",
            expected_output="images in file",
            agent=agent,
            callback=self.update_info,
            context=[task],
            tools=[self.generate_image_tool]
        )

    def generate_video(self, agent, task: Task):
        return Task(
            description="Based on Product Script Writer result ,create video",
            expected_output="mp4 files",
            agent=agent,
            callback=self.update_info,
            context=[task],
            tools=[self.videoMaker_tool]

        )
