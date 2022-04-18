from email import message
from platform import release
import pyxel as px
from lib import Number

class MainMenu:
    starting_time: Number
    selected: int

    def __init__(self) -> None:
        self.action = [self.start_game, self.quit]

    def draw(self):
        messages = [
            "The more you try, the easier it is, ",
            "mostly",
            "",
            "long press on space for next item",
            "short press to select",
            "then, space to jump"
        ]
        for i in range(len(messages)):
            px.text(10, 10 + i * 10, messages[i], px.COLOR_RED)

        px.rect(10, 27 + i * 10 + 10 * self.selected, px.width - 20, 10, px.COLOR_WHITE)
        px.text(10, 30 + i * 10, "start game", px.COLOR_DARK_BLUE)
        px.text(10, 40 + i * 10, "quit", px.COLOR_DARK_BLUE)

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

    def reset(self, score) -> None:
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
        px.text(10, 45, "Victory !", px.COLOR_RED)
        px.text(10, 55, f"Total Death Count: {self.score}", px.COLOR_RED)
        px.text(10, 80, "Space to start agaim", px.COLOR_RED)

    def udpate(self) -> None:
        if px.btnp(px.KEY_SPACE):
            self.again = True

    def victory(self) -> bool:
        return self.again

    def defeat(self) -> bool:
        return False

    def reset(self, score) -> None:
        self.again = False
        self.score = score
