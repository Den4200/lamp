from datetime import datetime

import arcade

from lamp import config


class TaskBar:

    def __init__(self, desktop) -> None:
        self.desktop = desktop
        self.window_icons = dict()

        self.widgets = list()

        self.center_x = int(config['window']['x']) / 2
        self.center_y = int(config['window']['y']) - (int(config['window']['y']) - 24)

        self.bar = arcade.create_rectangle_filled(
            center_x=self.center_x,
            center_y=self.center_y,
            width=int(config['window']['x']),
            height=48,
            color=(0, 0, 0, 120)
        )

        self.datetime_text = datetime.now().strftime(r'%I:%M %p | %d/%m/%Y')
        self.datetime = arcade.draw_text(
            self.datetime_text,
            start_x=int(config['window']['x']) - 84,
            start_y=self.center_y,
            font_size=12,
            color=arcade.color.WHITE,
            align='center',
            anchor_x='center',
            anchor_y='center'
        )
        self.widgets.append(self.datetime)

    def draw(self) -> None:
        self.bar.draw()

        for widget in self.widgets:
            widget.draw()

        for icon in self.window_icons.values():
            icon.draw()

    def add_window_icon(self, name, sprite) -> None:
        self.window_icons[name] = arcade.Sprite(
            'sys/lamp/default-window-icon.png',
            center_x=(len(self.window_icons) + 1) * 48 - 24,
            center_y=self.center_y,
            image_width=48,
            image_height=48
        )

    def on_update(self, delta_time) -> None:
        prev_datetime = datetime.strptime(self.datetime_text, r'%I:%M %p | %d/%m/%Y')
        now_datetime = datetime.strptime(
            datetime.strftime(datetime.now(), r'%I:%M %p | %d/%m/%Y'), r'%I:%M %p | %d/%m/%Y'
        )
        if prev_datetime != now_datetime:
            self.datetime_text = datetime.strftime(now_datetime, r'%I:%M %p | %d/%m/%Y')
            self.sprites.remove(self.datetime)

            self.datetime = arcade.draw_text(
                self.datetime_text,
                start_x=int(config['window']['x']) - 84,
                start_y=int(config['window']['y']) - (int(config['window']['y']) - 24),
                font_size=12,
                color=arcade.color.WHITE,
                align='center',
                anchor_x='center',
                anchor_y='center'
            )
            self.sprites.append(self.datetime)

        for widget in self.widgets:
            widget.on_update(delta_time)

        for icon in self.window_icons.values():
            icon.on_update(delta_time)
