# Trinkey Neokey Teams / Zoom / Skype / Webex configurable external extra audio mute unmute button (CircuitPython)

Windows and MacOS

The following key combinations can be configured by default (for custom shortcuts look at the end)˘:

Windows Teams (Ctrl+Shift+M)
Mac Teams (Cmd+Shift+M)

Windows Zoom (Alt+A)
Mac Zoom (Cmd+Shift+A)

Windows Skype/Webex (Ctrl+M)
Mac Skype Webex (Cmd+Shift+M)

Windows GoogleMeet (Ctrl+D)
Mac GoogleMeet (Cmd+D)

Windows/Mac Jitsi (M)

Windows BigBlueButton (Alt+Shift+M)
Mac BigBlueButton (Ctrl+Option+M)

Windows Lock Screen (Win+L)
Mac Lock Screen (Ctrl+Cmd+Q)



## Change Configuration 
* open a texteditor like notepad
* long touch the touch field
* press the key until your desired config is printed
* long touch the touch field to save


## Use a custom shortcut

It is possible to use a  custom shortcut, which is not one of the default shortcuts

For changing the shortcut into a custom shortcut you need to follow these steps:

* Press and hold down the button and press the reset button (small button on the back) 
  OR 
  remove the button from USB, press and hold down the button and put it back into USB.
  
* A disk with the name CIRCUITPY will appear in you file explorer
* Open the disk
* Rename the file "custom-off.keys" to "custom.keys"
* Open the file "custom.keys" in a text-editor (e.g. Notepad on windows) and change the text to your wanted Keycodes e.g. "(Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, Keycode.M)"
  A list of keyboard keycodes can be found here: https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/adafruit_hid/keycode.py
* Press the reset button again 
  OR 
  remove and put it in again

## Autohotkey script to bring Teams in front and mute/unmute

I added a autohotkey script (Autohotkey is only available for Windows) to bring Microsoft Teams in front and mute/unmutes. Shortcut is CTRL+ALT+SHIFT+M.

This can be used with the custom shortcut mode described above


Buy one here:
https://www.etsy.com/de/listing/1092538069/
