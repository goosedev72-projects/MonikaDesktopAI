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