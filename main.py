def isCatNotHere():
    global catNotHere
    if pins.analog_read_pin(AnalogPin.P0) < 500:
        basic.show_leds("""
            # . . . #
                        # # . # #
                        # # # # #
                        # . # . #
                        # # # # #
        """)
        catNotHere = False
    else:
        basic.show_leds("""
            . # . # .
                        # # . # #
                        # # # # #
                        # . # . #
                        . # # # .
        """)
        catNotHere = True
    return catNotHere

def on_button_pressed_a():
    global numSpin, time
    numSpin = 6
    time += -1
    if time == 0:
        time = 24
        basic.show_number(time)
    else:
        basic.show_number(time)
input.on_button_pressed(Button.A, on_button_pressed_a)

def changeCompartment():
    basic.pause(timer)
    if isCatNotHere() and isTrayEmpty():
        servos.P1.run(100)
        basic.pause(stop360)
        servos.P1.run(0)
    else:
        basic.pause(5000)
        changeCompartment()

def on_button_pressed_ab():
    global numSpin, timer, stop360
    numSpin = 0
    timer = time * 1000
    basic.show_number(time)
    while numSpin < 6:
        changeCompartment()
        if numSpin % 2 == 1:
            stop360 += 1
        else:
            stop360 += -1
        numSpin += 1
        basic.show_number(numSpin)
    while True:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
        basic.pause(200)
        basic.clear_screen()
        basic.pause(200)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global numSpin, time
    numSpin = 6
    time += 1
    if time > 24:
        time = 1
        basic.show_number(time)
    else:
        basic.show_number(time)
input.on_button_pressed(Button.B, on_button_pressed_b)

def isTrayEmpty():
    global Distance, isEmpty
    Distance = sonar.ping(DigitalPin.P2, DigitalPin.P1, PingUnit.CENTIMETERS)
    basic.show_number(Distance)
    basic.pause(100)
    if Distance <= 19:
        isEmpty = False
    else:
        isEmpty = True
    return isEmpty
isEmpty = False
Distance = 0
timer = 0
numSpin = 0
catNotHere = False
stop360 = 0
time = 0
basic.show_string("HELLO")
basic.show_leds("""
    . # # . .
        # . . # .
        # # # # .
        # . . # .
        # . . # .
""")
basic.show_leds("""
    # # # . .
        . . . # .
        . # # . .
        # . . . .
        # # # # .
""")
basic.show_leds("""
    # # # # .
        . . . # .
        . . # . .
        . # . . .
        # . . . .
""")
basic.clear_screen()
basic.pause(200)
basic.show_leds("""
    # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
""")
basic.clear_screen()
basic.pause(200)
time = 1
basic.show_number(time)
stop360 = 279