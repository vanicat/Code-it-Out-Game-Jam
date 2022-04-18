from platform import release
import pyxel as px
from lib import Number

class MainMenu:
    starting_time: Number
    selected: int

    def __init__(self) -> None:
        self.action = [self.start_game, self.quit]

    def draw(self):
        px.text(10, 10, "long press on space for next item", px.COLOR_RED)
        px.text(10, 20, "short press to select", px.COLOR_RED)

        px.rect(10, 47 + 10 * self.selected, px.width - 20, 10, px.COLOR_WHITE)
        px.text(10, 50, "start game", px.COLOR_RED)
        px.text(10, 60, "quit", px.COLOR_RED)

    def udpate(self) -> None:
        if px.frame_count > self.starting_time + 5:
            if px.btnp(px.KEY_SPACE):
                self.start_press = px.frame_count

            if px.btn(px.KEY_SPACE):
                time = px.frame_count - self.start_press
                if time > 15:
                    self.selected = (self.selected + 1) % len(self.action)
                    self.start_press = px.frame_count

            if px.btnr(px.KEY_SPACE):
                time = px.frame_count - self.start_press
                if time < 10:
                    self.action[self.selected]()

    def start_game(self) -> None:
        self.started = True

    def quit(self) -> None:
        px.quit()

    def reset(self) -> None:
        self.selected = 0

        self.started = False
        self.starting_time = px.frame_count

    def victory(self) -> bool:
        return self.started

    def defeat(self) -> bool:
        return False

class Victory:
    def __init__(self) -> None:
        pass

    def draw(self) -> None:
        px.text(10, 50, "Victory !", px.COLOR_RED)
        px.text(10, 60, "Space to start agaim", px.COLOR_RED)

    def udpate(self) -> None:
        if px.btnp(px.KEY_SPACE):
            self.again = True

    def victory(self) -> bool:
        return self.again

    def defeat(self) -> bool:
        return False

    def reset(self) -> None:
        self.again = False
