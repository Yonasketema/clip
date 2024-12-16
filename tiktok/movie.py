
import os
from moviepy.editor import TextClip, ImageClip, CompositeVideoClip, VideoFileClip, concatenate_videoclips, AudioFileClip
import numpy as np

import platform
import sys
import subprocess
import pathlib
import captacity


def search_program(program_name):
    try:
        search_cmd = "where" if platform.system() == "Windows" else "which"
        return subprocess.check_output([search_cmd, program_name]).decode().strip()
    except subprocess.CalledProcessError:
        return None


def get_program_path(program_name):
    program_path = search_program(program_name)
    return program_path


magick_path = get_program_path("magick")
if magick_path:
    os.environ['IMAGEMAGICK_BINARY'] = magick_path


def create_caption(textJSON, framesize, font="Helvetica-Bold", fontsize=80, color='white', bgcolor='blue'):
    wordcount = len(textJSON['textcontents'])
    full_duration = textJSON['end']-textJSON['start']

    word_clips = []
    xy_textclips_positions = []

    x_pos = 0
    y_pos = 0
    # max_height = 0
    frame_width = framesize[0]
    frame_height = framesize[1]
    x_buffer = frame_width*1/10
    y_buffer = frame_height*1/5

    space_width = ""
    space_height = ""

    for index, wordJSON in enumerate(textJSON['textcontents']):
        duration = wordJSON['end']-wordJSON['start']
        word_clip = TextClip(wordJSON['word'], font=font, fontsize=fontsize, color=color).set_start(
            textJSON['start']).set_duration(full_duration)
        word_clip_space = TextClip(" ", font=font, fontsize=fontsize, color=color).set_start(
            textJSON['start']).set_duration(full_duration)
        word_width, word_height = word_clip.size
        space_width, space_height = word_clip_space.size
        if x_pos + word_width + space_width > frame_width-2*x_buffer:
            # Move to the next line
            x_pos = 0
            y_pos = y_pos + word_height+40

            # Store info of each word_clip created
            xy_textclips_positions.append({
                "x_pos": x_pos+x_buffer,
                "y_pos": y_pos+y_buffer,
                "width": word_width,
                "height": word_height,
                "word": wordJSON['word'],
                "start": wordJSON['start'],
                "end": wordJSON['end'],
                "duration": duration
            })

            word_clip = word_clip.set_position(
                (x_pos+x_buffer, y_pos+y_buffer))
            word_clip_space = word_clip_space.set_position(
                (x_pos + word_width + x_buffer, y_pos+y_buffer))
            x_pos = word_width + space_width
        else:
            # Store info of each word_clip created
            xy_textclips_positions.append({
                "x_pos": x_pos+x_buffer,
                "y_pos": y_pos+y_buffer,
                "width": word_width,
                "height": word_height,
                "word": wordJSON['word'],
                "start": wordJSON['start'],
                "end": wordJSON['end'],
                "duration": duration
            })

            word_clip = word_clip.set_position(
                (x_pos+x_buffer, y_pos+y_buffer))
            word_clip_space = word_clip_space.set_position(
                (x_pos + word_width + x_buffer, y_pos+y_buffer))

            x_pos = x_pos + word_width + space_width

        word_clips.append(word_clip)
        word_clips.append(word_clip_space)

    for highlight_word in xy_textclips_positions:

        word_clip_highlight = TextClip(highlight_word['word'], font=font, fontsize=fontsize, color=color, bg_color=bgcolor).set_start(
            highlight_word['start']).set_duration(highlight_word['duration'])
        word_clip_highlight = word_clip_highlight.set_position(
            (highlight_word['x_pos'], highlight_word['y_pos']))
        word_clips.append(word_clip_highlight)

    return word_clips


# def create_bg(split_text_into_lines, size):

#     return final_video


def compose_video(split_text_into_lines, audio, crew_id):
    frame_size = (1080, 1920)

    # all_linelevel_splits = []

    # for line in split_text_into_lines:
    #     out = create_caption(line, frame_size)

    #     all_linelevel_splits.extend(out)

    clips = []

    import random

    random_numbers = random.sample(range(3, 9), 3)
    first_number = random_numbers[0]
    second_number = random_numbers[1]
    last = random_numbers[2]

    for index, textJSON in enumerate(split_text_into_lines):
        full_duration = textJSON['end']-textJSON['start']

        clip = None

        # if first_number == index:
        #     clip = ImageClip(
        #         f"tiktok/upload/{crew_id}_image.png").set_duration(full_duration).resize(frame_size)
        #     clip = clip.set_duration(3).set_start(0)
        #     clip = clip.resize(lambda t: 1+0.05*t)
        if second_number == index:  # pexel video
            import pprint
            import requests

            from pexelsapi.pexels import Pexels
            pexel = Pexels(
                'qIscZgc6YaDnLvoozgmG9EeTpxqMImzTFjzyfmdrmV4QtWnSbWr78ZgW')
            search_videos = pexel.search_videos(
                query=textJSON['word'].strip(), orientation='portrait', size='', color='', locale='', page=1, per_page=1)
            pprint.pprint(search_videos.get('videos')[
                          0].get('video_files')[0].get('link'))

            video_url = search_videos.get('videos')[0].get(
                'video_files')[0].get('link')
            # pexel = Pexels('API_KEY')
            # get_video = pexel.get_video(search_videos.get('videos')[0].get('id'))
            # print(get_video)

            video_response = requests.get(video_url)
            if video_response.status_code == 200:
                with open(f"tiktok/upload/{crew_id}_pexelVideo.mp4", 'wb') as file:
                    file.write(video_response.content)

            clip = VideoFileClip(
                f"tiktok/upload/{crew_id}_pexelVideo.mp4").resize(frame_size).set_duration(full_duration)

        # demo_video
        elif last == index and pathlib.Path(f"tiktok/upload/{crew_id}_video.mp4").is_file():
            clip = VideoFileClip(
                f"tiktok/upload/{crew_id}_video.mp4").resize(frame_size).set_duration(full_duration)
        # demo image
        elif first_number == index and pathlib.Path(f"tiktok/upload/{crew_id}_image.png").is_file():
            clip = ImageClip(
                f"tiktok/upload/{crew_id}_image.png").set_duration(full_duration).resize(frame_size)
            clip = clip.resize(lambda t: 1+0.05*t)

        else:
            clip = ImageClip(
                f"tiktok/images/{crew_id}_image_{index}.png").set_duration(full_duration).resize(frame_size)

            clip = clip.resize(lambda t: 1+0.07*t)
            if index % 2 == 0:
                clip = clip.set_position(('center', 'center'))

        video = CompositeVideoClip([clip])

        clips.append(video)

    background_clip = concatenate_videoclips(clips, method="compose")
    # background_clip.write_videofile("bg_video.mp4", fps=24)

    print('--- ------ bg video')

    audio_clip = AudioFileClip(f"tiktok/audios/{audio}.mp3")
    audio_duration = audio_clip.duration

    print('start compose final video')
    final_video = CompositeVideoClip(
        [background_clip]).set_duration(audio_duration)
    # final_video = CompositeVideoClip([background_clip] + all_linelevel_splits)

    final_video = final_video.set_audio(audio_clip)

    final_video.write_videofile(
        f"tiktok/videos/{crew_id}_bgVideo.mp4", fps=24)
    #   codec="libx264", audio_codec="aac")

    captacity.add_captions(
        video_file=f"tiktok/videos/{crew_id}_bgVideo.mp4",
        output_file=f"tiktok/videos/{crew_id}_output.mp4",
        font="tiktok/font/Designer.otf",
        font_size=70,
        font_color="yellow",
        stroke_width=3,
        stroke_color="black",
        shadow_strength=1.0,
        shadow_blur=0.1,
        highlight_current_word=True,
        word_highlight_color="red",
        line_count=1,
        padding=50,
    )

    return 'Complete Composing Video'
