import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton, QVBoxLayout, QWidget
from PyQt5 import uic
class Camera:
    def __init__(self, cam_num):

        self.cam_num = cam_num

        self.cap = None

    def initialize(self):
        self.cap = cv2.VideoCapture(self.cam_num)

    def get_frame(self):
        ret, self.last_frame = self.cap.read()
        return self.last_frame

    def acquire_movie(self, num_frames):
        movie = []
        for _ in range(num_frames):
            movie.append(self.get_frame())
        return movie

    def set_brightness(self, value):
        pass

    def __str__(self):
        return 'OpenCV Camera {}'.format(self.cam_num)

    def close_camera(self):
        self.cap.release()

if __name__ == '__main__':
    cam = Camera(0)
    cam.initialize()
    print(cam)
    frame = cam.get_frame()
    print(frame)
    cam.close_camera()