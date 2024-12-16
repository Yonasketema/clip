import os
import json
from pathlib import Path
from crewai_tools import BaseTool
from faster_whisper import WhisperModel
from utils import split_text_into_lines
from openai import OpenAI
from typing import Any

# class BaseT


class AppBaseTool(BaseTool):
    crew_id: str = ""
    pass


class VoiceGenerator(AppBaseTool):

    name: str = "voice generator"
    description: str = """
        Generates an voice for a given script
        Using the OpenAI voice generation API,
        saves it in the current audios folder.
        and create voice timestamps


        Args:
           self: self is not required positional argument: 'self' is the instance of a python class
           script:  the product script as a string.
        Returns:
            The extracted video path as a string, or None if the URL is invalid.
        """

    def __init__(self, crew_id, **kwargs):
        super().__init__(**kwargs)
        if crew_id is not None:
            self.crew_id = crew_id

    def _run(self, script: str, **kwargs: Any) -> str:

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        voice_file_path = Path(__file__).parent.parent / \
            f"audios/{self.crew_id}_audio.mp3"
        json_file_path = Path(__file__).parent.parent / \
            f"data/{self.crew_id}_data.json"

        response = client.audio.speech.create(
            model="tts-1",
            voice="onyx",
            input=f'{script}'
        )

        response.stream_to_file(voice_file_path)

        model_size = "base"
        model = WhisperModel(model_size)

        segments, info = model.transcribe(
            f'{voice_file_path}', word_timestamps=True)

        wordlevel_info = []

        for segment in segments:
            for word in segment.words:
                wordlevel_info.append(
                    {'word': word.word, 'start': word.start, 'end': word.end})

        # split_text_into_lines(wordlevel_info)

        subWord = split_text_into_lines(wordlevel_info)

        with open(json_file_path, "w") as file:
            json.dump(subWord, file)

        return voice_file_path
