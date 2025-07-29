import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP29, board.GP0)
keyboard.row_pins = (board.GP28, board.GP27, board.GP26)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [[KC.LGUI(KC.C), KC.LGUI(KC.V), KC.LGUI(KC.X), KC.LGUI(KC.Z), KC.LGUI(KC.LSFT(KC.Z)), KC.LGUI(KC.Q)]]

if __name__ == '__main__':
    keyboard.go()
