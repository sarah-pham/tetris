import time
from enum import Enum
import pygame
from pygame import QUIT, KEYDOWN, KEYUP, K_ESCAPE, K_LEFT, K_RIGHT, K_DOWN, K_SPACE, K_UP, K_z
from pygame.event import Event

from config import INTIAL_REPEAT_INTERVAL, REPEAT_INTERVAL

class Action(Enum):
    QUIT = 1
    LEFT = 2
    RIGHT = 3
    DOWN = 4
    DROP = 5
    ROTATE_LEFT = 6
    ROTATE_RIGHT = 7
    TOGGLE_PAUSE = 8

class EventHandler:
    def __init__(self) -> None:
        self.actions = {
            K_LEFT: Action.LEFT,
            K_RIGHT: Action.RIGHT,
            K_DOWN: Action.DOWN,
            K_SPACE: Action.DROP,
            K_UP: Action.ROTATE_RIGHT,
            K_z: Action.ROTATE_LEFT,
            K_ESCAPE: Action.TOGGLE_PAUSE
        }
        self.down_keys = []

    def get_actions(self) -> list[Action]:
        actions = []

        for event in pygame.event.get():
            if event.type == QUIT:
                actions.append(Action.QUIT)
            elif event.type == KEYDOWN:
                self.handle_key_down(actions, event)
            elif event.type == KEYUP:
                self.handle_key_up(event)

        for i, (tm, key) in enumerate(self.down_keys):
            if time.time() >= tm:
                actions.append(self.actions[key])
                self.down_keys[i][0] += REPEAT_INTERVAL

        return actions

    def handle_key_down(self, actions: list[Action], event: Event) -> None:
        if event.key not in self.actions:
            return

        actions.append(self.actions[event.key])

        if event.key in [K_LEFT, K_RIGHT, K_DOWN]:
            time_of_repeat = time.time() + INTIAL_REPEAT_INTERVAL
            self.down_keys.append([time_of_repeat, event.key])

    def handle_key_up(self, event: Event) -> None:
        if event.key not in self.actions:
            return

        for tm, key in self.down_keys:
            if key == event.key:
                self.down_keys.remove([tm, key])
