from typing import Optional

from fastapi import FastAPI, Response, Query
import urllib.parse

from .image import make_og_image, template_name

app = FastAPI()


@app.get("/{title}.png")
def og_image( 
    title: str,
    template: str = Query("default")):

    title = urllib.parse.unquote(title)
    
    if template in template_name:  
        ogp_image = make_og_image(title, template)
        
        return Response(content=ogp_image, media_type="image/png")

    else:
        return {"template":"notfound"}
    