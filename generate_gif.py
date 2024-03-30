import random
from PIL import Image, ImageDraw, ImageFont


def dot(img, x, y):
    draw = ImageDraw.Draw(img)
    current_pixel = img.getpixel((x, y))
    new_pixel = 1 if current_pixel == 0 else 0
    draw.point((x, y), fill=new_pixel)
    return img


def circle(img, x, y, size=50):  # size = radius. name unification with other methods
    draw = ImageDraw.Draw(img)
    points_in_circle = ((i, j) for i in range(x - size, x + size + 1)
                        for j in range(y - size, y + size + 1)
                        if (i - x) ** 2 + (j - y) ** 2 <= size ** 2
                        and 0 <= i < img.width and 0 <= j < img.height)
    for i, j in points_in_circle:
        current_pixel = img.getpixel((i, j))
        new_pixel = 1 - current_pixel
        draw.point((i, j), fill=new_pixel)
    return img


def square(img, x, y, size=50):
    draw = ImageDraw.Draw(img)
    for i in range(x - size, x + size):
        for j in range(y - size, y + size):
            if 0 <= i < img.width and 0 <= j < img.height:
                current_pixel = img.getpixel((i, j))
                new_pixel = 1 if current_pixel == 0 else 0
                draw.point((i, j), fill=new_pixel)

    return img


def letter(img, x, y, size=200, text="A"):
    x -= size // 2  # font coordinate system are in corner
    y -= size // 2
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
                new_pixel = 1 - current_pixel
                pixels[i, j] = new_pixel

    return img


def move_variables(img):
    x = random.randint(img.width // 4, (img.width // 4) * 3)
    y = random.randint(img.height // 4, (img.height // 4) * 3)
    step_x = random.randint(1, 4)
    if x > img.width // 2:
        step_x *= -1
    step_y = random.randint(1, 4)
    if y > img.height // 2:
        step_y *= -1
    return x, y, step_x, step_y


def make_gif(random_seed=None, animation_type='move', draw_method=circle, draw_args=(50,)):
    random.seed(random_seed)
    img = init_noise()

    x, y, step_x, step_y = move_variables(img)
    frames = []
    if animation_type == 'move':
        frame_count = 100
        frame_duration = 20
        for frame in range(frame_count):
            if frame == frame_count // 2:
                step_x *= -1
                step_y *= -1
            new_frame = draw_method(img.copy(), x, y, *draw_args)
            frames.append(new_frame)
            x += step_x
            y += step_y
    if animation_type == 'blink':
        frame_duration = 100
        frames.append(img)
        new_frame = draw_method(img.copy(), x, y, *draw_args)
        frames.append(new_frame)

    frame_one = frames[0]
    frame_one.save("test.gif", format="GIF", append_images=frames[1:], save_all=True, duration=frame_duration, loop=0)


def init_noise():
    image = Image.new("1", (400, 400))
    pixels = [random.randint(0, 1) for _ in range(400 * 400)]
    image.putdata(pixels)
    return image


if __name__ == "__main__":
    # pass
    make_gif(None,'move', circle, (100,))
    # make_gif(None, 'blink', circle, (50,))

    # make_gif(None,'move', square, (50,))
    # make_gif(None,'blink', square, (100,))

    # make_gif(None,'move', letter, (350, "A"))
    # make_gif(None,'blink', letter, (150, "A"))
