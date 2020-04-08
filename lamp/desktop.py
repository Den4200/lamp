import arcade

from lamp import config


class Desktop(arcade.View):

    def __init__(self) -> None:
        super().__init__()

        self.background = arcade.load_texture(
            f"sys/{config['desktop']['background']}"
        )

    def on_draw(self) -> None:
        super().on_draw()

        arcade.draw_lrwh_rectangle_textured(
            0, 0,
            int(config['window']['x']),
            int(config['window']['y']),
            self.background
        )
