# Desafio #4: Jogue o jogo de espera

Seu objetivo é implementar uma função, `jogo_de_espera()`, que exibe uma mensagem para quem joga esperar por um tempo aleatório, entre dois e quatro segundos. Quando a pessoa jogando pressionar “Enter”, um cronômetro é iniciado. O objetivo de quem joga é esperar o número de segundos especificado e, em seguida, pressionar “Enter” novamente. Isso exibe o tempo decorrido, juntamente com uma mensagem informando se a pessoa jogando foi muito rápida, muito lenta ou se acertou em cheio.

## Exemplo de entrada e saída

```console
>>> jogo_de_espera()

Seu objetivo é de 2 segundos
 ---Pressione Enter para começar---

...Pressione Enter de novo depois de 2 segundos...

Tempo decorrido: 2.100 segundos
Iiii... Devagar demais... Sobrou (0.100 segundos)
```