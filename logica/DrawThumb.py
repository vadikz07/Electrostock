from PIL import Image, ImageDraw, ImageFont
import os

class DrawThumb:
    size_xxl = 190
    size_bold = 45
    size_normal = 35
    def __init__(self, num, name, model, maker, imgpath) -> None:
        print('inicializando draw')
        self.num = num
        self.name = name
        self.model = model
        self.maker = maker
        self.imgpath = imgpath
        if num and name and model and imgpath:
            self.create_img()
        
    def create_img(self):
        width, height = 600, 300
        image = Image.new("RGB", (width, height), "white") #base
        drawing = ImageDraw.Draw(image)
        font_xxl = ImageFont.truetype('arialbd.ttf', size=self.size_xxl)
        font_bold = ImageFont.truetype('arialbd.ttf', size=self.size_bold)
        font_italic = ImageFont.truetype('ariali.ttf', size=self.size_normal)
        font = ImageFont.truetype('arial.ttf',size=self.size_normal)
        drawing.text((350,10), f"{self.num}", fill="black", font=font_xxl)
        drawing.text((10, 10), f"{self.name}", fill="black", font=font_bold)
        drawing.text((10, 80), f"{self.model}", fill="black", font=font)
        if self.maker != "":
            drawing.text((250,210), 'Fabricante:', fill="grey", font=font)
            drawing.text((250,250), f"{self.maker.upper()}",fill="black", font=font_italic)
        
        if self.imgpath != 'Sin imagen': # RUTA A IMAGEN ENCONTRADA
            img_component = Image.open(self.imgpath)
            img_component.thumbnail((160, 160))
            image.paste(img_component, (10,130))
        if not os.path.exists('output_images'):
            os.makedirs('output_images')
        image.save(f'output_images/ImagenCajon{self.num}.png')
        image.show()
        
        