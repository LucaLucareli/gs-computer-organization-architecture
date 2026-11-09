import machine
import utime
import time

time.sleep(0.1) 
print("Iniciando Sistema da Bengala Inteligente (Versão Orientada a Objetos)...")

class SensorUltrassonico:
    """Classe responsável por gerir o hardware do sensor HC-SR04"""
    def __init__(self, trigger_pin, echo_pin):
        self.trigger = machine.Pin(trigger_pin, machine.Pin.OUT)
        self.echo = machine.Pin(echo_pin, machine.Pin.IN)

    def medir_distancia(self):
        # Gera o pulso de gatilho
        self.trigger.low()
        utime.sleep_us(2)
        self.trigger.high()
        utime.sleep_us(5)
        self.trigger.low()
        
        timeout = utime.ticks_us()
        
        # Capta o início do eco
        while self.echo.value() == 0:
            sinal_desligado = utime.ticks_us()
            if utime.ticks_diff(utime.ticks_us(), timeout) > 30000:
                return -1 # Timeout
                
        # Capta o fim do eco
        while self.echo.value() == 1:
            sinal_ligado = utime.ticks_us()
            if utime.ticks_diff(utime.ticks_us(), timeout) > 30000:
                return -1 # Timeout
                
        tempo_passado = sinal_ligado - sinal_desligado
        distancia = (tempo_passado * 0.0343) / 2
        return distancia

class SistemaAlerta:
    """Classe responsável por atuar nos sinais sonoros e visuais (Buzzer e LED)"""
    def __init__(self, buzzer_pin, led_pin):
        self.buzzer = machine.PWM(machine.Pin(buzzer_pin))
        self.led = machine.Pin(led_pin, machine.Pin.OUT)
        self.desligar()
        self.ultimo_bipe = utime.ticks_ms()
        self.estado_bipe = False

    def alerta_perigo(self):
        # Som contínuo e LED fixo (Risco Iminente)
        self.buzzer.duty_u16(32768)
        self.buzzer.freq(1000)
        self.led.value(1)

    def alerta_atencao(self, distancia):
        # Calcula o intervalo do bipe dinamicamente com base na distância
        # 50cm = bipe rápido (aprox 150ms) | 150cm = bipe lento (aprox 450ms)
        intervalo_ms = int(distancia * 3) 
        
        agora = utime.ticks_ms()
        # Lógica não-bloqueante (substitui o utime.sleep)
        if utime.ticks_diff(agora, self.ultimo_bipe) > intervalo_ms:
            self.ultimo_bipe = agora
            self.estado_bipe = not self.estado_bipe
            
            if self.estado_bipe:
                self.buzzer.duty_u16(32768)
                self.buzzer.freq(500)
                self.led.value(1)
            else:
                self.buzzer.duty_u16(0)
                self.led.value(0)

    def desligar(self):
        self.buzzer.duty_u16(0)
        self.led.value(0)

sensor = SensorUltrassonico(trigger_pin=15, echo_pin=14)
alerta = SistemaAlerta(buzzer_pin=16, led_pin=17)

# Variáveis para o Filtro de Média Móvel
historico_leituras = []
TAMANHO_FILTRO = 3

# Loop Principal
while True:
    dist_atual = sensor.medir_distancia()
    
    if dist_atual > 0:
        # 1. Filtro de Média Móvel (Suavização de Dados)
        historico_leituras.append(dist_atual)
        if len(historico_leituras) > TAMANHO_FILTRO:
            historico_leituras.pop(0) # Remove a leitura mais antiga
            
        dist_suavizada = sum(historico_leituras) / len(historico_leituras)
        
        # 2. Avaliação de Regras de Negócio
        print("Distância: {:.2f} cm".format(dist_suavizada))
        
        if dist_suavizada < 50:
            alerta.alerta_perigo()
        elif dist_suavizada < 150:
            alerta.alerta_atencao(dist_suavizada)
        else:
            alerta.desligar()
    else:
        print("Erro na leitura do sensor.")
        alerta.desligar()
        
    # Pausa minúscula apenas para não esgotar 100% da CPU do microcontrolador à toa
    utime.sleep_ms(30)