from adafruit_hid.keycode import Keycode

class KeyOptions():
    OPTIONS = (
   {'keys': (Keycode.CONTROL, Keycode.SHIFT, Keycode.M), 'description': 'Win Teams ToggleMute Ctrl Shift M'},
   {'keys': (Keycode.COMMAND, Keycode.SHIFT, Keycode.M), 'description': 'Mac Teams ToggleMute Cmd Shift M'},

   {'keys': (Keycode.ALT, Keycode.A), 'description': 'Win Zoom ToggleMute Alt A'},
   {'keys': (Keycode.COMMAND, Keycode.SHIFT, Keycode.A), 'description': 'Mac Zoom ToggleMute Cmd Shift A'},

   {'keys': (Keycode.CONTROL, Keycode.M), 'description': 'Win Skype Webex ToggleMute Ctrl M'},
   {'keys': (Keycode.COMMAND, Keycode.SHIFT, Keycode.M), 'description': 'Mac Skype Webex ToggleMute Cmd Shift M'},

   {'keys': (Keycode.CONTROL, Keycode.D), 'description': 'Win GoogleMeet ToggleMute Ctrl D'},
   {'keys': (Keycode.COMMAND, Keycode.D), 'description': 'Mac GoogleMeet ToggleMute Cmd D'},

   {'keys': (Keycode.M), 'description': 'Win Mac Jitsi ToggleMute M'},

   {'keys': (Keycode.ALT, Keycode.SHIFT, Keycode.M), 'description': 'Win BigBlueButton ToggleMute Alt Shift M'},
   {'keys': (Keycode.CONTROL, Keycode.OPTION, Keycode.M), 'description': 'Mac BigBlueButton ToggleMute Ctrl Option M'},

   {'keys': (Keycode.F5), 'description': 'Win Reload F5'},


   {'keys': (Keycode.GUI, Keycode.L), 'description': 'Win Lock Screen Win L'},
   {'keys': (Keycode.CONTROL, Keycode.COMMAND, Keycode.Q), 'description': 'Mac Lock Screen Ctrl Cmd Q'}
)
