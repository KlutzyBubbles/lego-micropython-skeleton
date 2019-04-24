from enum import Enum

class Port(Enum):

    A = 0
    B = 1
    C = 2
    D = 3

    S1 = 4
    S2 = 5
    S3 = 6
    S4 = 7

class Direction(Enum):

    CLOCKWISE = 0
    COUNTCLOCKWISE = 1

class Stop(Enum):
    
    COAST = 0
    BRAKE = 1
    HOLD = 2

class Color(Enum):

    BLACK = 0
    BLUE = 1
    GREEN = 2
    YELLOW = 3
    RED = 4
    WHITE = 5
    BROWN = 6
    ORANGE = 7
    PURPLE = 8

class Button(Enum):

    LEFT_DOWN = 'ld'
    DOWN = 'd'
    RIGHT_DOWN = 'rd'
    LEFT = 'l'
    CENTER = 'c'
    RIGHT = 'r'
    LEFT_UP = 'lu'
    UP = 'u'
    BEACON = 'b'
    RIGHT_UP = 'ru'

class Align(Enum):

    BOTTOM_LEFT = ''
    BOTTOM = ''
    BOTTOM_RIGHT = ''
    LEFT = ''
    CENTER = ''
    RIGHT = ''
    TOP_LEFT = ''
    TOP = ''
    TOP_RIGHT = ''

class ImageFile(Enum):

    # Information

    RIGHT = ''
    FORWARD = ''
    ACCEPT = ''
    QUESTION_MARK = ''
    STOP_1 = ''
    LEFT = ''
    DECLINE = ''
    THUMBS_DOWN = ''
    BACKWARD = ''
    NO_GO = ''
    WARNING = ''
    STOP_2 = ''
    THUMBS_UP = ''

    # LEGO

    EV3 = ''
    EV3_ICON = ''

    # Objects

    TARGET = ''

    # Eyes

    BOTTOM_RIGHT = ''
    BOTTOM_LEFT = ''
    EVIL = ''
    CRAZY_2 = ''
    KNOCKED_OUT = ''
    PINCHED_RIGHT = ''
    WINKING = ''
    DIZZY = ''
    DOWN = ''
    TIRED_MIDDLE = ''
    MIDDLE_RIGHT = ''
    SLEEPING = ''
    MIDDLE_LEFT = ''
    TIRED_RIGHT = ''
    PINCHED_LEFT = ''
    PINCHED_MIDDLE = ''
    CRAZY_1 = ''
    NEUTRAL = ''
    AWAKE = ''
    UP = ''
    TIRED_LEFT = ''
    ANGRY = ''

class SoundFile(Enum):

    # Expressions

    SHOUTING = ''
    CHEERING = ''
    CRYING = ''
    OUCH = ''
    LAUGHING_2 = ''
    SNEEZING = ''
    SMACK = ''
    BOING = ''
    BOO = ''
    UH_OH = ''
    SNORING = ''
    KUNG_FU = ''
    FANFARE = ''
    CRUNCHING = ''
    MAGIC_WAND = ''
    LAUGHING_1 = ''

    # Information

    LEFT = ''
    BACKWARDS = ''
    RIGHT = ''
    OBJECT = ''
    COLOR = ''
    FLASHING = ''
    ERROR = ''
    ERROR_ALARM = ''
    DOWN = ''
    FORWARD = ''
    ACTIVATE = ''
    SEARCHING = ''
    TOUCH = ''
    UP = ''
    ANALYZE = ''
    STOP = ''
    DETECTED = ''
    TURN = ''
    START = ''

    # Communication

    MORNING = ''
    EV3 = ''
    GO = ''
    GOOD_JOB = ''
    OKEY_DOKEY = ''
    GOOD = ''
    NO = ''
    THANK_YOU = ''
    YES = ''
    GAME_OVER = ''
    OKAY = ''
    SORRY = ''
    BRAVO = ''
    GOODBYE = ''
    HI = ''
    HELLO = ''
    MINDSTORMS = ''
    LEGO = ''
    FANTASTIC = ''

    # Movements

    SPEED_IDLE = ''
    SPEED_DOWN = ''
    SPEED_UP = ''

    # Color

    BROWN = ''
    GREEN = ''
    BLACK = ''
    WHITE = ''
    RED = ''
    BLUE = ''
    YELLOW = ''

    # Mechanical

    TICK_TACK = ''
    HORN_1 = ''
    BACKING_ALERT = ''
    MOTOR_IDLE = ''
    AIR_RELEASE = ''
    AIRBRAKE = ''
    RATCHET = ''
    MOTOR_STOP = ''
    HORN_2 = ''
    LASER = ''
    SONAR = ''
    MOTOR_START = ''

    # Animals

    INSECT_BUZZ_2 = ''
    ELEPHANT_CALL = ''
    SNAKE_HISS = ''
    DOG_BARK_2 = ''
    DOG_WHINE = ''
    INSECT_BUZZ_1 = ''
    DOG_SNIFF = ''
    T_REX_ROAR = ''
    INSECT_CHIRP = ''
    DOG_GROWL = ''
    SNAKE_RATTLE = ''
    DOG_BARK_1 = ''
    CAT_PURR = ''

    # Numbers

    ZERO = ''
    ONE = ''
    TWO = ''
    THREE = ''
    FOUR = ''
    FIVE = ''
    SIX = ''
    SEVEN = ''
    EIGHT = ''
    NINE = ''
    TEN = ''

    # System

    READY = ''
    CONFIRM = ''
    GENERAL_ALERT = ''
    CLICK = ''
    OVERPOWER = ''