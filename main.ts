controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    info.changeScoreBy(1)
})
let mySprite = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . 2 2 2 2 2 2 2 2 . . . 
    . . . . . 2 2 . . . . 2 2 . . . 
    . . . . . 2 . . . . . . 2 . . . 
    . . . . . 2 . 2 2 2 . . 2 . . . 
    . . . . . 2 2 2 2 2 2 2 2 . . . 
    . . . . . 2 . . . . . . 2 . . . 
    . . . . . 2 . . . . . . 2 . . . 
    . . . . 2 2 . . . . . . 2 2 . . 
    . . . . 2 2 . . . . . . 2 2 . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
info.setScore(0)
