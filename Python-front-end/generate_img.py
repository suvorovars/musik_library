from PIL import Image, ImageDraw, ImageFont


def generate_image(text: str) -> Image:
    img = Image.new(mode='RGB', size=(400, 400))
    img_draw = ImageDraw.Draw(img)
    #img_font = ImageFont.truetype(r'./UbuntuNerdFont-Bold.ttf', 20)
    img_draw.text((70, 250), text, fill='green') #font=img_font)
    return img