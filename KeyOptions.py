from adafruit_hid.keycode import Keycode

class KeyOptions():
    OPTIONS = (
   {'keys': (Keycode.CONTROL, Keycode.SHIFT, Keycode.M), 'description': 'Windows Teams MuteUnmute Ctrl Shift M'},
   {'keys': (Keycode.COMMAND, Keycode.SHIFT, Keycode.M), 'description': 'MAC Teams MuteUnmute (Command + Shift + M)'},
   {'keys': (Keycode.GUI, Keycode.L), 'description': 'Windows Lock Screen (Win + L)'}
)
