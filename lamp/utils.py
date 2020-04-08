class SimpleSpriteList:

    def __init__(self) -> None:
        self.sprites = list()

    def draw(self) -> None:
        for sprite in self.sprites:
            sprite.draw()

    def update(self) -> None:
        for sprite in self.sprites:
            sprite.draw()

    def append(self, sprite) -> None:
        self.sprites.append(sprite)

    def remove(self, sprite) -> None:
        self.sprites.remove(sprite)

    def pop(self, index: int = -1):
        self.sprites.pop(index)
