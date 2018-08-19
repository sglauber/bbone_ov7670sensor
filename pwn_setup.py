# Diferente de valores digitais (0 ou 1) os valores analógicos são variáveis.
# Valores digitais são usados pra representar informações como: ligado / desligado, aberto ou fechado.
# Utilizando valores analógico por exemplo, podemos trabalhar com uma "porcentagem" em determinada situação.
# Por exemplo uma porta está aberta, (valor lógico 1), mas... o quanto ela está aberta?
# Esta informação nos seria dada através de uma informação analógico.

# Aqui nós vamos simular escritas analógicas usando PWM (Pulse Width Modulation) ou Modução por Largura de Pulso
# Podemos simular valores analógicos ligando e desligando a tensão do nosso sistema rapidamente para assim, gerar a informação analógica.
# Neste exemplo utilizaremos os pinos roxos.
# Aqui utilizaremos os pinos do HEADER P8 (lado direito), P8_13 .
# Estas informações estão representados no diagrama.

# Para termos acesso a interface programável com python utilizaremos a biblioteca da Adafruit importando as configurações PWM.

import Adafruit_BBIO.PWM as PWM

# Vamos configurar a saída que iremos utilizar.
# Aqui iremos setar o nosso ciclo de trabalho (duty cycle), este valor é dado em porcentagem e também a frequência, em Hz.
# PWM.start("PIN_Reference" DutyCycle %, Frequency Hz).
# Configurando nossa saída, iremos iniciar em 0 ou seja a saída está desligada e não deve gerar nenhuma tensão.

PWM.start("P8_13",0, 1000)

# Através do metódo set_duty_cycle() podemos reescrever o nosso ciclo de trabalho
# Tendo um ciclo de trabalho de 100%, o que significa que agora a nossa saída está a "todo o vapor" e deve gerar uma tensão de 3.3V.
PWM.set_duty_cycle("P8_13",100)

# Vamos utilizaar um input(), pedir ao usuário um valor, para assim setar o nosso ciclo de trabalho.
# Pediremos a ele a tensão desejada e como iremos modificar o ciclo de trabalho converteremos o valor da tensão para a porcentagem correspondente.
# A nossa tensão máxima é aproximadamente 3.365V
# Devemos tomar cuidado para não ultrapassar este valor e para isto utilizaremo uma condicional, já que o nosso ciclo de trabalho não deve ser maior que 100%.
# Nosso código terá a seguinte estrutura:

tensao = input("Qual a tensão desejada?: ")
ciclo = tensao/3.365*100
if (ciclo > 100):
    ciclo = 100

# Então reescreveramos nossa saída com o valor informado pelo usuário

PWM.set_duty_cycle("P8_13",ciclo)

# Podemos modificar a frequência através do metódo set_frequency()
# Porém alterar a frequência neste caso não irá afetar em nada pois estamos nos baseando em nosso ciclo de trabalho.
# PWM.set_frequency("P8_13", 100)

# Devemos então parar as configurações
PWM.stop("P8_13")
# E limpar nossas saídas
PWM.cleanup()
