# Проверка и корректировка размеров изображения
def check_image_dimensions(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        if width < 10 or height < 10 or width > 10000 or height > 10000:
            new_width = min(max(width, 10), 10000)
            new_height = min(max(height, 10), 10000)
            img = img.resize((new_width, new_height))
            img.save(image_path)
