from PIL import Image

def split_skybox(image_path, save_path):
    skybox_texture = Image.open(image_path)
    width, height = skybox_texture.size
    part_width = width // 4
    part_height = height // 3

    skybox_parts = []
    for row in range(3):
        for col in range(4):
            x = col * part_width
            y = row * part_height
            skybox_parts.append(skybox_texture.crop((x, y, x + part_width, y + part_height)))

    for i, part in enumerate(skybox_parts):
        if i == 1:
            part.save(f'{save_path}top.png')
        if i == 4:
            part.save(f'{save_path}left.png')
        if i == 5:
            part.save(f'{save_path}front.png')
        if i == 6:
            part.save(f'{save_path}right.png')
        if i == 7:
            part.save(f'{save_path}back.png')
        if i == 9:
            part.save(f'{save_path}bottom.png')
        # part.save(f'{save_path}skybox_{i+1}.png')


# split_skybox('textures/skybox/day/day.png','textures/skybox/day/')
split_skybox('textures/skybox/night/night.png','textures/skybox/night/')

