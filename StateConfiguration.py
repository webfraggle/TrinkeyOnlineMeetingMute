from State import State
from KeyOptions import KeyOptions
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import microcontroller
import time

class StateConfiguration(State):

    def __init__(self, keyboard):
        print("init StateConfiguration")
        self.keyboard = keyboard
        self.keyboard_layout = KeyboardLayoutUS(self.keyboard)  # We're in the US :)
        self.current = microcontroller.nvm[0]
        if self.current >= len(KeyOptions.OPTIONS):
            self.current = 0

    def start(self):
        self.pixel.fill((0, 0, 255))
        print("start configuration "+str(self.current))
        self.make_keystrokes("Start Configuration", 0.1)
        self.make_keystrokes(Keycode.ENTER, 0.1)
        print("Current Configuration: "+KeyOptions.OPTIONS[self.current]["description"])
        self.make_keystrokes("Current Configuration "+KeyOptions.OPTIONS[self.current]["description"], 0.1)
        self.make_keystrokes(Keycode.ENTER, 0.1)


    def onButtonPress(self):
        print("do the button config")
        print(KeyOptions.OPTIONS)


    def make_keystrokes(self, keys, delay):
        if isinstance(keys, str):
            self.keyboard_layout.write(keys)
        elif isinstance(keys, int):
            self.keyboard.press(keys)
            self.keyboard.release_all()
        elif isinstance(keys, (list, tuple)):
            self.keyboard.press(*keys)
            self.keyboard.release_all()
        time.sleep(delay)
