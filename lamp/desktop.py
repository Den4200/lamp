import arcade

from lamp import config
from lamp.taskbar import TaskBar
from lamp.window import Window
from lamp.utils import SimpleSpriteList


class Desktop(arcade.View):

    def __init__(self) -> None:
        super().__init__()

        self.windows = SimpleSpriteList()

        self.background = arcade.load_texture(
            f"sys/{config['desktop']['background']}"
        )
        self.taskbar = TaskBar()
        # here for testing purposes
        self.test_window = Window(self, 'Test Window')
        self.windows.append(self.test_window)

    def on_draw(self) -> None:
        super().on_draw()

        arcade.draw_lrwh_rectangle_textured(
            bottom_left_x=0,
            bottom_left_y=0,
            width=int(config['window']['x']),
            height=int(config['window']['y']),
            texture=self.background
        )
        self.taskbar.draw()
        self.windows.draw()

    def on_update(self, delta_time) -> None:
        self.windows.update()
        self.taskbar.update()
