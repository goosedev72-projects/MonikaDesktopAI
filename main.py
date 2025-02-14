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
    empty_expression()
    
    sys.exit(app.exec_())