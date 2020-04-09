import arcade

from lamp import config
from lamp.utils import SimpleSpriteList


class CloseButton(arcade.gui.TextButton):

    def __init__(self, window, center_x: float, center_y: float) -> None:
        super().__init__(center_x, center_y, 48, 32, 'X')
        self.window = window

    def on_press(self) -> None:
        self.window.close()


class FillButton(arcade.gui.TextButton):

    def __init__(self, window, center_x: float, center_y: float) -> None:
        super().__init__(center_x, center_y, 48, 32, '[ ]')
        self.window = window
        self.is_full = True

    def on_press(self) -> None:
        if self.is_full:
            self.is_full = False
            self.window.unfill_screen()
        else:
            self.is_full = True
            self.window.fill_screen()


class MinimizeButton(arcade.gui.TextButton):

    def __init__(self, window, center_x: float, center_y: float) -> None:
        super().__init__(center_x, center_y, 48, 32, '-')
        self.window = window

    def on_press(self) -> None:
        self.window.minimize()


class Window:

    def __init__(self, desktop, name: str) -> None:
        self.desktop = desktop
        self.name = name

        self.center_x = int(config['window']['x']) / 2
        self.center_y = (int(config['window']['y']) - (48 + 32)) / 2 + 48

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

        buttons = (
            ('close_button', CloseButton),
            ('fill_button', FillButton),
            ('minimize_button', MinimizeButton)
        )

        for idx, button in enumerate(buttons):
            name, button = button

            button = button(
                window=self,
                center_x=int(config['window']['x']) + 24 - (idx + 1) * 48,
                center_y=int(config['window']['y']) - 16
            )

            self.ui.append(button)
            self.desktop.button_list.append(button)

            setattr(self, name, button)

        self.screen_background = arcade.create_rectangle_filled(
            center_x=self.center_x,
            center_y=self.center_y,
            width=int(config['window']['x']),
            height=int(config['window']['y']) - (48 + 32),
            color=(60, 60, 60, 255)
        )
        self.ui.append(self.screen_background)

    def close(self) -> None:
        self.ui.clear()
        self.desktop.button_list.remove(self.close_button)
        self.desktop.windows.remove(self)

    def fill_screen(self) -> None:
        pass

    def unfill_screen(self) -> None:
        pass

    def minimize(self) -> None:
        pass

    def unminimize(self) -> None:
        pass

    def draw(self) -> None:
        self.ui.draw()

    def update(self) -> None:
        pass
