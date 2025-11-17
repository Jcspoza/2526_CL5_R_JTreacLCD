# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2023 - 4 - 13
# Goal : Aprender uso de pulsador PARA Medir Tiempo 1ra pulsacion SIN Interrupciones
# Ref : Get started with MicroPython on Raspberry Pi Pico
# 1.0 

from machine import Pin # Get the Pin function from the machine module.
from utime import sleep, ticks_ms, ticks_diff # Get the sleep library from the time module.

# Informative block - start
p_ucontroler = "Pico W & Pico_"
p_keyOhw = "External switch on GPIO15 & pull-down 10k + int led + t espera"
p_project = "External switch - Time meas. no IRQ"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

PINPULSADOR = 15

# Define un objeto Pin en pin15, en modo entrada , con una resitencia de pull-down
# externa de 10k, es decir normalmente estará a estado Low, 0 voltios
# Nota : no usamos Pin(EXTERNAL_BUTTON, Pin.IN, Pin.PULL_DOWN) por el fallo
# de los RP2350 version A2
pulsador = Pin(PINPULSADOR, Pin.IN)
intled = machine.Pin("LED", machine.Pin.OUT)

# Enciende el led , lo mantien 2 segundo y lo apaga
intled.value(1)
sleep(2)
intled.value(0)
timer_start = ticks_ms() # guardamso el tiempo en milisegundos


while pulsador.value() == 0:
    pass

timer_reaction = ticks_diff(ticks_ms(), timer_start)
print("Your reaction time was " + str(timer_reaction) + " milliseconds!")

