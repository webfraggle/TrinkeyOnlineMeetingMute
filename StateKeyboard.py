from State import State
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import time
import microcontroller
from KeyOptions import KeyOptions

class StateKeyboard(State):

    def __init__(self, keyboard):
        self.keyboard = keyboard
        self.keyboard_layout = KeyboardLayoutUS(self.keyboard)
        self.custom_keys = None
        try:
            f = open("custom.keys", "r")
            self.custom_keys_string = f.read()
            self.custom_keys = eval(self.custom_keys_string)
        except OSError:
            self.custom_keys = None
            pass
        self.key_output = ""

    def start(self):
        self.pixel.fill(0x0)
        nr = microcontroller.nvm[0]
        if nr >= len(KeyOptions.OPTIONS):
            nr = 0
        self.key_output = KeyOptions.OPTIONS[nr]["keys"]


    def onButtonPress(self):
        self.pixel.fill((255, 0, 0))
        if self.custom_keys is not None:
            key_output = self.custom_keys
        else:
            key_output = self.key_output
        if isinstance(key_output, (list, tuple)) and isinstance(key_output[0], dict):
            for k in key_output:
                self.make_keystrokes(k['keys'], k['delay'])
        else:
            self.make_keystrokes(key_output, delay=0)
        pass
    def onButtonRelease(self):
        self.pixel.fill(0x0)

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

