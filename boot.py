import storage
import board
from digitalio import DigitalInOut, Pull

button = DigitalInOut(board.SWITCH)
button.switch_to_input(pull=Pull.DOWN)

# Disable devices only if button is not pressed.
if not button.value:
	storage.disable_usb_drive()
