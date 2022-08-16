def isCatNotHere():
    global catNotHere
    if pins.analog_read_pin(AnalogPin.P0) > 500:
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
    global time
    time += -1
    if time == 0:
        time = 24
        basic.show_number(time)
    else:
        basic.show_number(time)
input.on_button_pressed(Button.A, on_button_pressed_a)

def changeCompartment():
    if isCatNotHere() and isTrayEmpty():
        servos.P0.run(100)
        basic.pause(stop360)
        servos.P0.run(0)
    else:
        basic.pause(5000)
        changeCompartment()

def on_button_pressed_ab():
    global timer, numSpin, stop360
    timer = time * 1000
    basic.show_number(time)
    numSpin = 0
    stop360 = 1161
    while numSpin != 6:
        basic.pause(timer)
        changeCompartment()
        if input.button_is_pressed(Button.AB):
            break
        if numSpin % 2 == 1:
            stop360 += 1
        else:
            stop360 += -1
        numSpin += 1
        basic.show_number(numSpin)
    basic.show_number(time)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global time
    time += 1
    if time > 24:
        time = 1
        basic.show_number(time)
    else:
        basic.show_number(time)
input.on_button_pressed(Button.B, on_button_pressed_b)

def isTrayEmpty():
    global isEmpty
    isEmpty = True
    return isEmpty
isEmpty = False
numSpin = 0
timer = 0
stop360 = 0
catNotHere = False
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
time = 1
basic.show_number(time)