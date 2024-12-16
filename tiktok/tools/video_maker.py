import json
from crewai_tools import BaseTool
from typing import Any
from movie import compose_video
from pathlib import Path
from config.conf import BASE_DIR
# from tk_uploader.main import tiktok_setup, TiktokVideo
from tiktokUploader.main_chrome import tiktok_setup, TiktokVideo
from config.files_times import generate_schedule_time_next_day
import asyncio


class AppBaseTool(BaseTool):
    crew_id: str = ""
    title: str = ""
    pass


class VideoMakerGenerator(AppBaseTool):
    name: str = "video maker"
    description: str = """
        Args:
           self: self is not required positional argument: 'self' is the instance of a python class
           script:  the product script as a string.
        Returns:
            The extracted Video path as a string, or None if the URL is invalid.
        """

    def __init__(self, crew_id, title, ** kwargs):
        super().__init__(**kwargs)
        if crew_id is not None:
            self.crew_id = crew_id
            self.title = title

    def _run(self, script: str, **kwargs: Any) -> str:
        json_file_path = f"tiktok/data/{self.crew_id}_data.json"

        with open(json_file_path, "r") as file:
            # Load  the  script JSON data from the file
            split_text_into_lines = json.load(file)

        final_video = compose_video(
            split_text_into_lines, f"{self.crew_id}_audio", self.crew_id)
        filepath = Path(BASE_DIR) / "videos/{self.crew_id}_output.mp4"
        account_file = Path(BASE_DIR / "tiktokUploader" / "account.json")

        # publish_datetimes = generate_schedule_time_next_day(
        #     file_num, 1, daily_times=[16])
        cookie_setup = asyncio.run(tiktok_setup(account_file, handle=True))

        tags = ['new']
        print('[-] start uploading .....')
        app = TiktokVideo(self.title, filepath, tags,
                          0, account_file)
        asyncio.run(app.main(), debug=False)

        return '[-] finish uploading .....'
