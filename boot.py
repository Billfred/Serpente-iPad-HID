import board
import digitalio
import storage
import usb_cdc
import usb_hid

pin5 = digitalio.DigitalInOut(board.A5)
pin4 = digitalio.DigitalInOut(board.A4)
pin4.switch_to_input(pull=digitalio.Pull.UP)
pin5.switch_to_input(pull=digitalio.Pull.UP)
notpin4 = not pin4
notpin5 = not pin5

if notpin4 and notpin5:
    storage.disable_usb_drive()  # disable CIRCUITPY USB drive
    usb_cdc.disable()            # disable REPL
    usb_midi.disable()           # disable MIDI

usb_hid.enable((usb_hid.KEYBOARD))

pin4.deinit()
pin5.deinit()
