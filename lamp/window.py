import arcade

from lamp import config


class CloseButton(arcade.TextButton):

    def __init__(self, window, center_x: float, center_y: float) -> None:
        super().__init__(center_x, center_y, 48, 32, 'X')
        self.window = window

    def on_press(self) -> None:
        print('close!')


class Window:

    def __init__(self, desktop) -> None:
        self.desktop = desktop

        self.top_bar = arcade.create_rectangle_filled(
            center_x=int(config['window']['x']) / 2,
            center_y=int(config['window']['y']) - 16,
            width=int(config['window']['x']),
            height=32,
            color=(40, 40, 40, 255)
        )
        self.close_button = CloseButton(
            window=self,
            center_x=int(config['window']['x']) - 24,
            center_y=int(config['window']['y']) - 16
        )

        self.desktop.button_list.append(self.close_button)

    def draw(self) -> None:
        self.top_bar.draw()
        self.close_button.draw()

    def update(self) -> None:
        pass
