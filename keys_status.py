class KeysStatus:
    """
    A KeysStatus is a 1byte value which describes the buttons which are being currently pressed by the user
    """

    UP          = 0b00000001
    DOWN        = 0b00000010
    LEFT        = 0b00000100
    RIGHT       = 0b00001000
    BRAKE       = 0b00010000
    QUIT        = 0b00100000
    SPEED_UP    = 0b01000000
    SPEED_DOWN  = 0b10000000