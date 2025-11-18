# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2025 - 11 - 16
# Goal : DEMO External switch in GPIO14 + Rection Time example
# Learning Target : interruptions basic
# Ref : Get started with MicroPython on Raspberry Pi Pico, pag 68 Reaction 1 player
# 1.0 as is in book small changes
# 2.0 alguna mejora de limpieza
# 2.1 no espera 2 seg sino cuando salga de la interrupcion

from machine import Pin # Get the Pin function from the machine module.
from urandom import uniform
from utime import sleep, ticks_ms, ticks_diff

# Informative block - start
p_ucontroler = "Pico W / NO Pico _"
p_keyOhw = "External switch on GPIO15 IN pull down"
p_project = "Reaction time with interruption"
p_version = "2.0 as is in book + clean code"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0 - Creacion de objetos
# 0.1 Objeto pulsador y led externo
PINPULSADOR = 15
pulsador = Pin(PINPULSADOR, Pin.IN)

extled = Pin(16, Pin.OUT)

# 0.2 Variables generales
pulsado = False
tiempoReaccion = None 

# F- Funciones 
def pulsador_quehacer(pin):    
    global pulsado, tiempoReaccion
    if not pulsado:
        pulsado=True
        tiempoReaccion = ticks_diff(ticks_ms(), tiempo_start)
         
# Fase 1 - presentacion e instrucciones + configuracion interrupcion
print("El led se encendera y apagara. Tienes que pulsar despues de que se apague")
pulsador.irq(trigger=Pin.IRQ_RISING, handler=pulsador_quehacer)

# Fase 2- Comienza el juego encendiendo el led
extled.value(1)
sleep(uniform(2, 5))
extled.value(0)
tiempo_start = ticks_ms() # aqui ponemos a cero el tiempo

# Espero a pasar de fase justo despues de pulsar
while not pulsado:
    pass

# Fase 3- Fin del juego
print(f"¡Tu tiempo de reaccion fue de  {tiempoReaccion} millisegundos!")
print('-------------- Fin del juego --------------')
