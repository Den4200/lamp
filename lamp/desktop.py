import arcade

from lamp import config
from lamp.taskbar import TaskBar
from lamp.window import Window


class Desktop(arcade.View):

    def __init__(self) -> None:
        super().__init__()

        self.windows = list()

        self.background = arcade.load_texture(
            f"sys/{config['desktop']['background']}"
        )
        self.taskbar = TaskBar(self)

        # here for testing purposes
        self.test_window = Window(self, 'Test Window')
        self.windows.append(self.test_window)
        self.taskbar.add_window_icon('Test Window', self.test_window)

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

        for window in self.windows:
            window.draw()

    def on_update(self, delta_time) -> None:
        self.taskbar.update()

        for window in self.windows:
            window.draw.on_update(delta_time)
