import time
import board
import neopixel
import usb_hid
import microcontroller

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

from digitalio import DigitalInOut, Pull
import touchio
from States import States
from StateKeyboard import StateKeyboard
from StateConfiguration import StateConfiguration

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)
pixel.fill(0x0)

time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

states = States()
states.stateKeyboard = StateKeyboard(keyboard)
states.stateKeyboard.pixel = pixel
states.stateConfiguration = StateConfiguration(keyboard)
states.stateConfiguration.pixel = pixel
states.stateKeyboard.start()
states.currentState = states.stateKeyboard
button = DigitalInOut(board.SWITCH)
button.switch_to_input(pull=Pull.DOWN)
button_state = False
touch = touchio.TouchIn(board.TOUCH)
touch_state = False
startTime = -1


while True:
    now = time.monotonic()
    if button.value and not button_state:
        states.currentState.onButtonPress()
        button_state = True
    if not button.value and button_state:
        states.currentState.onButtonRelease()
        button_state = False
    if touch.value and not touch_state:
        startTime = now
        touch_state = True
        timerActive = True
    if not touch.value and touch_state:
        startTime = -1
        pixel.fill(0x0)
        touch_state = False

    if touch_state and timerActive:
        diff = now - startTime
        if (round(diff * 10) % 2) == 0:
            pixel.fill((0, 0, 255))
        else:
            pixel.fill(0x0)
        if diff > 2:
            timerActive = False
            if states.currentState is states.stateKeyboard:
                states.currentState = states.stateConfiguration
                states.stateConfiguration.start()
            elif states.currentState is states.stateConfiguration:
                states.stateConfiguration.end()
                states.currentState = states.stateKeyboard
                states.stateKeyboard.start()
