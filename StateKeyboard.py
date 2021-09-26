from State import State
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import time
import microcontroller
from KeyOptions import KeyOptions

class StateKeyboard(State):

    def __init__(self, keyboard):
        #print("init StateKeyboard")
        self.keyboard = keyboard
        self.keyboard_layout = KeyboardLayoutUS(self.keyboard)
        self.custom_keys = None
        try:
            f = open("custom.keys", "r")
            self.custom_keys_string = f.read()
            #print (sstr)
            self.custom_keys = eval(self.custom_keys_string)
            #print (custom_keys)
        except OSError:
            #print("no custom keys")
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
        #print("do the button Keyboard")
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

    # our helper function will press the keys themselves
    def make_keystrokes(self, keys, delay):
        if isinstance(keys, str):  # If it's a string...
            self.keyboard_layout.write(keys)  # ...Print the string
        elif isinstance(keys, int):  # If its a single key
            self.keyboard.press(keys)  # "Press"...
            self.keyboard.release_all()  # ..."Release"!
        elif isinstance(keys, (list, tuple)):  # If its multiple keys
            self.keyboard.press(*keys)  # "Press"...
            self.keyboard.release_all()  # ..."Release"!
        time.sleep(delay)

