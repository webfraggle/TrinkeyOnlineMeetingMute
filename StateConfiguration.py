from State import State
from KeyOptions import KeyOptions
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import microcontroller
import time

class StateConfiguration(State):

    def __init__(self, keyboard):
        self.keyboard = keyboard
        self.keyboard_layout = KeyboardLayoutUS(self.keyboard)

    def start(self):
        self.pixel.fill((0, 0, 255))
        self.current = microcontroller.nvm[0]
        if self.current >= len(KeyOptions.OPTIONS):
            self.current = 0
        self.make_keystrokes("Start Configuration")
        self.make_keystrokes(Keycode.ENTER)
        self.make_keystrokes(Keycode.ENTER)
        self.make_keystrokes("Current Configuration ")
        self.make_keystrokes(Keycode.ENTER)
        self.make_keystrokes(KeyOptions.OPTIONS[self.current]["description"])
        self.make_keystrokes(Keycode.ENTER)
        self.make_keystrokes(Keycode.ENTER)

    def end(self):
        microcontroller.nvm[0] = self.current
        pass

    def onButtonPress(self):
        self.current += 1
        if self.current >= len(KeyOptions.OPTIONS):
            self.current = 0
        self.make_keystrokes(""+KeyOptions.OPTIONS[self.current]["description"])
        self.make_keystrokes(Keycode.ENTER)


    def doKeyStrokes(self, key_output):
        if isinstance(self.key_output, (list, tuple)) and isinstance(self.key_output[0], dict):
            for k in self.key_output:
                self.make_keystrokes(k['keys'], k['delay'])
        else:
            self.make_keystrokes(self.key_output, delay=0)
        pass
    def make_keystrokes(self, keys):
        if isinstance(keys, str):
            self.keyboard_layout.write(keys)
        elif isinstance(keys, int):
            self.keyboard.press(keys)
            self.keyboard.release_all()
        elif isinstance(keys, (list, tuple)):
            self.keyboard.press(*keys)
            self.keyboard.release_all()
        time.sleep(0.1)
