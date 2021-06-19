from typing import Optional

from fastapi import FastAPI, Request,Response, Query
from fastapi.templating import Jinja2Templates

import urllib.parse

from .image import make_og_image, template_image_name

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

@app.get("/{title}.png")
def og_image( 
    title: str,
    template: str = Query("default")):

    title = urllib.parse.unquote(title)
    
    if template in template_image_name:  
        ogp_image = make_og_image(title, template)
        
        return Response(content=ogp_image, media_type="image/png")

    else:
        return {"template":"notfound"}
    