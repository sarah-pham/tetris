import pygame
from pygame import QUIT, KEYDOWN, KEYUP, K_ESCAPE, K_LEFT, K_RIGHT, K_DOWN, K_SPACE, K_UP, K_z
from pygame.event import Event
from enum import Enum
from config import INTIAL_REPEAT_DELAY

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
    key_action_map = {
        K_LEFT: Action.LEFT,
        K_RIGHT: Action.RIGHT,
        K_DOWN: Action.DOWN,
        K_SPACE: Action.DROP,
        K_UP: Action.ROTATE_RIGHT,
        K_z: Action.ROTATE_LEFT,
        K_ESCAPE: Action.TOGGLE_PAUSE
    }

    def __init__(self) -> None:
        self.held_key = False
        self.num_events_skipped = 0

    def handle_events(self) -> list[Action]:
        actions = []
        for event in pygame.event.get():
            if event.type == QUIT:
                actions.append(Action.QUIT)
            elif event.type == KEYDOWN:
                self.handle_key_down(actions, event)
            elif event.type == KEYUP:
                self.held_key = False
                self.num_events_skipped = 0

        return actions

    def handle_key_down(self, actions: list[Action], event: Event) -> None:
        if event.key not in EventHandler.key_action_map:
            return

        if self.held_key:
            if event.key not in [K_LEFT, K_RIGHT, K_DOWN]:
                return
            if self.num_events_skipped < INTIAL_REPEAT_DELAY:
                self.num_events_skipped += 1
                return

        actions.append(EventHandler.key_action_map[event.key])
        self.held_key = True