# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2025 - 11 - 16
# Goal : DEMO External switch in GPIO14 + Rection Time example
# Learning Target : interruptions basic
# Ref : Get started with MicroPython on Raspberry Pi Pico, pag 68 Reaction 1 player
# 1.0 as is in book small changes
# 2.0 alguna mejora de limpieza

from machine import Pin # Get the Pin function from the machine module.
from urandom import uniform
import utime  

# Informative block - start
p_ucontroler = "Pico W / NO Pico _"
p_keyOhw = "External switch on GPIO15 IN pull down"
p_project = "Reaction time with interruption"
p_version = "2.0 as is in book + clean code"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

EXTERNAL_BUTTON = 15
pulsador = Pin(EXTERNAL_BUTTON, Pin.IN, Pin.PULL_DOWN)

intled = Pin(16, Pin.OUT)

pressed = False
tiempoReaccion = None 

def manejaPulsador(pin):    
    global pressed, tiempoReaccion
    if not pressed:
        pressed=True
        tiempoReaccion = utime.ticks_diff(utime.ticks_ms(), tiempo_start)
         
# Fase 0- presentacion e instrucciones + configuracion interrupcion
print("El led se encendera y apagara. Tienes que pulsar despues de que se apague")
pulsador.irq(trigger=Pin.IRQ_RISING, handler=manejaPulsador)

# Fase 1- Comienza el juego encendiendo el led
intled.value(1)
utime.sleep(uniform(2, 5))
intled.value(0)
tiempo_start = utime.ticks_ms() # aqui ponemos a cero el tiempo

utime.sleep(2) # dejamos tiempo suficiente para que pulse el pulsador
# Todo : pasar de fase justo despues de pulsar

# Fase 2- Fin del juego
print(f"¡Tu tiempo de reaccion fue de  {tiempoReaccion} millisegundos!")
print('-------------- Fin del juego --------------')
