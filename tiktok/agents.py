from crewai import Agent
from textwrap import dedent


class TiktokAgent():
    def research_product_agent(self):
        """
          research agent
        """

        return Agent(
            role='Product Researcher',
            goal='Research HighPaid Product',
            backstory=dedent("""\
				You are a product researcher 
                You select the best and Top tiktok shop trend product """),
            allow_delegation=False,
            verbose=True,

        )

    def product_script_writer(self):
        """
          product script writer
        """

        return Agent(
            role='Product Script Writer',
            goal='Write product script for tiktok short video',
            backstory=dedent("""\
				You are a product content creator 
                You create a tiktok video for your audiences and write script for a product for the video  """),
            allow_delegation=False,
            verbose=True,

        )

    def image_generator_agent(self):
        """
          image generator
        """

        return Agent(
            role='Image Generator',
            goal='Generate image for the script',
            backstory="A creative AI specialized in visual storytelling, bringing each script to life through imagery.",
            verbose=True,
            allow_delegation=False
        )

    def voice_generator_agent(self):
        """
          voice generator
        """

        return Agent(
            role='Voice Generator',
            goal='generate script voice with mp3 file ',
            backstory="you are a narrater",
            verbose=True,
            allow_delegation=False
        )

    def video_maker_agent(self):
        """
          voice generator
        """

        return Agent(
            role='Video Editor',
            goal='tiktok shop video mp4 file',
            backstory="video editor",
            verbose=True,
            allow_delegation=False
        )

        # return Agent(
        #     role='Product Researcher',
        #     goal='Research HighPaid tiktok shop Product',
        #     backstory=dedent("""\
        # 		You are a product researcher
        #         You select the best and Top tiktok shop trend product """),
        #     allow_delegation=False,
        # 	verbose=True ,

        # )
