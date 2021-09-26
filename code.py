"""NeoKey Trinkey Capacitive Touch and HID Keyboard example"""
import time
import board
import neopixel
import usb_hid
import microcontroller

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode  # pylint: disable=unused-import

from digitalio import DigitalInOut, Pull
import touchio
from States import States
from StateKeyboard import StateKeyboard
from StateConfiguration import StateConfiguration

# create the pixel and turn it off
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)
pixel.fill(0x0)

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

states = States()
states.stateKeyboard = StateKeyboard(keyboard)
states.stateKeyboard.pixel = pixel

states.stateConfiguration = StateConfiguration(keyboard)
states.stateConfiguration.pixel = pixel

states.stateKeyboard.start()
states.currentState = states.stateKeyboard

# create the switch, add a pullup, start it with not being pressed
button = DigitalInOut(board.SWITCH)
button.switch_to_input(pull=Pull.DOWN)
button_state = False

# create the captouch element and start it with not touched
touch = touchio.TouchIn(board.TOUCH)
touch_state = False

startTime = -1


while True:
    now = time.monotonic()
    # print(now)

    if button.value and not button_state:
        #print("Button pressed.")
        states.currentState.onButtonPress()
        button_state = True

    if not button.value and button_state:
        #print("Button released.")
        states.currentState.onButtonRelease()
        button_state = False

    if touch.value and not touch_state:
        #print("Touched!")
        startTime = now
        # microcontroller.nvm[0] = microcontroller.nvm[0] + 1
        touch_state = True
        timerActive = True
    if not touch.value and touch_state:
        #print("Untouched!")
        startTime = -1
        # pixel.fill(0x0)
        touch_state = False

    # check configuration timer
    if touch_state and timerActive:
        diff = now - startTime
        if (round(diff * 10) % 2) == 0:
            pixel.fill((0, 0, 255))
        else:
            pixel.fill(0x0)
        if diff > 2:
            print("timer end")
            # print(states.currentState)
            # print(states.stateKeyboard)
            timerActive = False
            if states.currentState is states.stateKeyboard:
                print("switch to conf")
                states.currentState = states.stateConfiguration
                states.stateConfiguration.start()
            elif states.currentState is states.stateConfiguration:
                print("switch to keyboard")
                states.stateConfiguration.end()
                states.currentState = states.stateKeyboard
                states.stateKeyboard.start()
