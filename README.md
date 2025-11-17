# CL5 - R Juego Tiempo Reaccion con LCD  x1 y x2 jugadores - Pulsadores y LCD

Indice evolutivo del las clases del taller + libros y webs de referencia:

[GitHub - Jcspoza/2526_PyR_Index: Curso Programación y Robotica 2025 2026 - CMM BML](https://github.com/Jcspoza/2526_PyR_Index)

## Clase 5 - Indice - 90 minutos

- Materiales y links a información

- Propuesta de proyecto

- Plan de trabajo : prototipado en 2 Dimensiones 

- 

- Tabla resumen de programas

- TO DO

## Materiales y links a informacion

| Material                                                                                                              | Descripcion                                                                                                                     | Kit SF |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |:------:|
| [Protoboard 400 o 700](https://docs.sunfounder.com/projects/kepler-kit/en/latest/component/component_breadboard.html) | Placa para prototipos ver apartado [Uso de la protoboard](https://github.com/Jcspoza/2526CL1_R_CircElect0#uso-de-la-protoboard) | SI     |
| [Cables dupond M-M](https://docs.sunfounder.com/projects/kepler-kit/en/latest/component/component_wire.html)          | Sirven para hacer conexiones en protoboard                                                                                      | SI     |
| [Led rojo](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_led.html)                   | Se usara para indicar comienzo de cuenta de Tiempo de reacción                                                                  | SI     |
| [Resistencia 220 ohm](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_resistor.html)   | Resistencia 220 ohm para limitar corriente de LED                                                                               | SI     |
| [Pulsador x2](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_button.html)             | Pulsador para protoboard, su pulsación indicará fin de tiempo de reacción                                                       | SI     |
| [Resistencia 10k ohm](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_resistor.html)   | Resistencia de 10 K ohm para pull-Down                                                                                          | SI     |
| [LCD i2c 16x2](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_i2clcd1602.html)        | Display LCD con comunicación i2c, de 2 líneas de 16 caracteres cada una                                                         | SI     |

### Link a Tutoriales / informacion

- El juego se basa en el capitulo 6 del libro 

[Libro 'Get started with MicroPython on Raspberry Pi Pico'](https://github.com/Jcspoza/2526_PyR_Index/blob/main/doc/upython_RPi_PiPico_Digital_v10.pdf) que esta disponible también en la pagina de indice

- Tutorial sobre uso del LCD : ver la clase del año 24-25 [2425CL5_LCD primeros pasos](https://github.com/Jcspoza/CMM_Python_uP_PicoW/tree/main/2425CL5_LCD1st)

### Librerías importantes

Para el **LCD** usaremos la libreria del usuario T-622

[GitHub - T-622/RPI-PICO-I2C-LCD: to allow usage of the PCF8574 I2C lcd backpack for either 20x4 or 16x2 lcd screens.](https://github.com/T-622/RPI-PICO-I2C-LCD)

mejor que la que trae el kit. Es algo mas versátil y de uso mas común

## Propuesta de Proyecto

Vamos a hacer el **Juego de Tiempo de Reacción humana ante un evento** siguiendo el tutorial del libro 'Get started ...' 

Para hacerlo mas 'real' , vamos a llegar a un **prototipo autónomo**, es decir que no necesitemos el PC ni la consola de Thonny para jugar. Por tanto, necesitamos: 

1. un display para mostrar informacion -> usaremos el del kit : LCD i2c 2x16 + la libreria T-622
2. queremos que todo el proyecto tenga alimentación independiente del PC

## Plan de trabajo : prototipado en 2 Dimensiones

Vamos a escribir en una tabla por un lado los requisitos HW y por otro lado las pruebas básicas + pruebas de aprendizaje + programas con funcionalidades requeridas

| Prueba/ Funcionalidad                                                                 | Alimentación independiente                      | LCD          | Pulsador con interrupciones                                                                      | Medir Tiempo con pulsadores                                        |
| ------------------------------------------------------------------------------------- | ----------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| Pruebas de Aprendizaje                                                                |                                                 |              | Aprender / Entender pulsadores SIN interrupciones: contar pulsaciones: **PulsaScan** v1.0 y v2.1 |                                                                    |
| Pruebas de Aprendizaje                                                                |                                                 |              |                                                                                                  | Medir tiempo SIN interrupción: PulsaTime v1.0                      |
| Pruebas de Aprendizaje                                                                |                                                 |              | Entender pulsadores CON interrupciones, contar pulsaciones                                       |                                                                    |
| Pruebas de Aprendizaje                                                                |                                                 |              |                                                                                                  | Medir tiempo CON interrupciones PulsaTimeIrq v1.0, v2.0            |
| Test básico                                                                           |                                                 | Bhwt del LCD |                                                                                                  |                                                                    |
| Funcionalidad : Autonomía                                                             | Ejecutar BHWT de LCD con 1.batería Lipo => FAIL |              |                                                                                                  |                                                                    |
| Funcionalidad : Autonomía                                                             | Ejecutar BHWT de LCD con 2. Power bank => OK    |              |                                                                                                  |                                                                    |
| Funcionalidad: Medir tiempo Reacción 1 jugador CON Interrupciones                     |                                                 |              | X                                                                                                | Primeros prototipos Juego x1:  **JTReacX1_irq** :  v1.0, v2.0 v2.1 |
| Funcionalidades: Medir tiempo Reacción 1 jugador CON Interrupciones + LCD + powerbank | JTReacX1_irqLCD_1_0.py                          | X            | X                                                                                                | X                                                                  |

## 

## Aprender / Entender: pulsadores, interrupciones y medidas de tiempo

### SIN interrupciones: contar pulsaciones: **PulsaScan** v1.0 y v2.1

### SIN interrupciones: medir Tiempo: **PulsaTime** v1.0

#### Medir diferencias de tiempo en uC

### CON interrupciones: contar pulsaciones:

### CON interrupciones: medir Tiempo: **PulsaTime** v1.0

## Test Básico HW del LCD

En una rama paralela del nuestro trabajo en el proyecto vamos a usar el display LCD, sin entrar a dar muchas explicaciones. Ver tutorial sobre uso del LCD : ver la clase del año 24-25 [2425CL5_LCD primeros pasos](https://github.com/Jcspoza/CMM_Python_uP_PicoW/tree/main/2425CL5_LCD1st)

### Carga de las librerías

La libreria que usaremos esta dividida en 2 ficheros ( no es lo normal, es asi por razones históricas)

Hay que subir al directorio /lib de la Pico  / W / 2W

[lcd_api.py](lcd_api.py)

[pico_i2c_lcd.py](pico_i2c_lcd.py)

### Montaje HW

![]()



## Tabla resumen de programas

| Programa | Lenguaje | HW si Robotica y Notas | Objetivo de Aprendizaje |
| -------- | -------- | ---------------------- | ----------------------- |
|          |          |                        |                         |

---

## TO DO :
