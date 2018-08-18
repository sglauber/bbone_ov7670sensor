# Beagle Bone Black
É uma placa de desenvolvimento disponível que assim como o Raspberry, propõe a ser um computador de baixo custo, onde podemos rodar versões do Linux, como o Debian e Angstrom (uma distribuição linux para embarcados.)

Para começar utilizá-la podemos utilizar apenas um cabo com conector mini USB, e é por meio desse cabo que será feita a alimentação do BeagleBone e também a comunicação com o computador.

 Este repositório tem o intuito de demonstrar o progresso de aprendizado na plataforma da beaglebone, algumas anotações e alguns códigos testes seram feitos e publicados aqui o diagrama citado em alguns dos scripts encontra-se abaixo e pode ser encontrado no site:

[TopTechBoy](http://www.toptechboy.com/beaglevone-black-rev-c/beaglebone-black-lesson-1-understanding-beaglebone-black-pinout/)

Diagrama, pinagem da beagle bone black:

![Diagrama](http://www.toptechboy.com/wp-content/uploads/2015/06/beaglebone-black-pinout.jpg)

# Códigos e bibliotecas

Abaixo alguns exemplos de códigos em python para serem testados com a beagle bone, podemos utilizar todas as linguagens nesta placa, basta importar as bibliotecas corretamente, links para algumas bibliotecas podem ser encontrados abaixo:

## Bibliotecas

Javascript - Bonescript http://beagleboard.org/Support/BoneScript

C - BBClip - https://github.com/sijpesteijn/BBCLib

C++ - BlackLib - https://github.com/yigityuce/BlackLib

## Códigos

```python
# Código para escritas digitais utilizanodo os pinos GPIO
import Adafruit_BBIO.GPIO as GPIO

# Configurando o pino 12 do HEADER P9 com saída
GPIO.setup("P9_12",OUT)
# Podemos atribuir níveis lógicos aos nossos pinos utilizando o método output através dos parâmetros (HIGH,LOW), também podemos utilizar (1 e 0)
GPIO.output("P9_12",HIGH)
GPIO.output("P9_12",LOW)
# Limpando as configurações
GPIO.cleanup()

```


```python
# Exemplo de código para leitura de entradas analógica
# Importando ADC - Analog to Digital Converter
import Adafruit_BBIO.ADC as ADC
ADC.setup()
while true:
# Utiliza-se 1.8 pois este é o valor máximo suportado pelos pinos de entrada analógica
    reading = ADC.read("P9_33") * 1.8
    print("Value is: ", reading)
```

```python
# Exemplo de código para trabalhar com Pulse with Modulation
# Podemos simularr pulsos analógicos, com frequência, através destes pinos
import Adafruit_BBIO.PWM as PWM

PWM.start("P8_13",0, 1000)
# Atribuindo o ciclo de trabalho após inicialização
# Isto pode ser feito através do metódo set_duty_cycle
PWM.set_duty_cycle("P8_13",100)
# Parando as configurações
PWM.stop("P8_13")
# Limpando as configurações
PWM.cleanup()
```
