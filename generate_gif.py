import random
import string

from PIL import Image, ImageDraw, ImageFont


def dot(img, x, y):
    draw = ImageDraw.Draw(img)
    current_pixel = img.getpixel((x, y))
    new_pixel = 1 if current_pixel == 0 else 0
    draw.point((x, y), fill=new_pixel)
    return img


def circle(img, x, y, radius):
    draw = ImageDraw.Draw(img)
    for i in range(x - radius, x + radius + 1):
        for j in range(y - radius, y + radius + 1):
            if (i - x) ** 2 + (j - y) ** 2 <= radius ** 2:
                if 0 <= i < img.width and 0 <= j < img.height:
                    current_pixel = img.getpixel((i, j))
                    new_pixel = 1 if current_pixel == 0 else 0
                    draw.point((i, j), fill=new_pixel)
    return img


def square(img, x, y, size):
    draw = ImageDraw.Draw(img)
    for i in range(x - size, x + size):
        for j in range(y - size, y + size):
            if 0 <= i < img.width and 0 <= j < img.height:
                current_pixel = img.getpixel((i, j))
                new_pixel = 1 if current_pixel == 0 else 0
                draw.point((i, j), fill=new_pixel)

    return img


def letter(img, x, y, text, size=200):
    temp_img = Image.new('1', img.size, 0)
    draw_temp = ImageDraw.Draw(temp_img)
    try:
        font = ImageFont.truetype("Arial.ttf", size)
    except IOError:
        font = ImageFont.load_default()
    draw_temp.text((x, y), text, fill=1, font=font)
    mask = temp_img.load()
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if mask[i, j] == 1:
                current_pixel = img.getpixel((i, j))
                new_pixel = 1 if current_pixel == 0 else 0
                pixels[i, j] = new_pixel

    return img


def make_gif():
    frames = []
    img = init_noise()
    frames.append(img.copy())
    x, y = 0, 0
    step = 4
    frame_count = 100
    selected_letter = random.choice(string.ascii_uppercase)
    for number in range(frame_count):
        if number == frame_count // 2:
            step *= -1
        if x >= img.width or y >= img.height:
            break
        # TODO BLINKING
        # new_frame = dot(img.copy(), x, y)
        # new_frame = circle(img.copy(), x, y, 60)
        # new_frame = square(img.copy(), x, y, 50)
        new_frame = letter(img.copy(), x, y, selected_letter)
        frames.append(new_frame)
        x += step
        y += step

    frame_one = frames[0]
    frame_one.save("test.gif", format="GIF", append_images=frames[1:], save_all=True, duration=20, loop=0)


def init_noise(seed_num: int = 1):
    random.seed(seed_num)
    image = Image.new("1", (400, 400))
    pixels = [random.randint(0, 1) for _ in range(400 * 400)]
    image.putdata(pixels)
    # image = Image.new("1", (400, 400), color=0)
    return image


if __name__ == "__main__":
    make_gif()
