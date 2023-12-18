from PIL import Image, ImageDraw, ImageFont

class DrawThumb:
    def __init__(self, num, name, model, imgpath) -> None:
        print('inicializando draw')
        self.num = num
        self.name = name
        self.model = model
        self.imgpath = imgpath
        
    def create_img(self):
        width, height = 400, 200
        image = Image.new("RGB", (width, height), "white") #base
        drawing = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        drawing.text((10, 10), f"Nombre: {self.name}", fill="black", font=font)
        drawing.text((10, 40), f"Modelo: {self.model}", fill="black", font=font)
        img_component = Image.open(self.imgpath)
        image.paste(img_component, (10,70))
        image.save(f'ImagenCajon{self.num}')
        image.show()
        
        