import os
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from .lib import fw_wrap

CURRENT_DIR = os.path.dirname(__file__)

template_name = [
    "default",
    "kinpokoblog"
]

font_file_name = "NotoSansJP-Medium.otf"
font_size = 50
font_color = (0, 0, 0)

def make_og_image(title: str, template: str) -> bytes:
    
    template_image_path : str = os.path.join(CURRENT_DIR, f"template/{template}.png")
    font_path : str = os.path.join(CURRENT_DIR, f"font/{font_file_name}")

    output_image = Image.open(template_image_path).copy()
    imgWidth, imgHeight = output_image.size
    draw = ImageDraw.Draw(output_image)
    font = ImageFont.truetype(font_path, font_size)
    title_list = fw_wrap(title, 34)

    if len(title_list) == 1:
        draw.text(((imgWidth - draw.textsize(title, font=font)[0]) / 2, (imgHeight / 2) - (draw.textsize(title, font=font)[1] / 2) - font_size), title, font_color, font=font)

    elif len(title_list) == 2:
        draw.text(((imgWidth - draw.textsize(title_list[0], font=font)[0]) / 2, (imgHeight / 2) - draw.textsize(title_list[0], font=font)[1] - font_size), title_list[0], font_color, font=font)
        draw.text(((imgWidth - draw.textsize(title_list[1], font=font)[0]) / 2, (imgHeight / 2) + draw.textsize(title_list[1], font=font)[1] - font_size), title_list[1], font_color, font=font)

    else:
        title_list[2] = "..."
        draw.text(((imgWidth - draw.textsize(title_list[0], font=font)[0]) / 2, (imgHeight / 2) - draw.textsize(title_list[0], font=font)[1] - font_size), title_list[0], font_color, font=font)
        draw.text(((imgWidth - draw.textsize(title_list[1], font=font)[0]) / 2, (imgHeight / 2) - font_size), title_list[1], font_color, font=font)
        draw.text(((imgWidth - draw.textsize(title_list[2], font=font)[0]) / 2, (imgHeight / 2) ), title_list[2], font_color, font=font)

    buffer = BytesIO()
    output_image.save(buffer, format="png")
    
    return buffer.getvalue()
