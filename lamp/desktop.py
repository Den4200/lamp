import arcade

from lamp import config
from lamp.window import Window


class Desktop(arcade.View):

    def __init__(self) -> None:
        super().__init__()

        self.background = arcade.load_texture(
            f"sys/{config['desktop']['background']}"
        )
        self.taskbar = arcade.create_rectangle_filled(
            center_x=int(config['window']['x']) / 2,
            center_y=int(config['window']['y']) - (int(config['window']['y']) - 24),
            width=int(config['window']['x']),
            height=48,
            color=(0, 0, 0, 120)
        )
        # here for testing purposes
        self.test_window = Window(self)

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
        self.test_window.draw()

    def on_update(self, delta_time) -> None:
        self.test_window.update()
