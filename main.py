@namespace
class SpriteKind:
    PaintBrush = SpriteKind.create()
i = 0
mySprite = sprites.create(img("""
    1
"""), SpriteKind.player)
mySprite.set_bounce_on_wall(True)
mySprite.start_effect(effects.spray)
mySprite.start_effect(effects.trail)
mySprite.start_effect(effects.fountain)
mySprite.start_effect(effects.confetti)
mySprite.start_effect(effects.hearts)
mySprite.start_effect(effects.smiles)
mySprite.start_effect(effects.rings)
mySprite.start_effect(effects.fire)
mySprite.start_effect(effects.warm_radial)
mySprite.start_effect(effects.cool_radial)
mySprite.start_effect(effects.halo)
mySprite.start_effect(effects.ashes)
mySprite.start_effect(effects.disintegrate)
mySprite.start_effect(effects.blizzard)
mySprite.start_effect(effects.bubbles)
mySprite.start_effect(effects.star_field)
mySprite.start_effect(effects.clouds)

def on_on_update():
    global i
    i += 1 # kinda hard to explain, changing to add more than 1 makes the spin thing faster
    mySprite.x += Math.cos(i) * randint(10, 50)
    mySprite.y += Math.sin(i) * randint(10, 50)
game.on_update(on_on_update)
