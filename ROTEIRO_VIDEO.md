# 🎬 Roteiro Oficial do Vídeo Demonstrativo – CitizenTech

> **Projeto:** Bengala Inteligente com Sensor Ultrassônico e Alerta Multissensorial  
> **Disciplina:** Computer Organization and Architecture (Prof. Dr. Marcus Grilo)  
> **Atividade:** Global Solution (GS 2026.2)  
> **Duração Estimada:** 3 a 5 minutos  
> **Plataforma de Envio:** YouTube (Formato *Não Listado* ou *Público*)  

---

## 📋 Checklist Pré-Gravação

Antes de iniciar a gravação, certifique-se de:
- [ ] Ter a simulação aberta no [Wokwi](https://wokwi.com) com o zoom ajustado para enquadrar perfeitamente a Raspberry Pi Pico, o sensor HC-SR04, o Buzzer, o LED e a janela do Terminal Serial.
- [ ] Verificar se o som do sistema está sendo capturado pelo software de gravação (ex: OBS Studio, Loom, Google Meet ou Teams) para que o som do Buzzer do Wokwi seja audível no vídeo.
- [ ] Garantir microfone limpo, sem eco e em ambiente silencioso.
- [ ] Manter o código `main.py` aberto em uma aba do navegador ou editor para exibição rápida durante a explicação da lógica.
- [ ] Todos os integrantes estarem cientes de suas respectivas falas ou um representante apresentar citando nominalmente todos os membros e RMs.

---

## ⏱️ Cronograma e Divisão de Cenas

| Cena | Tempo Estimado | Foco Principal | Responsável Sugerido |
| :---: | :---: | :--- | :--- |
| **1** | 0:00 – 0:45 | Abertura, identificação dos integrantes e contexto da disciplina | Integrante 1 |
| **2** | 0:45 – 1:30 | O problema social urbano e o público afetado (CitizenTech) | Integrante 2 |
| **3** | 1:30 – 2:30 | Apresentação da solução, componentes e circuito montado | Integrante 3 |
| **4** | 2:30 – 4:00 | Demonstração prática no Wokwi (mudança de sensores e saídas) | Integrante 4 |
| **5** | 4:00 – 4:45 | Destaques da programação em MicroPython e conclusão | Integrante 5 |

*(Nota: Caso a gravação seja feita por menos pessoas ou individualmente, o apresentador pode seguir todas as etapas na sequência).*

---

## 🎙️ Roteiro Detalhado (Script Fala a Fala)

---

### 🟢 Cena 1: Abertura e Identificação (0:00 – 0:45)
**O que mostrar na tela:** Slide inicial ou tela do projeto no Wokwi com o circuito visível e câmera dos integrantes ativa.

> **Fala (Apresentador / Integrante 1):**  
> *"Olá, professor Marcus Grilo e a todos que estão assistindo!  
> Nós somos alunos da FIAP e estamos apresentando o nosso projeto da Global Solution da disciplina de **Computer Organization and Architecture**, referente ao tema **CitizenTech – Tecnologia Cidadã**.*  
>  
> *O nosso grupo é composto pelos seguintes integrantes:*  
> * *`[Nome do Integrante 1]` - RM `[Número]`*  
> * *`[Nome do Integrante 2]` - RM `[Número]`*  
> * *`[Nome do Integrante 3]` - RM `[Número]`*  
> * *`[Nome do Integrante 4]` - RM `[Número]`*  
> * *`[Nome do Integrante 5]` - RM `[Número]`*  
>  
> *O nosso projeto é o protótipo de uma **Bengala Inteligente com Detecção de Obstáculos Aéreos e Alerta Multissensorial**, desenvolvido com a placa **Raspberry Pi Pico** na plataforma Wokwi."*

---

### 🟡 Cena 2: O Problema Social e o Público Afetado (0:45 – 1:30)
**O que mostrar na tela:** Diagrama conceitual ou manter foco na apresentação destacando o tema de Acessibilidade Urbana.

> **Fala (Integrante 2):**  
> *"Dentro do pilar de **Acessibilidade e Mobilidade Urbana**, identificamos um problema crítico enfrentado diariamente por pessoas com deficiência visual severa ou cegueira total.*  
>  
> *A bengala longa convencional é excelente para identificar desníveis, degraus e buracos no chão. No entanto, ela possui um ponto cego perigoso: **não detecta obstáculos suspensos ou aéreos**, como orelhões, galhos baixos de árvores, lixeiras suspensas, placas de trânsito ou caçambas de entulho.*  
>  
> *Isso gera frequentes colisões na altura da cabeça e do tronco, causando acidentes físicos e medo de se locomover pela cidade. A nossa proposta CitizenTech foi aplicar a computação física e a Internet das Coisas para criar uma solução de baixo custo, eficiente e proativa, garantindo maior autonomia e dignidade para esse público."*

---

### 🟠 Cena 3: A Solução e os Componentes Eletrônicos (1:30 – 2:30)
**O que mostrar na tela:** Zoom no circuito montado no Wokwi, apontando com o cursor para cada um dos componentes.

> **Fala (Integrante 3):**  
> *"Para resolver esse problema, projetamos um sistema embarcado inteligente. Vamos apresentar os componentes que integram o nosso circuito:*  
>  
> 1. *Como cérebro do projeto, utilizamos a **Raspberry Pi Pico**, equipada com o microcontrolador RP2040 e programada em MicroPython.*  
> 2. *Como sensor de entrada, usamos o **Sensor Ultrassônico HC-SR04**, posicionado na bengala para realizar a varredura frontal constante. Ele está conectado aos pinos GP15 (Trigger) e GP14 (Echo).*  
> 3. *Para o feedback sensorial sonoro, conectamos um **Buzzer Piezoelétrico** na porta GP16, controlado via modulação PWM para produzir alertas dinâmicos.*  
> 4. *E como feedback visual de segurança para alertar também pessoas ao redor, utilizamos um **LED Difuso Vermelho** acoplado ao pino GP17 com um resistor limitador de 220 ohms.*  
>  
> *Agora, vamos demonstrar a simulação em tempo real e como as entradas dos sensores geram respostas imediatas nos atuadores."*

---

### 🔴 Cena 4: Demonstração Prática no Wokwi (2:30 – 4:00)
> ⚠️ **Atenção (Critério Obrigatório do Edital):** Demonstre de forma bem clara a alteração no controle deslizante do sensor e a reação imediata do circuito!

**O que mostrar na tela:** Clique no botão verde de **Play (▶️)** no Wokwi, abra a janela do **Terminal Serial** e clique no sensor **HC-SR04** para exibir o controle deslizante de distância.

> **Fala (Integrante 4):**  
> *(Inicia a simulação no Wokwi)*  
> *"Iniciando a simulação... Como podem ver no terminal serial, o sistema inicializa e já começa a fazer o monitoramento contínuo da distância.*  
>  
> *(Arrasta o slider do sensor para 250 cm)*  
> * **1. Teste da Zona Segura (Acima de 150 cm):**  
> *Neste momento, o obstáculo está a mais de 150 centímetros. O caminho está livre. O LED permanece totalmente apagado e o buzzer em silêncio absoluto, economizando bateria e sem perturbar o usuário.*  
>  
> *(Arrasta o slider gradualmente para 100 cm e depois para 70 cm)*  
> * **2. Teste da Zona de Atenção (Entre 50 cm e 150 cm):**  
> *Agora aproximamos um obstáculo para 100 centímetros. Percebam que o Buzzer começou a emitir bipes intermitentes e o LED começou a piscar de forma sincronizada.*  
> *O grande diferencial da nossa lógica é que o bipe é **proporcional e dinâmico**: conforme eu aproximo o obstáculo de 100 cm para 60 cm, o intervalo entre os bipes diminui e o som fica mais rápido, permitindo que a pessoa com deficiência visual saiba intuitivamente se está se aproximando ou se afastando do perigo!*  
>  
> *(Arrasta o slider para 30 cm)*  
> * **3. Teste da Zona de Perigo Crítico (Abaixo de 50 cm):**  
> *Ao atingir menos de 50 centímetros, entramos na zona de risco iminente de colisão. Imediatamente o Buzzer passa a emitir um som contínuo e estridente em 1000 Hertz e o LED fica aceso fixo, indicando parada imediata!"*

---

### 🟣 Cena 5: Diferenciais de Código e Conclusão (4:00 – 4:45)
**O que mostrar na tela:** Mostrar rapidamente o arquivo `main.py` destacando as classes e o loop principal, finalizando com a tela de agradecimento.

> **Fala (Integrante 5):**  
> *"Do ponto de vista de arquitetura de software embarcado, implementamos três boas práticas cruciais no código em MicroPython:*  
> 1. * **Orientação a Objetos:** Classes dedicadas para o `SensorUltrassonico` e o `SistemaAlerta`, garantindo código limpo e modular.*  
> 2. * **Filtro de Média Móvel:** Suavização das últimas 3 leituras do sensor para filtrar falsos ecos e ruídos de leitura.*  
> 3. * **Lógica Não-Bloqueante:** Em vez de usar `sleep()`, utilizamos `utime.ticks_ms()` e cálculo delta, permitindo que o microcontrolador continue lendo o sensor sem travar a execução enquanto o alarme toca.*  
>  
> *Com essa solução simples, acessível e de baixo custo, comprovamos como a computação física e a disciplina de Arquitetura de Computadores podem ser aplicadas diretamente no conceito de CitizenTech, transformando e protegendo a vida de milhares de cidadãos.*  
>  
> *Muito obrigado pela atenção de todos!"*

---

## 💡 Dicas de Gravação e Produção

1. **Ferramenta de Gravação Recomendada:**
   - **OBS Studio:** Permite gravar tela inteira com excelente nitidez e capturar o áudio do navegador perfeitamente.
   - **Google Meet ou Teams:** Excelente caso o grupo queira gravar remotamente com todos os membros com webcam ligada.
2. **Configuração de Áudio do Wokwi:**
   - No arquivo `diagram.json`, o buzzer já está configurado com volume moderado (`"volume": "0.1"`). Ao simular, clique na aba do simulador para que o navegador libere a reprodução de áudio.
3. **Publicação no YouTube:**
   - Ao fazer o upload no YouTube, selecione a visibilidade **"Não listado"** (qualquer pessoa com o link pode assistir, sem ficar público nas buscas) ou **"Público"**.
   - Copie o link do vídeo e cole-o no campo indicado no [`README.md`](README.md).

