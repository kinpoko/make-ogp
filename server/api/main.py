from typing import Optional

from fastapi import FastAPI, Response, Path, Query
from fastapi.responses import FileResponse


from .image import make_og_image, template_name

app = FastAPI()


@app.get("/{title}.png")
def og_image( 
    title: str,
    template: str = Query("default")):

    title.encode('utf-8')
    
    if template in template_name:  
        ogp_image = make_og_image(title, template)
        
        return Response(content=ogp_image, media_type="image/png")

    else:
        return {"template":"notfound"}
    