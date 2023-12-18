from PIL import Image, ImageDraw, ImageFont


def generate_image(text: str) -> Image:
    img = Image.new('RGB', (400, 400), (255, 255, 255))
    img_draw = ImageDraw.Draw(img)
    img_font = ImageFont.truetype(r'./RubikLines-Regular.ttf', 40)
    img_draw.text((60, 200), text, fill='green', font=img_font)
    return img