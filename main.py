counter = True
radio.set_transmit_power(7)

def on_received_number(receivedNumber):
    global counter
    if receivedNumber == 1:
        radio.set_group(128)
    if receivedNumber == 2:
        counter = False
radio.on_received_number(on_received_number)

def on_pin_pressed_p2():
    while counter == True:
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_b():
    global counter
    radio.send_number(2)
    counter = True
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    radio.set_group(128)
    radio.set_transmit_serial_number(True)
    radio.send_number(1)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)



def on_forever():
    pass
basic.forever(on_forever)
