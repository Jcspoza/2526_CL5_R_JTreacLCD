# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2025 - 11 - 16
# Goal : DEMO External switch in GPIO15 + Reaction Time example
# Learning Target : interruptions basic + LCD i2c
# Ref : Get started with MicroPython on Raspberry Pi Pico, pag 68 Reaction 1 player
# Versio0nes naterires Sin LCD
# 1.0 as is in book small changes
# 2.0 alguna mejora de limpieza
# 2.1 no espera 2 seg sino cuando salga de la interrupcion
# Con LCD
# 1.0 añado LCD y mensjes basicos a version 2.1 sin lcd

from machine import Pin, I2C  # Get the Pin & I2C modules from the machine module.
from urandom import uniform
from utime import sleep, ticks_diff, ticks_ms
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# Informative block - start
p_ucontroler = "Pico W / NO Pico _"
p_keyOhw = "External switch on GPIO15 IN pull down 10kohm"
p_project = "Game Reaction time x 1 player: w. interruption + LCD"
p_version = "1.0 with LCD based on 2.1 w/lcd"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0 - Creacion de objetos
# 0.1 Objeto pulsador y led externo
EXTERNAL_BUTTON = 15
pulsador = Pin(EXTERNAL_BUTTON, Pin.IN)

extled = Pin(16, Pin.OUT)

pressed = False
tiempoReaccion = None

#0.2 objeto LCD
LCD_ADDR = 0x3F
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16
FREQ = 400_000   # Try lowering this value in case of "Errno 5"
i2c = I2C(0, sda = Pin(4), scl = Pin(5), freq = FREQ)
lcd = I2cLcd(i2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

def manejaPulsador(pin):    
    global pressed, tiempoReaccion
    if not pressed:
        pressed=True
        tiempoReaccion = ticks_diff(ticks_ms(), tiempo_start)
         
# Fase 0- presentacion e instrucciones + configuracion interrupcion
print("El led se encendera y apagara. Tienes que pulsar despues de que se apague")
pulsador.irq(trigger=Pin.IRQ_RISING, handler=manejaPulsador)
lcd.move_to(0,0)
linea0 = 'Juego T. reac x1'
lcd.putstr(linea0)
lcd.move_to(0,1)
linea1 = 'Pulsa si led ->0'
lcd.putstr(linea1)

# Fase 1- Comienza el juego encendiendo el led
extled.value(1)
sleep(uniform(2, 5))
extled.value(0)
tiempo_start = ticks_ms() # aqui ponemos a cero el tiempo

# utime.sleep(2) # dejamos tiempo suficiente para que pulse el pulsador
# Todo : pasar de fase justo despues de pulsar
while not pressed:
    pass

# Fase 2- Fin del juego
lcd.clear()
linea0 = f'Tu T.reac={tiempoReaccion}ms'
lcd.putstr(linea0)
lcd.move_to(0,1)
linea1 = 'Fin J. T.reac x1'
lcd.putstr(linea1)

print(f"¡Tu tiempo de reaccion fue de  {tiempoReaccion} millisegundos!")
print('-------------- Fin del juego --------------')
