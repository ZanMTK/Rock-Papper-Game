input.onGesture(Gesture.Shake, function () {
    tangan = randint(1, 3)
    if (tangan == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (tangan == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
})
let tangan = 0
basic.showIcon(IconNames.Heart)
