import sys
from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
import requests


class MainWindow(QMainWindow):
    g_map: QLabel

    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.press_delta = 0.005

        self.map_zoom = 10
        self.map_ll = [37.615, 55.752]
        self.map_l = 'map'
        self.map_key = ''

        self.refresh_map()

    def refresh_map(self):
        map_params = {'ll': ','.join(map(str, self.map_ll)), 'l': self.map_l, 'z': self.map_zoom}
        map_api_server = 'https://static-maps.yandex.ru/1.x/'
        respons = requests.get(map_api_server, params=map_params)
        pixmap = QImage()
        pixmap.loadFromData(respons.content)
        self.g_map.setPixmap(QPixmap.fromImage(pixmap))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
