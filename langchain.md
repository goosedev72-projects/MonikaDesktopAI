Project Path: MonikaDesktopAI

Source Tree:

```
MonikaDesktopAI
├── config.py
├── window.py
├── langchain.md
├── __pycache__
│   ├── config.cpython-313.pyc
│   ├── window.cpython-312.pyc
│   ├── window.cpython-313.pyc
│   ├── config.cpython-312.pyc
│   ├── utils.cpython-312.pyc
│   └── utils.cpython-313.pyc
├── utils.py
├── main.py
└── assets
    ├── Expression.png
    ├── happy.png
    ├── good.png
    ├── ComicSans.ttf
    ├── cheerful.png
    ├── sad.png
    ├── not-good.png
    ├── gasp.png
    ├── shy.png
    ├── not-so-good.png
    ├── sorry.png
    ├── scared.png
    ├── what-calm.png
    ├── base.png
    ├── normal.png
    ├── worrying.png
    ├── worried.png
    ├── thanks.png
    ├── bad.png
    ├── what.png
    ├── very-happy.png
    └── not-calm.png

```

`/Users/goosedev72/making-zone/MonikaDesktopAI/config.py`:

```py
from appdirs import user_data_dir
import os
# Конфигурационные параметры приложения

app_name = "MonikaDesktopAI"
app_author = "GooseDev72"

# Пути к ресурсам
data_dir = user_data_dir(app_name, app_author)
assets_dir = os.path.join(os.path.dirname(__file__), "assets")
output_file = os.path.join(data_dir, "output.png")
```

`/Users/goosedev72/making-zone/MonikaDesktopAI/window.py`:

```py
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from config import output_file

app = QtWidgets.QApplication(sys.argv)

class TransparentWindow(QtWidgets.QWidget):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.image_path = image_path
        self.image = QtGui.QPixmap(image_path)
        self.move_to_right_bottom()  # <-- Переместить в правый нижний угол
        self.watch_file_for_changes()
        self.initUI()
        
    def initUI(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setStyleSheet("background-color: transparent; border: none;")
        self.setFixedSize(500, 500)  # Установите фиксированный размер окна

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        scaled_image = self.image.scaled(self.width(), self.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        painter.drawPixmap(0, 0, scaled_image)

    def watch_file_for_changes(self):
        self.file_watcher = QtCore.QFileSystemWatcher([self.image_path])
        self.file_watcher.fileChanged.connect(self.update_image)

    def update_image(self, path=None):
        if path is None:
            path = self.image_path
        if path == self.image_path:
            self.image = QtGui.QPixmap(self.image_path)
            self.update()

    def move_to_right_bottom(self):
        screen_geometry = QtWidgets.QApplication.desktop().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        self.move(screen_width - self.width(), screen_height - self.height())

class ExpressionWindow(QtWidgets.QWidget):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.image_path = image_path
        self.image = QtGui.QPixmap(image_path)
        self.move_to_right_bottom()  # <-- Переместить выше основного окна
        self.initUI()
        self.watch_file_for_changes()

    def initUI(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setStyleSheet("background-color: transparent; border: none;")
        self.setFixedSize(400, 100)  # Размер окна для выражения

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        scaled_image = self.image.scaled(self.width(), self.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        painter.drawPixmap(0, 0, scaled_image)

    def watch_file_for_changes(self):
        self.file_watcher = QtCore.QFileSystemWatcher([self.image_path])
        self.file_watcher.fileChanged.connect(self.update_image)

    def update_image(self, path=None):
        if path is None:
            path = self.image_path
        if path == self.image_path:
            self.image = QtGui.QPixmap(self.image_path)
            self.update()

    def move_to_right_bottom(self):
        screen_geometry = QtWidgets.QApplication.desktop().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        self.move(screen_width - self.width(), screen_height - self.height())
        self.raise_()  # Поднять окно над другими
        self.activateWindow()  # Активировать окно
```

`/Users/goosedev72/making-zone/MonikaDesktopAI/utils.py`:

```py
import os
from PIL import Image, ImageDraw, ImageFont
from config import data_dir
from config import assets_dir, output_file
import subprocess
from window import TransparentWindow

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

def empty_expression(output_image_path):
    """
    Генерирует пустое выражение (пустую картинку) и сохраняет его по указанному пути.
    """
    output_empty_path = os.path.join(assets_dir, "output_expression.png")
    create_empty_image(output_empty_path, size=(400, 100), color=(255, 255, 255))
    return output_image_path
```

`/Users/goosedev72/making-zone/MonikaDesktopAI/main.py`:

```py
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from window import TransparentWindow, ExpressionWindow
from utils import render_face, expression, empty_expression
from config import output_file, data_dir, assets_dir
import os

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TransparentWindow(os.path.join(data_dir, "output.png"))
    window.show()

    empty_path = os.path.join(data_dir, "output_expression.png")
    expression_window = ExpressionWindow(empty_path)
    expression_window.show()
    
    render_face('normal')
    
    sys.exit(app.exec_())
```