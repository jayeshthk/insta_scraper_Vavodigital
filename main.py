from fastapi import  FastAPI
from fastapi_utils.tasks import repeat_every
from pydantic import BaseModel
from caption import insta_posts
from optional_scrawl import optional_scrawl
import uvicorn

app=FastAPI(title='Insta_collector',debug=True)

@app.get('/')
async def basic():
    return 'Welcome to insta-collector by @jayeshthk'

#defining basemodel json object
class InstaCollectir(BaseModel):
    username:str
    is_save:bool


#by default we are running once a day you can set n_repeat to 1 or 2 or as per your desire.
n_repeat=1
@app.on_event("startup")
@repeat_every(seconds=int(86400/n_repeat))
def insta_collector(payload: InstaCollectir):
    username=payload.username
    try:
        insta_posts(TARGET=username,save=False)
    except:
        optional_scrawl(username=username)

#optional API method for custom runs.
@app.post('/insta_collector')
def insta_collector(payload: InstaCollectir):
    username=payload.username
    is_save=payload.is_save
    try:
        return_respo=insta_posts(TARGET=username,save=is_save)
    except:
        return_respo=optional_scrawl(username=username)

    return return_respo

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
