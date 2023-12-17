import os
from os import path
from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
def add_watermark(dir_path):

    for item in os.walk(dir_path):
        fld = item[0]
        for file in item[2]:
            image_path = ''.join([fld, '\\', file])
            print(image_path + '...')
            image = Image.open(image_path).convert("RGBA")
            txt = Image.new('RGBA', image.size, (0,0,0,0))

            width, height = image.size
            font_size=int(width/25)
            font_path = path.join(BASE_DIR, 'fonts\\Alverata-Bold.ttf')
            
            font = ImageFont.truetype(font_path, font_size)
            d = ImageDraw.Draw(txt)    

            x, y = int(width/2), int(height/2)
            d.text((x,y), "MOMBASA CAR MARKET", fill=(0, 0, 0, 15), stroke_width=1, stroke_fill=(0, 0, 0, 130), font=font, anchor='ms')
            combined = Image.alpha_composite(image, txt)    

            combined.save(image_path, format="PNG")

dir_path = r'C:\_Django\env_msa_car_market_com\msa-car-market-com\media\cache'
add_watermark(dir_path)
