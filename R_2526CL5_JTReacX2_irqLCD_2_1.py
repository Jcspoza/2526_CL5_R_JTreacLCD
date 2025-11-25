# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2025 - 11 - 24
# Goal : Crear un juego completo x2 jugadores de 'Reaction Time example'
# Learning Target : interruptions basic learning + LCD i2c
# Ref : Get started with MicroPython on Raspberry Pi Pico, pag 68 Reaction 1 player
# Versiones naterires Sin LCD
# 1.0 as is in book small changes
# 2.0 alguna mejora de limpieza
# 2.1 no espera 2 seg sino cuando salga de la interrupcion
# Con LCD
# 1.0 añado LCD y mensajes basicos a version 2.1 sin lcd
# 2.1 ampliacion a 2 jugadores basado en 2.1 x2 jugadores sin LCD

from machine import Pin, I2C, reset  # Get the Pin & I2C modules from the machine module.
from urandom import uniform
from utime import sleep, ticks_diff, ticks_ms
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# Informative block - start
p_ucontroler = "Pico W / NO Pico _"
p_keyOhw = "External switch on GPIO14 & 15 IN pull down 10kohm"
p_project = "Game Reaction time x 2 player: w. interruption + LCD + 2 end var"
p_version = "2.1 with LCD based on 3.0 w/lcd"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0 - Creacion de objetos
# 0.1 Objeto pulsadores y led externo
PINPULSADORA = 15
PINPULSADORD = 17
pulsadorA = Pin(PINPULSADORA, Pin.IN)
pulsadorD = Pin(PINPULSADORD, Pin.IN)

extled = Pin(16, Pin.OUT)

# 0.2 Variables generales
pulsado = False
pulsadorMasRapido = None
tiempoReaccion = None

#0.3 objeto LCD
LCD_ADDR = 0x3F
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16
FREQ = 400_000   # Try lowering this value in case of "Errno 5"
i2c = I2C(0, sda = Pin(4), scl = Pin(5), freq = FREQ)
lcd = I2cLcd(i2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

# F- Funciones
def pulsador_quehacer(pin):    
    global pulsado, tiempoReaccion, pulsadorMasRapido
    if not pulsado:
        pulsado=True
        tiempoReaccion = ticks_diff(ticks_ms(), tiempo_start)
        pulsadorMasRapido = pin # otra forma de pasar parametros / es de tipo Pin
        print(pin)
       
# Fase 1- presentacion e instrucciones 
print("El led se encendera y apagara. Cada jugador tiene que pulsar despues de que se apague")
lcd.move_to(0,0)
linea0 = 'Juego T. reac x2'
lcd.putstr(linea0)
lcd.move_to(0,1)
linea1 = 'Pulsad si led->0'
lcd.putstr(linea1)

# Fase 2- Comienza el juego encendiendo el led + configuracion interrupcion
extled.value(1)
sleep(uniform(2, 5))
extled.value(0)
tiempo_start = ticks_ms() # aqui ponemos a cero el tiempo
# No debemos configurar antes las interrupciones, para que un apulsacion antes de led -> 0
# dispare la interrupcion
pulsadorD.irq(trigger=Pin.IRQ_RISING, handler=pulsador_quehacer)
pulsadorA.irq(trigger=Pin.IRQ_RISING, handler=pulsador_quehacer)

# Espero a pasar de fase justo despues de pulsar
while not pulsado:
    pass

# Fase 3- Fin del juego
lcd.clear()
if pulsadorMasRapido == pulsadorA:
    print('Ganó el pulsador A')
    print(f"¡Su tiempo de reaccion fue de  {tiempoReaccion} millisegundos!")
    linea0 = 'Gano A- FIN TRx2'
    lcd.putstr(linea0)
    lcd.move_to(0,1)
    linea1 = f'Su T.reac={tiempoReaccion}ms'
    lcd.putstr(linea1)
else:
    print('Ganó el pulsador D')
    print(f"¡Su tiempo de reaccion fue de  {tiempoReaccion} millisegundos!")
    linea0 = 'Gano D- FIN TRx2'
    lcd.putstr(linea0)
    lcd.move_to(0,1)
    linea1 = f'Su T.reac={tiempoReaccion}ms'
    lcd.putstr(linea1)
    
print('-------------- Fin del juego x2 --------------')



