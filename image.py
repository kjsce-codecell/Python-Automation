from PIL import Image,ImageDraw,ImageFont
import string, random

def pass_gen(name, email, phone):
    img = Image.open("templates/pass.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("templates/Quicksand-Bold.otf", 40)

    s_path = "passes/" + email + ".png"
    if len(name) >= 18:
        name = name.split()
        name = name[0] + " " + name[1][0]

    draw.text((200, 300), name.capitalize(), font=font, fill=(255, 255, 255))
    draw.text((650, 300), phone, font=font, fill=(255, 255, 255))
    draw.text((200, 500), email.lower(), font=font, fill=(255, 255, 255))

    img.save(s_path)
    return s_path