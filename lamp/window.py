import arcade

from lamp import config
from lamp.utils import SimpleSpriteList


class CloseButton(arcade.gui.TextButton):

    def __init__(self, window, center_x: float, center_y: float) -> None:
        super().__init__(center_x, center_y, 48, 32, 'X')
        self.window = window

    def on_press(self) -> None:
        print('closing')
        self.window.close()


class Window:

    def __init__(self, desktop, name: str) -> None:
        self.desktop = desktop
        self.name = name

        self.ui = SimpleSpriteList()

        self.top_bar = arcade.create_rectangle_filled(
            center_x=int(config['window']['x']) / 2,
            center_y=int(config['window']['y']) - 16,
            width=int(config['window']['x']),
            height=32,
            color=(30, 30, 30, 255)
        )
        self.ui.append(self.top_bar)

        self.top_bar_name = arcade.draw_text(
            self.name,
            start_x=int(config['window']['x']) / 2,
            start_y=int(config['window']['y']) - 16,
            color=arcade.color.WHITE,
            font_size=12,
            align='center',
            anchor_x='center',
            anchor_y='center'
        )
        self.ui.append(self.top_bar_name)

        self.close_button = CloseButton(
            window=self,
            center_x=int(config['window']['x']) - 24,
            center_y=int(config['window']['y']) - 16
        )
        self.ui.append(self.close_button)
        self.desktop.button_list.append(self.close_button)

    def close(self) -> None:
        self.desktop.button_list.remove(self.close_button)
        self.ui.clear()

    def draw(self) -> None:
        self.ui.draw()

    def update(self) -> None:
        pass
