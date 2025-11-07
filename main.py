def on_a_pressed():
    info.change_score_by(1)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

mySprite = sprites.create(img("""
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
        """),
    SpriteKind.player)
statusbar = statusbars.create(100, 5000, StatusBarKind.health)
info.set_score(0)