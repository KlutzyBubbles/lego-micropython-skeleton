:mod:`parameters` -- Parameters and Constants
=============================================

Constant parameters/arguments for the Pybricks API.

.. automodule:: parameters
    :no-members:

.. autoclass:: Port
    :no-members:

    Motor Ports:

    .. autoattribute:: parameters.Port.A
        :annotation:
    .. autoattribute:: parameters.Port.B
        :annotation:
    .. autoattribute:: parameters.Port.C
        :annotation:
    .. autoattribute:: parameters.Port.D
        :annotation:

    Sensor Ports:

    .. autoattribute:: parameters.Port.S1
        :annotation:
    .. autoattribute:: parameters.Port.S2
        :annotation:
    .. autoattribute:: parameters.Port.S3
        :annotation:
    .. autoattribute:: parameters.Port.S4
        :annotation:

.. autoclass:: Direction
    :no-members:

    .. autoattribute:: parameters.Direction.CLOCKWISE
        :annotation:
    .. autoattribute:: parameters.Direction.COUNTERCLOCKWISE
        :annotation:

    For all motors, this is defined when looking at the shaft, just like looking at a clock.

    For NXT or EV3 motors, make sure to look at the motor with the red/orange shaft to the lower right.

    ==========================   ================   ================
    Parameter                    Positive Speed     Negative Speed
    ==========================   ================   ================
    Direction.CLOCKWISE          clockwise          counterclockwise
    Direction.COUNTERCLOCKWISE   counterclockwise   clockwise
    ==========================   ================   ================

    .. code-block:: none

        Medium EV3 Motor:


            counterclockwise          clockwise
        |        ____                _____
        |       /                         \
        |      /       _____________       \
        |     /      /              \       \
        |    |      |        _       |       |
        |    |      |     __| |__    |       |
        |    v      |    |__ o __|   |       v
        |           |       |_|      |
        |           |                |
        |            \______________/


        Large EV3 Motor:

            __________
            /         \       ___    ___
            |          \     /          \
            |            ---/------      \
            counterclockwise|    __\__    |  clockwise
            \__________     v  /      \   v
                        -------|  +   |
                                \_____/

.. autoclass:: parameters.Stop
    :no-members:

    .. autoattribute:: parameters.Stop.COAST
        :annotation:
    .. autoattribute:: parameters.Stop.BRAKE
        :annotation:
    .. autoattribute:: parameters.Stop.HOLD
        :annotation:

    The stop type defines the resistance to motion after coming to a standstill:

    ==========================   ================   =========================================
    Parameter                    Resistance         Physical meaning
    ==========================   ================   =========================================
    Stop.COAST                   low                Friction
    Stop.BRAKE                   medium             Friction + Torque opposite to motion
    Stop.HOLD                    high               Friction + Torque to hold commanded angle
    ==========================   ================   =========================================

.. autoclass:: parameters.Color
    :no-members:

    .. autoattribute:: parameters.Color.BLACK
        :annotation:
    .. autoattribute:: parameters.Color.BLUE
        :annotation:
    .. autoattribute:: parameters.Color.GREEN
        :annotation:
    .. autoattribute:: parameters.Color.YELLOW
        :annotation:
    .. autoattribute:: parameters.Color.RED
        :annotation:
    .. autoattribute:: parameters.Color.WHITE
        :annotation:
    .. autoattribute:: parameters.Color.BROWN
        :annotation:
    .. autoattribute:: parameters.Color.ORANGE
        :annotation:
    .. autoattribute:: parameters.Color.PURPLE
        :annotation:

.. autoclass:: parameters.Button
    :no-members:

    .. autoattribute:: parameters.Button.LEFT_DOWN
        :annotation:
    .. autoattribute:: parameters.Button.DOWN
        :annotation:
    .. autoattribute:: parameters.Button.RIGHT_DOWN
        :annotation:
    .. autoattribute:: parameters.Button.LEFT
        :annotation:
    .. autoattribute:: parameters.Button.CENTER
        :annotation:
    .. autoattribute:: parameters.Button.RIGHT
        :annotation:
    .. autoattribute:: parameters.Button.LEFT_UP
        :annotation:
    .. autoattribute:: parameters.Button.UP
        :annotation:
    .. autoattribute:: parameters.Button.BEACON
        :annotation:
    .. autoattribute:: parameters.Button.RIGHT_UP
        :annotation:

    ==========   ==========   ==========
    LEFT_UP      UP/BEACON    RIGHT_UP
    LEFT         CENTER       RIGHT
    LEFT_DOWN    DOWN         RIGHT_DOWN
    ==========   ==========   ==========

.. autoclass:: parameters.Align
    :no-members:

    .. autoattribute:: parameters.Align.BOTTOM_LEFT
        :annotation:
    .. autoattribute:: parameters.Align.BOTTOM
        :annotation:
    .. autoattribute:: parameters.Align.BOTTOM_RIGHT
        :annotation:
    .. autoattribute:: parameters.Align.LEFT
        :annotation:
    .. autoattribute:: parameters.Align.CENTER
        :annotation:
    .. autoattribute:: parameters.Align.RIGHT
        :annotation:
    .. autoattribute:: parameters.Align.TOP_LEFT
        :annotation:
    .. autoattribute:: parameters.Align.TOP
        :annotation:
    .. autoattribute:: parameters.Align.TOP_RIGHT
        :annotation:

    ============   ============   ============
    TOP_LEFT       TOP            TOP_RIGHT
    LEFT           CENTER         RIGHT
    BOTTOM_LEFT    BOTTOM         BOTTOM_RIGHT
    ============   ============   ============

.. autoclass:: parameters.ImageFile
    :no-members:

    Information

    .. autoattribute:: parameters.ImageFile.RIGHT
        :annotation:
    .. autoattribute:: parameters.ImageFile.FORWARD
        :annotation:
    .. autoattribute:: parameters.ImageFile.ACCEPT
        :annotation:
    .. autoattribute:: parameters.ImageFile.QUESTION_MARK
        :annotation:
    .. autoattribute:: parameters.ImageFile.STOP_1
        :annotation:
    .. autoattribute:: parameters.ImageFile.LEFT
        :annotation:
    .. autoattribute:: parameters.ImageFile.DECLINE
        :annotation:
    .. autoattribute:: parameters.ImageFile.THUMBS_DOWN
        :annotation:
    .. autoattribute:: parameters.ImageFile.BACKWARD
        :annotation:
    .. autoattribute:: parameters.ImageFile.NO_GO
        :annotation:
    .. autoattribute:: parameters.ImageFile.WARNING
        :annotation:
    .. autoattribute:: parameters.ImageFile.STOP_2
        :annotation:
    .. autoattribute:: parameters.ImageFile.THUMBS_UP
        :annotation:

    LEGO

    .. autoattribute:: parameters.ImageFile.EV3
        :annotation:
    .. autoattribute:: parameters.ImageFile.EV3_ICON
        :annotation:

    Objects

    .. autoattribute:: parameters.ImageFile.TARGET
        :annotation:

    Eyes

    .. autoattribute:: parameters.ImageFile.BOTTOM_RIGHT
        :annotation:
    .. autoattribute:: parameters.ImageFile.BOTTOM_LEFT
        :annotation:
    .. autoattribute:: parameters.ImageFile.EVIL
        :annotation:
    .. autoattribute:: parameters.ImageFile.CRAZY_2
        :annotation:
    .. autoattribute:: parameters.ImageFile.KNOCKED_OUT
        :annotation:
    .. autoattribute:: parameters.ImageFile.PINCHED_RIGHT
        :annotation:
    .. autoattribute:: parameters.ImageFile.WINKING
        :annotation:
    .. autoattribute:: parameters.ImageFile.DIZZY
        :annotation:
    .. autoattribute:: parameters.ImageFile.DOWN
        :annotation:
    .. autoattribute:: parameters.ImageFile.TIRED_MIDDLE
        :annotation:
    .. autoattribute:: parameters.ImageFile.MIDDLE_RIGHT
        :annotation:
    .. autoattribute:: parameters.ImageFile.SLEEPING
        :annotation:
    .. autoattribute:: parameters.ImageFile.MIDDLE_LEFT
        :annotation:
    .. autoattribute:: parameters.ImageFile.TIRED_RIGHT
        :annotation:
    .. autoattribute:: parameters.ImageFile.PINCHED_LEFT
        :annotation:
    .. autoattribute:: parameters.ImageFile.PINCHED_MIDDLE
        :annotation:
    .. autoattribute:: parameters.ImageFile.CRAZY_1
        :annotation:
    .. autoattribute:: parameters.ImageFile.NEUTRAL
        :annotation:
    .. autoattribute:: parameters.ImageFile.AWAKE
        :annotation:
    .. autoattribute:: parameters.ImageFile.UP
        :annotation:
    .. autoattribute:: parameters.ImageFile.TIRED_LEFT
        :annotation:
    .. autoattribute:: parameters.ImageFile.ANGRY
        :annotation:

.. autoclass:: parameters.SoundFile
    :no-members:

    Expressions

    .. autoattribute:: parameters.SoundFile.SHOUTING
        :annotation:
    .. autoattribute:: parameters.SoundFile.CHEERING
        :annotation:
    .. autoattribute:: parameters.SoundFile.CRYING
        :annotation:
    .. autoattribute:: parameters.SoundFile.OUCH
        :annotation:
    .. autoattribute:: parameters.SoundFile.LAUGHING_2
        :annotation:
    .. autoattribute:: parameters.SoundFile.SNEEZING
        :annotation:
    .. autoattribute:: parameters.SoundFile.SMACK
        :annotation:
    .. autoattribute:: parameters.SoundFile.BOING
        :annotation:
    .. autoattribute:: parameters.SoundFile.BOO
        :annotation:
    .. autoattribute:: parameters.SoundFile.UH_OH
        :annotation:
    .. autoattribute:: parameters.SoundFile.SNORING
        :annotation:
    .. autoattribute:: parameters.SoundFile.KUNG_FU
        :annotation:
    .. autoattribute:: parameters.SoundFile.FANFARE
        :annotation:
    .. autoattribute:: parameters.SoundFile.CRUNCHING
        :annotation:
    .. autoattribute:: parameters.SoundFile.MAGIC_WAND
        :annotation:
    .. autoattribute:: parameters.SoundFile.LAUGHING_1
        :annotation:

    Information

    .. autoattribute:: parameters.SoundFile.LEFT
        :annotation:
    .. autoattribute:: parameters.SoundFile.BACKWARDS
        :annotation:
    .. autoattribute:: parameters.SoundFile.RIGHT
        :annotation:
    .. autoattribute:: parameters.SoundFile.OBJECT
        :annotation:
    .. autoattribute:: parameters.SoundFile.COLOR
        :annotation:
    .. autoattribute:: parameters.SoundFile.FLASHING
        :annotation:
    .. autoattribute:: parameters.SoundFile.ERROR
        :annotation:
    .. autoattribute:: parameters.SoundFile.ERROR_ALARM
        :annotation:
    .. autoattribute:: parameters.SoundFile.DOWN
        :annotation:
    .. autoattribute:: parameters.SoundFile.FORWARD
        :annotation:
    .. autoattribute:: parameters.SoundFile.ACTIVATE
        :annotation:
    .. autoattribute:: parameters.SoundFile.SEARCHING
        :annotation:
    .. autoattribute:: parameters.SoundFile.TOUCH
        :annotation:
    .. autoattribute:: parameters.SoundFile.UP
        :annotation:
    .. autoattribute:: parameters.SoundFile.ANALYZE
        :annotation:
    .. autoattribute:: parameters.SoundFile.STOP
        :annotation:
    .. autoattribute:: parameters.SoundFile.DETECTED
        :annotation:
    .. autoattribute:: parameters.SoundFile.TURN
        :annotation:
    .. autoattribute:: parameters.SoundFile.START
        :annotation:

    Communication

    .. autoattribute:: parameters.SoundFile.MORNING
        :annotation:
    .. autoattribute:: parameters.SoundFile.EV3
        :annotation:
    .. autoattribute:: parameters.SoundFile.GO
        :annotation:
    .. autoattribute:: parameters.SoundFile.GOOD_JOB
        :annotation:
    .. autoattribute:: parameters.SoundFile.OKEY_DOKEY
        :annotation:
    .. autoattribute:: parameters.SoundFile.GOOD
        :annotation:
    .. autoattribute:: parameters.SoundFile.NO
        :annotation:
    .. autoattribute:: parameters.SoundFile.THANK_YOU
        :annotation:
    .. autoattribute:: parameters.SoundFile.YES
        :annotation:
    .. autoattribute:: parameters.SoundFile.GAME_OVER
        :annotation:
    .. autoattribute:: parameters.SoundFile.OKAY
        :annotation:
    .. autoattribute:: parameters.SoundFile.SORRY
        :annotation:
    .. autoattribute:: parameters.SoundFile.BRAVO
        :annotation:
    .. autoattribute:: parameters.SoundFile.GOODBYE
        :annotation:
    .. autoattribute:: parameters.SoundFile.HI
        :annotation:
    .. autoattribute:: parameters.SoundFile.HELLO
        :annotation:
    .. autoattribute:: parameters.SoundFile.MINDSTORMS
        :annotation:
    .. autoattribute:: parameters.SoundFile.LEGO
        :annotation:
    .. autoattribute:: parameters.SoundFile.FANTASTIC
        :annotation:

    Movements

    .. autoattribute:: parameters.SoundFile.SPEED_IDLE
        :annotation:
    .. autoattribute:: parameters.SoundFile.SPEED_DOWN
        :annotation:
    .. autoattribute:: parameters.SoundFile.SPEED_UP
        :annotation:

    Color

    .. autoattribute:: parameters.SoundFile.BROWN
        :annotation:
    .. autoattribute:: parameters.SoundFile.GREEN
        :annotation:
    .. autoattribute:: parameters.SoundFile.BLACK
        :annotation:
    .. autoattribute:: parameters.SoundFile.WHITE
        :annotation:
    .. autoattribute:: parameters.SoundFile.RED
        :annotation:
    .. autoattribute:: parameters.SoundFile.BLUE
        :annotation:
    .. autoattribute:: parameters.SoundFile.YELLOW
        :annotation:

    Mechanical

    .. autoattribute:: parameters.SoundFile.TICK_TACK
        :annotation:
    .. autoattribute:: parameters.SoundFile.HORN_1
        :annotation:
    .. autoattribute:: parameters.SoundFile.BACKING_ALERT
        :annotation:
    .. autoattribute:: parameters.SoundFile.MOTOR_IDLE
        :annotation:
    .. autoattribute:: parameters.SoundFile.AIR_RELEASE
        :annotation:
    .. autoattribute:: parameters.SoundFile.AIRBRAKE
        :annotation:
    .. autoattribute:: parameters.SoundFile.RATCHET
        :annotation:
    .. autoattribute:: parameters.SoundFile.MOTOR_STOP
        :annotation:
    .. autoattribute:: parameters.SoundFile.HORN_2
        :annotation:
    .. autoattribute:: parameters.SoundFile.LASER
        :annotation:
    .. autoattribute:: parameters.SoundFile.SONAR
        :annotation:
    .. autoattribute:: parameters.SoundFile.MOTOR_START
        :annotation:

    Animals

    .. autoattribute:: parameters.SoundFile.INSECT_BUZZ_2
        :annotation:
    .. autoattribute:: parameters.SoundFile.ELEPHANT_CALL
        :annotation:
    .. autoattribute:: parameters.SoundFile.SNAKE_HISS
        :annotation:
    .. autoattribute:: parameters.SoundFile.DOG_BARK_2
        :annotation:
    .. autoattribute:: parameters.SoundFile.DOG_WHINE
        :annotation:
    .. autoattribute:: parameters.SoundFile.INSECT_BUZZ_1
        :annotation:
    .. autoattribute:: parameters.SoundFile.DOG_SNIFF
        :annotation:
    .. autoattribute:: parameters.SoundFile.T_REX_ROAR
        :annotation:
    .. autoattribute:: parameters.SoundFile.INSECT_CHIRP
        :annotation:
    .. autoattribute:: parameters.SoundFile.DOG_GROWL
        :annotation:
    .. autoattribute:: parameters.SoundFile.SNAKE_RATTLE
        :annotation:
    .. autoattribute:: parameters.SoundFile.DOG_BARK_1
        :annotation:
    .. autoattribute:: parameters.SoundFile.CAT_PURR
        :annotation:

    Numbers

    .. autoattribute:: parameters.SoundFile.ZERO
        :annotation:
    .. autoattribute:: parameters.SoundFile.ONE
        :annotation:
    .. autoattribute:: parameters.SoundFile.TWO
        :annotation:
    .. autoattribute:: parameters.SoundFile.THREE
        :annotation:
    .. autoattribute:: parameters.SoundFile.FOUR
        :annotation:
    .. autoattribute:: parameters.SoundFile.FIVE
        :annotation:
    .. autoattribute:: parameters.SoundFile.SIX
        :annotation:
    .. autoattribute:: parameters.SoundFile.SEVEN
        :annotation:
    .. autoattribute:: parameters.SoundFile.EIGHT
        :annotation:
    .. autoattribute:: parameters.SoundFile.NINE
        :annotation:
    .. autoattribute:: parameters.SoundFile.TEN
        :annotation:

    System

    .. autoattribute:: parameters.SoundFile.READY
        :annotation:
    .. autoattribute:: parameters.SoundFile.CONFIRM
        :annotation:
    .. autoattribute:: parameters.SoundFile.GENERAL_ALERT
        :annotation:
    .. autoattribute:: parameters.SoundFile.CLICK
        :annotation:
    .. autoattribute:: parameters.SoundFile.OVERPOWER
        :annotation:
