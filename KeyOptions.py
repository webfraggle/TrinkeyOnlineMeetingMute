from adafruit_hid.keycode import Keycode

class KeyOptions():
    OPTIONS = (
   {'keys': (Keycode.CONTROL, Keycode.SHIFT, Keycode.M), 'description': 'Windows Teams MuteUnmute Ctrl Shift M'},
   {'keys': (Keycode.COMMAND, Keycode.SHIFT, Keycode.M), 'description': 'MAC Teams MuteUnmute Command Shift M'},

   {'keys': (Keycode.ALT, Keycode.A), 'description': 'Windows Zoom MuteUnmute Alt A'},
   {'keys': (Keycode.COMMAND, Keycode.SHIFT, Keycode.A), 'description': 'MAC Zoom MuteUnmute Command Shift A'},

   {'keys': (Keycode.CONTROL, Keycode.M), 'description': 'Windows Skype Webex MuteUnmute Ctrl M'},
   {'keys': (Keycode.COMMAND, Keycode.SHIFT, Keycode.M), 'description': 'MAC Skype Webex MuteUnmute Command Shift M'},

   {'keys': (Keycode.CONTROL, Keycode.D), 'description': 'Windows GoogleMeet MuteUnmute Ctrl D'},
   {'keys': (Keycode.COMMAND, Keycode.D), 'description': 'MAC GoogleMeet MuteUnmute Command D'},

   {'keys': (Keycode.M), 'description': 'Windows Mac Jitsi MuteUnmute M'},

   {'keys': (Keycode.ALT, Keycode.SHIFT, Keycode.M), 'description': 'Windows BigBlueButton MuteUnmute Alt Shift M'},
   {'keys': (Keycode.CONTROL, Keycode.OPTION, Keycode.M), 'description': 'MAC BigBlueButton MuteUnmute Control Option M'},


   {'keys': (Keycode.GUI, Keycode.L), 'description': 'Windows Lock Screen Win L'}
)
