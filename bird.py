# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, load_font
from state_machine import *
from ball import Ball
import game_world
import game_framework

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Bird:

    def __init__(self):
        self.x, self.y = 400, 300
        self.face_dir = 1
        self.frame = 0
        self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        if self.x >= 750:
            self.face_dir = -1
        elif self.x <= 50:
            self.face_dir = 1
        self.x += self.face_dir * RUN_SPEED_PPS * game_framework.frame_time

    def handle_event(self, event):
        pass

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw((int(self.frame) % 5) * (918 // 5), (int(self.frame) // 5) * (506 // 3), 100, 100, self.x, self.y)
        elif self.face_dir == -1:
            self.image.clip_composite_draw((int(self.frame) % 5) * (918 // 5), (int(self.frame) // 5) * (506 // 3), 100, 100, 0, 'v', self.x, self.y)