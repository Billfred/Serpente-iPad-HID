import board
import digitalio

switch3 = digitalio.DigitalInOut(board.D3)
switch3.pull = digitalio.Pull.UP
switch5 = digitalio.DigitalInOut(board.D5)
switch5.pull = digitalio.Pull.UP

if switch3 and switch5:
    print("Holla if you hear me! \n")
    import storage

    storage.disable_usb_drive()
    import usb_midi

    usb_midi.disable()
    import usb_cdc
    usb_cdc.disable()
