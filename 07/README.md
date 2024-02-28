# Desafio #7: Agendamento de funções

Seu objetivo é implementar uma função chamada `agendar_funcao()`, que recebe três argumentos de entrada:

- horário em que executar uma função específica;
- a função que você deseja executar; e
- um número variável (zero ou mais) de argumentos que são passados para a função de agendamento para uso.

## Exemplo de entrada e saída

```console
>>> agendar_funcao(time.time() + 3, print, 'Olá!')
# print() agendado para Sun Jan 28 01:18:06 2024
```

Então, 3 segundos depois...

```console
Olá!
```