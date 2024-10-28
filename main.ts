namespace SpriteKind {
    export const PaintBrush = SpriteKind.create()
}
let i = 0
let mySprite = sprites.create(img`
    1 
    `, SpriteKind.Player)
mySprite.setBounceOnWall(true)
mySprite.startEffect(effects.spray)
mySprite.startEffect(effects.trail)
mySprite.startEffect(effects.fountain)
mySprite.startEffect(effects.confetti)
mySprite.startEffect(effects.hearts)
mySprite.startEffect(effects.smiles)
mySprite.startEffect(effects.rings)
mySprite.startEffect(effects.fire)
mySprite.startEffect(effects.warmRadial)
mySprite.startEffect(effects.coolRadial)
mySprite.startEffect(effects.halo)
mySprite.startEffect(effects.ashes)
mySprite.startEffect(effects.disintegrate)
mySprite.startEffect(effects.blizzard)
mySprite.startEffect(effects.bubbles)
mySprite.startEffect(effects.starField)
mySprite.startEffect(effects.clouds)
game.onUpdate(function () {
    i += 1
    mySprite.x += Math.cos(i) * randint(10, 50)
    mySprite.y += Math.sin(i) * randint(10, 50)
})
