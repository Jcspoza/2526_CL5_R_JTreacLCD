# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2025 - 11 - 16
# Goal : DEMO External switch in GPIO14 + Rection Time example
# Learning Target : interruptions basic
# Ref : Get started with MicroPython on Raspberry Pi Pico, pag 68 Reaction 1 player
# 1.0 as is in book small changes

import machine
import utime
import urandom

pressed = False
led = machine.Pin(16, machine.Pin.OUT) # cambiado a pin 16
button = machine.Pin(15, machine.Pin.IN) # cambiado a pin 15

def button_handler(pin):
    global pressed
    if not pressed:
        pressed=True
        timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
        print("Your reaction time was " + str(timer_reaction) + " milliseconds!")
        
led.value(1)
utime.sleep(urandom.uniform(5, 10))
led.value(0)
timer_start = utime.ticks_ms()
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)