def on_gesture_shake():
    global tangan
    tangan = randint(1, 3)
    if tangan == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif tangan == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

tangan = 0
basic.show_icon(IconNames.HEART)