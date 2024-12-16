from tasks import TiktokTasks
from agents import TiktokAgent
from crewai import Crew
from fastapi import HTTPException
import requests
from dotenv import load_dotenv
load_dotenv()


def tiktok_video_creator(crew_id, url="", ProductName="", description="", page=""):
    tasks = TiktokTasks(crew_id, url, ProductName, description, page)
    agents = TiktokAgent()

    print("## Welcome to the CrewTikTok")
    print('-------------------------------')

    # task_list =

    # Create Agents
    research_product_agent = agents.research_product_agent()
    product_script_writer = agents.product_script_writer()
    voice_generator_agent = agents.voice_generator_agent()
    image_generator_agent = agents.image_generator_agent()
    video_maker_agent = agents.video_maker_agent()

    # Create Tasks
    product_list = tasks.product_list(research_product_agent)
    write_script = tasks.write_script(product_script_writer, product_list)
    voice_generator = tasks.generate_voice(voice_generator_agent, write_script)
    generate_image = tasks.generate_image(image_generator_agent, write_script)
    video_maker = tasks.generate_video(video_maker_agent, write_script)

    crew = Crew(
        agents=[
            research_product_agent,
            product_script_writer,
            voice_generator_agent,
            image_generator_agent,
            video_maker_agent
        ],
        tasks=[
            product_list,
            write_script,
            voice_generator,
            generate_image,
            video_maker

        ],
        verbose=3,
        # process='hierarchical'

    )

    # Create Necessary Folders
    # os.makedirs("audio/")
    # os.makedirs("images/")
    # os.makedirs("videos/")
    try:

        result = crew.kickoff()
        return result

    except Exception as e:
        print(f'Crew ERROR : {e}')
        print(e)

        data = {
            "status": "ERROR",
            "event_message": f'ERROR: {e}',
            "output": ""
        }

        try:
            response = requests.post(
                f'http://localhost:3000/api/{crew_id}', json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=str(e))
