from fastapi import FastAPI
from apps.media_resource.viewsets import resource

# from travel_of_the_life.config import CONFIG

app = FastAPI()

app.include_router(resource.router)
