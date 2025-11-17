# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2023 - 4 - 13
# Goal : Aprender uso de pulsador PARA CONTAR SIN Interrupciones
# Ref : Get started with MicroPython on Raspberry Pi Pico
# 1.0 -> 1.2 se puede cambiar el tiempo de espera

from machine import Pin # Get the Pin function from the machine module.
from utime import sleep # Get the sleep library from the time module.

# Informative block - start
p_ucontroler = "Pico W & Pico_"
p_keyOhw = "External switch on GPIO15 & pull-down 10k + int led + t espera"
p_project = "External switch Count - wait time config"
p_version = "1.2"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

PINPULSADOR = 15

# Define un objeto Pin en pin15, en modo entrada , con una resitencia de pull-down
# externa de 10k, es decir normalmente estará a estado Low, 0 voltios
# Nota : no usamos Pin(EXTERNAL_BUTTON, Pin.IN, Pin.PULL_DOWN) por el fallo
# de los RP2350 version A2
pulsador = Pin(PINPULSADOR, Pin.IN)
veces = 0
intled = machine.Pin("LED", machine.Pin.OUT)

espera = int(input('Tiempo de espera desde una deteccion a siguient en milisegundos? = ' ))/1000

while True:
    if pulsador.value() == 1:
        veces += 1 # es lo mismo que veces = veces + 1
        intled.toggle() # invierte el estado del LED
        print(f"Has presionado el pulsador {veces} veces")
# una cadena con f sustituye lo que hay dentro de las llaves con el valor de la variable
        sleep(espera)
