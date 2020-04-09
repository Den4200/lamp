from datetime import datetime

import arcade

from lamp import config
from lamp.utils import SimpleSpriteList


class TaskBar(SimpleSpriteList):

    def __init__(self) -> None:
        super().__init__()

        self.bar = arcade.create_rectangle_filled(
            center_x=int(config['window']['x']) / 2,
            center_y=int(config['window']['y']) - (int(config['window']['y']) - 24),
            width=int(config['window']['x']),
            height=48,
            color=(0, 0, 0, 120)
        )

        self.datetime_text = datetime.now().strftime(r'%I:%M %p | %d/%m/%Y')
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

    def draw(self) -> None:
        self.bar.draw()
        super().draw()

    def update(self) -> None:
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

        super().update()
