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

    BOTTOM_LEFT = 'bl'
    BOTTOM = 'b'
    BOTTOM_RIGHT = 'br'
    LEFT = 'l'
    CENTER = 'c'
    RIGHT = 'r'
    TOP_LEFT = 'tl'
    TOP = 't'
    TOP_RIGHT = 'tr'

class ImageFile(Enum):

    # Information

    RIGHT = 'right'
    FORWARD = 'forward'
    ACCEPT = 'accept'
    QUESTION_MARK = 'question_mark'
    STOP_1 = 'stop_1'
    LEFT = 'left'
    DECLINE = 'decline'
    THUMBS_DOWN = 'thumbs_down'
    BACKWARD = 'backwawrd'
    NO_GO = 'no_go'
    WARNING = 'warning'
    STOP_2 = 'stop_2'
    THUMBS_UP = 'thumbs_up'

    # LEGO

    EV3 = 'ev3'
    EV3_ICON = 'ev3_icon'

    # Objects

    TARGET = 'target'

    # Eyes

    BOTTOM_RIGHT = 'bottom_right'
    BOTTOM_LEFT = 'bottom_left'
    EVIL = 'evil'
    CRAZY_2 = 'crazy_2'
    KNOCKED_OUT = 'knocked_out'
    PINCHED_RIGHT = 'pinched_right'
    WINKING = 'winking'
    DIZZY = 'dizzy'
    DOWN = 'down'
    TIRED_MIDDLE = 'tired_middle'
    MIDDLE_RIGHT = 'middle_right'
    SLEEPING = 'sleeping'
    MIDDLE_LEFT = 'middle_left'
    TIRED_RIGHT = 'tired_right'
    PINCHED_LEFT = 'pinched_left'
    PINCHED_MIDDLE = 'pinched_middle'
    CRAZY_1 = 'crazy_1'
    NEUTRAL = 'neutral'
    AWAKE = 'awake'
    UP = 'up'
    TIRED_LEFT = 'tired_left'
    ANGRY = 'angry'

class SoundFile(Enum):

    # Expressions

    SHOUTING = 'shouting'
    CHEERING = 'cheering'
    CRYING = 'crying'
    OUCH = 'ouch'
    LAUGHING_2 = 'laughing_2'
    SNEEZING = 'sneezing'
    SMACK = 'smack'
    BOING = 'boing'
    BOO = 'boo'
    UH_OH = 'uh_oh'
    SNORING = 'snoring'
    KUNG_FU = 'kung_fu'
    FANFARE = 'fanfare'
    CRUNCHING = 'crunching'
    MAGIC_WAND = 'magic_wand'
    LAUGHING_1 = 'laughing_1'

    # Information

    LEFT = 'left'
    BACKWARDS = 'backwards'
    RIGHT = 'right'
    OBJECT = 'object'
    COLOR = 'color'
    FLASHING = 'flashing'
    ERROR = 'error'
    ERROR_ALARM = 'error_alarm'
    DOWN = 'down'
    FORWARD = 'forward'
    ACTIVATE = 'activate'
    SEARCHING = 'searching'
    TOUCH = 'touch'
    UP = 'up'
    ANALYZE = 'analyze'
    STOP = 'stop'
    DETECTED = 'detected'
    TURN = 'turn'
    START = 'start'

    # Communication

    MORNING = 'morning'
    EV3 = 'ev3'
    GO = 'go'
    GOOD_JOB = 'good_job'
    OKEY_DOKEY = 'okey_dokey'
    GOOD = 'good'
    NO = 'no'
    THANK_YOU = 'thank_you'
    YES = 'yes'
    GAME_OVER = 'game_over'
    OKAY = 'okay'
    SORRY = 'sorry'
    BRAVO = 'bravo'
    GOODBYE = 'goodbye'
    HI = 'hi'
    HELLO = 'hello'
    MINDSTORMS = 'mindstorms'
    LEGO = 'lego'
    FANTASTIC = 'fantastic'

    # Movements

    SPEED_IDLE = 'speed_idle'
    SPEED_DOWN = 'speed_down'
    SPEED_UP = 'speed_up'

    # Color

    BROWN = 'brown'
    GREEN = 'green'
    BLACK = 'black'
    WHITE = 'white'
    RED = 'red'
    BLUE = 'blue'
    YELLOW = 'yellow'

    # Mechanical

    TICK_TACK = 'tick_tack'
    HORN_1 = 'horn_1'
    BACKING_ALERT = 'backing_alert'
    MOTOR_IDLE = 'motor_idle'
    AIR_RELEASE = 'air_release'
    AIRBRAKE = 'airbrake'
    RATCHET = 'ratchet'
    MOTOR_STOP = 'motor_stop'
    HORN_2 = 'horn_2'
    LASER = 'laser'
    SONAR = 'sonar'
    MOTOR_START = 'motor_start'

    # Animals

    INSECT_BUZZ_2 = 'insect_buzz_2'
    ELEPHANT_CALL = 'elephant_call'
    SNAKE_HISS = 'snake_hiss'
    DOG_BARK_2 = 'dog_bark_2'
    DOG_WHINE = 'dog_whine'
    INSECT_BUZZ_1 = 'insect_buzz_1'
    DOG_SNIFF = 'dog_sniff'
    T_REX_ROAR = 't_rex_roar'
    INSECT_CHIRP = 'insect_chirp'
    DOG_GROWL = 'dog_growl'
    SNAKE_RATTLE = 'snake_rattle'
    DOG_BARK_1 = 'dog_bark_1'
    CAT_PURR = 'cat_purr'

    # Numbers

    ZERO = 'zero'
    ONE = 'one'
    TWO = 'two'
    THREE = 'three'
    FOUR = 'four'
    FIVE = 'five'
    SIX = 'six'
    SEVEN = 'seven'
    EIGHT = 'eight'
    NINE = 'nine'
    TEN = 'ten'

    # System

    READY = 'ready'
    CONFIRM = 'confirm'
    GENERAL_ALERT = 'general_alert'
    CLICK = 'click'
    OVERPOWER = 'overpower'
