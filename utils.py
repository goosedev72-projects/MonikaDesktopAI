import os
from PIL import Image, ImageDraw, ImageFont
from config import data_dir
from config import assets_dir, output_file
import subprocess
from window import TransparentWindow
import shutil

def overlay_images(background_image_path, face_image_path, output_image_path):
    """
    Накладывает изображение лица (face_image_path) на изображение фона (background_image_path)
    с заданным коэффициентом масштабирования, фиксированными координатами.
    Результат сохраняется в output_image_path.
    """
    background_picture = Image.open(background_image_path)
    face_picture = Image.open(face_image_path)

    scale_factor = 0.52
    scaled_face_picture = face_picture.resize(
        (int(face_picture.width * scale_factor), int(face_picture.height * scale_factor))
    )

    face_x, face_y = 321, 319
    face_x = max(0, min(face_x, background_picture.width - scaled_face_picture.width))
    face_y = max(0, min(face_y, background_picture.height - scaled_face_picture.height))

    if scaled_face_picture.mode!= 'RGBA':
        scaled_face_picture = scaled_face_picture.convert('RGBA')
    
    background_picture.paste(scaled_face_picture, (face_x, face_y), scaled_face_picture)
    background_picture.save(output_image_path)
    print(f"Результат сохранён как {output_image_path}")

    try:
        subprocess.run(["chafa", output_image_path])
    except FileNotFoundError:
        print("chafa не установлен или не найден. Результат сохранён, но не отображён.")

def render_face(face_expression, output_image_path=output_file):
    """
    Генерирует изображение с лицом для выбранного выражения (например, 'happy', 'angry').
    Файлы с лицами ожидаются в data_dir/assets (например, data_dir/assets/happy.png),
    для фона используется data_dir/base.png.
    """
    if output_image_path is None:
        output_image_path = os.path.join(data_dir, "output.png")
    background_image_path = os.path.join(data_dir, "base.png")
    window = TransparentWindow(output_image_path)
    assets_dir = os.path.join(data_dir, "assets")
    face_image_filename = f"{face_expression}.png"
    face_image_path = os.path.join(assets_dir, face_image_filename)

    if not os.path.exists(face_image_path):
        raise FileNotFoundError(f"Изображение лица '{face_image_path}' не найдено.")

    overlay_images(background_image_path, face_image_path, output_image_path)
    if window:
        window.update_image(output_image_path)
    else:
        print("No window provided to update.")
    return  # можно удалить, если не используется

def expression(text, output_image_path=os.path.join(data_dir, "output_expression.png")):
    # Метод для генерации изображения с текстом (выражением)
    overlay_text(text, output_image_path)
    return output_image_path

def overlay_text(text, output_image_path):
    # Ставим переменные
    base_path = os.path.join(assets_dir, "expression.png")
    font_path = os.path.join(assets_dir, "ComicSans.ttf")
    
    # Загружаем Expression
    img = Image.open(base_path)

    # Удобство работы - укороченная функция
    imgdraw = ImageDraw.Draw(img)

    # Шрифт комик санс
    myFont = ImageFont.truetype(font_path, 65)

    # Добавляем текст
    imgdraw.text((28, 36), text, font=myFont, fill=(255, 0, 0))
    
    # Сохранение
    img.save(output_image_path)

# def create_empty_image(output_path, size=(400, 100), color=(255, 255, 255)):
    # """
    # Создаёт пустое изображение заданного размера и цвета.
    # 
    # :param output_path: Путь для сохранения изображения
    # :param size: Размер изображения (ширина, высота)
    # :param color: Цвет изображения в формате RGB
    # """
    # img = Image.new('RGB', size, color)
    # img.save(output_path)

def empty_expression():
    """
    Генерирует пустое выражение (пустую картинку) и сохраняет его по указанному пути.
    """
    output_empty_path = os.path.join(assets_dir, "blank.png")
    output_empty_path_exp = os.path.join(assets_dir, "output_expression.png")
    shutil.copyfile(output_empty_path, output_empty_path_exp)
    return output_empty_path