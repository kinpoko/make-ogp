from typing import Optional

from fastapi import FastAPI, Path, Query
from fastapi.responses import FileResponse

from .image import make_og_image, template_name

app = FastAPI()


@app.get("/{title}.png")
def og_image( 
    title: str = Path(..., max_length=50),
    template: str = Query("default")):

    title.encode('utf-8')
    
    if template in template_name:  
        opg_img = make_og_image(title, template)
        return opg_img

    else:
        return {"not":"found"}
    