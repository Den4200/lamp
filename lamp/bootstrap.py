import time

import arcade

from lamp import config
from lamp.desktop import Desktop


class BootStrap(arcade.View):

    def __init__(self) -> None:
        super().__init__()

        self.logo = arcade.draw_text(
            config['sysinfo']['os'],
            int(config['window']['x']) / 2,
            int(config['window']['y']) / 2,
            color=arcade.color.WHITE,
            font_size=32,
            bold=True,
            align='center',
            anchor_x='center',
            anchor_y='center'
        )
        self.start_time = time.time()

    def on_draw(self) -> None:
        arcade.start_render()

        super().on_draw()
        self.logo.draw()

    def on_update(self, delta_time) -> None:
        # simulate a 2 second boot up time
        if time.time() - self.start_time >= 2:
            self.window.show_view(Desktop())
