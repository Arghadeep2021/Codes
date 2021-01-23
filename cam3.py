from PyQt5.QtWidgets import QApplication

from cam import Camera
from cam2 import StartWindow

camera = Camera(0)
camera.initialize()

app = QApplication([])
start_window = StartWindow(camera)
start_window.show()
app.exit(app.exec_())