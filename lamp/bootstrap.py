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
        self._delta_time = 0

    def on_draw(self) -> None:
        arcade.start_render()

        super().on_draw()
        self.logo.draw()

    def on_update(self, delta_time) -> None:
        self._delta_time += delta_time

        # simulate a 1 second boot up time
        if self._delta_time >= 1:
            self.window.show_view(Desktop())
