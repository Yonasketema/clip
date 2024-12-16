from fastapi import FastAPI, BackgroundTasks
from fastapi import FastAPI, BackgroundTasks, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta

from main import tiktok_video_creator

from fastapi import HTTPException
import requests


app = FastAPI()
scheduler = AsyncIOScheduler()


app.mount(
    "/images", StaticFiles(directory="tiktok/images"), name="images")

app.mount(
    "/audios", StaticFiles(directory="tiktok/audios"), name="audios")

app.mount(
    "/videos", StaticFiles(directory="tiktok/videos"), name="videos")

origins = [
    "http://localhost",
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# async def main(crew_id, background_tasks: BackgroundTasks, image: UploadFile = File(...), video: UploadFile = File(...), ProductName: str = Form(...), description: str = Form(...), url: str = Form(...)):
@app.post("/create/{crew_id}")
async def main(crew_id, request: Request, background_tasks: BackgroundTasks):
    form = await request.form()

    ProductName = form.get("ProductName")
    description = form.get("description")
    interval_hours = int(form.get('interval')) or 0
    videoNumber = int(form.get('videoNumber')) or 1
    page = form.get('page')
    url = form.get("url")

    image = form.get("image")
    video = form.get("video")
    # print(f"""

    #     XXXXXXXXXXXXXXXXXXX
    #       {image}

    #       {video}

    #   """)

    interval_minutes = interval_hours * 60

    if image and video:

        with open(f'tiktok/upload/{crew_id}_image.png', "wb") as f:
            contents = await image.read()
            f.write(contents)

        with open(f'tiktok/upload/{crew_id}_video.mp4', "wb") as f:
            contents = await video.read()
            f.write(contents)

    try:
        if all(string for string in [ProductName, description, url]):

            background_tasks.add_task(
                tiktok_video_creator, crew_id, url, ProductName, description, page)

            scheduler.add_job(tiktok_video_creator, "interval",  minutes=interval_minutes, args=[
                              crew_id, url, ProductName, description, page], kwargs={}, max_instances=videoNumber)

        else:
            background_tasks.add_task(tiktok_video_creator, crew_id, page)

        return {"message": f"Video generation started. {videoNumber} videos will be generated with an interval of {interval_minutes} minutes."}

    except Exception as e:
        print(f'error on main crew {e}')


@app.on_event("shutdown")
async def shutdown_event():
    scheduler.shutdown()


@app.on_event('startup')
async def startup_jobs():
    scheduler.start()
