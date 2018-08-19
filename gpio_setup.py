# Usando os pinos GPIOS (General Purpose Input/Output ) nós vamos controlar a entrada e saída de dados da beagle bone
# Neste exemplo vamos simular saídas digitais ou seja valores lógicos on-high/off-low (1/0)
# A tensão aplicada na interface I/O vai de 0 (off-low) até 3.3V (on-high)
# Os pinos que estão disponíveis com interface GPIO podem ser vistos no diagrama, na imagem anexada ao repositório.
# Os pinos digitais são representados em verde no diagrama.
# Neste exemplo os pinos foram configurado para utilizar o HEADER P9, pinos do lado esquerdo da placa, de acordo com o diagrama.
# Para termos acesso a interface programável com python utilizaremos a biblioteca da Adafruit importando as configurações GPIO.

import Adafruit_BBIO.GPIO as GPIO

# Configurando os pinos que iremos utilizar, neste caso o pino P9_12 é configurado como pino de saída.
# GPIO.setup("P9_12",OUT)
# Devemos então setar a nossa configuração informando se o pino deverá atuar em nível lógico baixo (LOW/0) ou alto (HIGH/1)

GPIO.output("P9_12",GPIO.HIGH)
GPIO.output("P9_12",GPIO.LOW)

# Devemos então limpar os pinos configurados através do comando cleanup
 GPIO.cleanup()
