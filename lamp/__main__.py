import arcade

from lamp import config
from lamp.bootstrap import BootStrap


def main():
    window = arcade.Window(
        int(config['window']['x']),
        int(config['window']['y']),
        config['sysinfo']['os']
    )
    window.show_view(BootStrap())
    arcade.run()


if __name__ == "__main__":
    main()
