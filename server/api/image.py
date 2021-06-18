import os
from PIL import Image  
from io import BytesIO
import base64

CURRENT_DIR = os.path.dirname(__file__)

template_name = [
    "default",
    "kinpokoblog"
]

def make_og_image(title: str, template: str) -> str:
    if template == "default":
        return 
    else:
        template_image_path : str = os.path.join(CURRENT_DIR, f"template/{template}.png")
        template_image = Image.open(template_image_path).copy()
        buffer = BytesIO()
        template_image.save(buffer, format="png")
        opg_img_str = base64.b64encode(buffer.getvalue()).decode("ascii")

        return opg_img_str

