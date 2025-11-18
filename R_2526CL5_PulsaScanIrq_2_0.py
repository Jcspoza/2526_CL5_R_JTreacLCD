# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2023 - 4 - 13
# Goal : Aprender uso de interrupciones y pulsador
# Ref : Get started with MicroPython on Raspberry Pi Pico
# 1.0 -> 1.2 se puede cambiar el tiempo de espera
# 2.0 : rechacer programa para que use interrupciones para contar

from machine import Pin # Get the Pin function from the machine module.
from urandom import uniform
import utime  

# Informative block - start
p_ucontroler = "Pico W / NO Pico _"
p_keyOhw = "External switch on GPIO15 & pull-down 10k + int led"
p_project = "Switch with interruption and loop No Debouncing"
p_version = "2.0 interupciones - sin manejo rebotes"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

EXTERNAL_BUTTON = 15
pulsador = Pin(EXTERNAL_BUTTON, Pin.IN)

intled = Pin("LED", Pin.OUT)
intled.on()

veces_pulsadas = 0

def manejaPulsador(pin):    
    global veces_pulsadas
    veces_pulsadas += 1
    

pulsador.irq(trigger=Pin.IRQ_RISING, handler=manejaPulsador)
veces_pulsadas_viejo = 0
while True:
    print('hago cosas y enciendo parpadeo el led, con tiempo aleatorio')
    utime.sleep(uniform(1, 4))
    if veces_pulsadas_viejo != veces_pulsadas:
       print('Veces pulsadas = ', veces_pulsadas)
       veces_pulsadas_viejo = veces_pulsadas
       
    intled.toggle()
