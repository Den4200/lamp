import arcade

from lamp import config


class BootStrap(arcade.View):

    def __init__(self) -> None:
        super().__init__()
        self.logo = arcade.draw_text(
            config['sysinfo']['os'],
            int(config['window']['x']) / 2 - 64,
            int(config['window']['y']) / 2 - 16,
            color=arcade.color.WHITE,
            font_size=32,
            bold=True
        )

    def on_draw(self):
        arcade.start_render()

        self.logo.draw()
        super().on_draw()
