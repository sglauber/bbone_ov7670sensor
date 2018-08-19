# As entradas digitais só podem assumir dois estados, HIGH e LOW, 0 e 1.
# Dessa forma só é possível ler apenas dois estados.
# Para verificar se uma porta está aberta ou fechada, identificar se um botão está pressionado ou solto, etc.
# Para leitura de um sinal analógico utilizamos a conversão analógico -> digital.
# Consiste em converter o sinal analógico para um valor digital, podendo assim quantificar o sinal presente no pino.

# Neste exemplo faremos leituas analógicas de uma das entradas.
# Estas leituras podem ser feitas utilizando os pinos azuis AnalogIN (ver diagrama).

# As leituras analógicas podem ser realizadas utilizando um potênciometro, push buttons ou um componente que seja de seu desejo.
# Aqui utilizaremos um potênciometro.
# Para termos acesso a interface programável com python utilizaremos a biblioteca da Adafruit importando as configurações ADC
# ADC - Analag to Digital Converter

import Adafruit_BBIO.ADC as ADC

# Iniciando nossa configuração

ADC.setup()

# Iremos importar sleep() para que possamos ter uma melhor visualização dos valores lidos.

from time import sleep

while 1:

    # Aqui iremos configurar a opção de leitura na entrada desejada, neste caso, o pino 33 no HEADER P9.
    # Utilizaremos também o pinos 32 P9_32 como nossa alimentação (pinos vermelhos) VDD.
    # E o pino 34 P9_34 como nosso ground (pinos vermlhos) GND.
    # Teremos então um potênciometro com os conectores esquerdo / direito ao nosso vdd/gnd e o conector central conectado ao P9_33 AnalogIN

    reading = ADC.read("P9_33")

    # Através do método read() teremos um valor em porcentagem correspondente a tensão que potenciômetro nos envia.
    # Este valor pode variar de 0V a 1.8V, tendo 0 teríamos 0% e 1.8 teríamos 100%.
    # O valor máximo da tensão para estes pinos deve ser 1.8V, valores maiores poderão danificar a placa.
    # Neste exemplo vamos analisar a voltagem aplicada, multiplicando a porcentagem lida por 1.8V.

    reading = reading * 1.8
    print("Value is: ", reading)
    sleep(0.5)

    # Se estiver executando no terminal, pressione Ctrl + D ou Ctrl + Z para encerrar a execução.
