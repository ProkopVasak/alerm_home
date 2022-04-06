let counter = true
radio.setTransmitPower(7)
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    if (receivedNumber == 1) {
        radio.setGroup(128)
    }
    
    if (receivedNumber == 2) {
        counter = false
    }
    
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    while (counter == true) {
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.playTone(262, music.beat(BeatFraction.Whole))
    }
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    radio.sendNumber(2)
    counter = true
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    radio.setGroup(128)
    radio.setTransmitSerialNumber(true)
    radio.sendNumber(1)
})
basic.forever(function on_forever() {
    
})
