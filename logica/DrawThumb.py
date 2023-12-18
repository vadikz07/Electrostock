from PIL import Image, ImageDraw, ImageFont
import os

class DrawThumb:
    def __init__(self, num, name, model, imgpath) -> None:
        print('inicializando draw')
        self.num = num
        self.name = name
        self.model = model
        self.imgpath = imgpath
        if num and name and model and imgpath:
            self.create_img()
        
    def create_img(self):
        width, height = 400, 200
        image = Image.new("RGB", (width, height), "white") #base
        drawing = ImageDraw.Draw(image)
        font_bold = ImageFont.truetype('arialbd.ttf', size=20)
        font = ImageFont.truetype('arial.ttf',size=14)
        drawing.text((10, 10), f"Nombre: {self.name}", fill="black", font=font_bold)
        drawing.text((10, 40), f"Modelo: {self.model}", fill="black", font=font)
        if self.imgpath != 'Sin imagen':
            img_component = Image.open(self.imgpath)
            image.paste(img_component, (10,70))
        if not os.path.exists('output_images'):
            os.makedirs('output_images')
        image.save(f'output_images/ImagenCajon{self.num}.png')
        image.show()
        
        