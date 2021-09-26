from State import State
import time

# one character on keypress
# key_output = Keycode.A

# multiple simultaneous keypresses
# key_output = (Keycode.SHIFT, Keycode.A)  # capital A
# key_output = (Keycode.CONTROL, Keycode.ALT, Keycode.DELETE) # three finger salute!

# complex commands! we make a list of dictionary entries for each command
# each line has 'keys' which is either a single key, a list of keys, or a string
# then the 'delay' is in seconds, since we often need to give the computer a minute
# before doing something!

# this will open up a notepad in windows, and ducky the user
"""
key_output = (
   {'keys': Keycode.GUI, 'delay': 0.1},
   {'keys': "notepad\n", 'delay': 1},  # give it a moment to launch!
   {'keys': "YOU HAVE BEEN DUCKIED!", 'delay': 0.1},
   {'keys': (Keycode.ALT, Keycode.O), 'delay': 0.1}, # open format menu
   {'keys': Keycode.F, 'delay': 0.1}, # open font submenu
   {'keys': "\t\t100\n", 'delay': 0.1}, # tab over to font size, enter 100
)
"""


class StateKeyboard(State):

    def __init__(self, keyboard):
        print("init StateKeyboard")
        self.keyboard = keyboard
        self.key_output = "Hello World!\n"

    def onButtonPress(self):
        print("do the button Keyboard")
        if isinstance(self.key_output, (list, tuple)) and isinstance(self.key_output[0], dict):
            for k in self.key_output:
                self.make_keystrokes(k['keys'], k['delay'])
        else:
            self.make_keystrokes(self.key_output, delay=0)
        pass

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

