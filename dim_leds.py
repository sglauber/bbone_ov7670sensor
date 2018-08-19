# Usando as saídas PWM da nossa BBBlack podemos controlar a intensidade do brilho de LEDs ou velocidade de um motor, ou seja "variar".
# Utilizaremos os pinos do HEADER P9 P9_14 e P9_22

# Para termos acesso a interface programável com python utilizaremos a biblioteca da Adafruit importando as configurações PWM.

import Adafruit_BBIO.PWM as PWM

# Configurando e inicializando nossas saídas

PWM.start("P9_14",0,1000)
PWM.start("P9_22",0,1000)

# for() loop onde perguntaremos ao usuário um valor entre 0 - 7 que alterará o brilho dos noss LEDS.

for i in range(0,5):
        valor_led1 = input("Brightness top (0 - 7): ")
        valor_led2 = input("Brightness bottom (0 - 7): ")
        ciclo_led1 = 2**valor_led1
        ciclo_led2 = 2**valor_led2

# Devemos ter certeza que o valor não irá ultrapassar 100%

        if brilho_led1 > 100:
            ciclo_led1 = 100
        if brilho_led2 > 100:
            ciclo_led2 = 100

# Configurando o nosso ciclo de trabalho para os valores informados através do metódo set_duty_cycle()
        PWM.set_duty_cycle("P9_14",ciclo_led1)
        PWM.set_duty_cycle("P9_22",ciclo_led2)

# Parando configurações

PWM.stop("P9_14")
PWM.stop("P9_22")

# Limpando as configurações
PWM.cleanup()
