function isCatNotHere () {
    if (pins.analogReadPin(AnalogPin.P0) < 500) {
        basic.showLeds(`
            # . . . #
            # # . # #
            # # # # #
            # . # . #
            # # # # #
            `)
        catNotHere = false
    } else {
        basic.showLeds(`
            . # . # .
            # # . # #
            # # # # #
            # . # . #
            . # # # .
            `)
        catNotHere = true
    }
    return catNotHere
}
input.onButtonPressed(Button.A, function () {
    numSpin = 6
    time += -1
    if (time == 0) {
        time = 24
        basic.showNumber(time)
    } else {
        basic.showNumber(time)
    }
})
function changeCompartment () {
    basic.pause(timer)
    if (isCatNotHere() && isTrayEmpty()) {
        servos.P1.run(100)
        basic.pause(stop360)
        servos.P1.run(0)
    } else {
        basic.pause(2000)
        changeCompartment()
    }
}
input.onButtonPressed(Button.AB, function () {
    numSpin = 0
    timer = time * 1000
    basic.showNumber(time)
    basic.pause(2000)
    while (numSpin < 6) {
        if (numSpin % 2 == 1) {
            stop360 += 1
        } else {
            stop360 += -1
        }
        changeCompartment()
        numSpin += 1
        basic.showNumber(6 - numSpin)
    }
    while (true) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(200)
        basic.clearScreen()
        basic.pause(200)
    }
})
input.onButtonPressed(Button.B, function () {
    numSpin = 6
    time += 1
    if (time > 24) {
        time = 1
        basic.showNumber(time)
    } else {
        basic.showNumber(time)
    }
})
function isTrayEmpty () {
    Distance = sonar.ping(
    DigitalPin.P2,
    DigitalPin.P8,
    PingUnit.Centimeters
    )
    basic.pause(100)
    if (Distance <= 12) {
        isEmpty = false
    } else {
        isEmpty = true
    }
    return isEmpty
}
let isEmpty = false
let Distance = 0
let timer = 0
let numSpin = 0
let catNotHere = false
let stop360 = 0
let time = 0
basic.showString("HELLO")
basic.showLeds(`
    . # # . .
    # . . # .
    # # # # .
    # . . # .
    # . . # .
    `)
basic.showLeds(`
    # # # . .
    . . . # .
    . # # . .
    # . . . .
    # # # # .
    `)
basic.showLeds(`
    # # # # .
    . . . # .
    . . # . .
    . # . . .
    # . . . .
    `)
basic.clearScreen()
basic.pause(200)
basic.showLeds(`
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    `)
basic.clearScreen()
basic.pause(200)
time = 1
basic.showNumber(time)
stop360 = 282
