# Desafio #6: Salvando um dicionário

Seu objetivo é implementar duas funções, `salvar_dicio()` e `carregar_dicio()`. A função `salvar_dicio()` recebe dois argumentos de entrada: o dicionário a ser salvo e o caminho do arquivo de saída. A função `carregar_dicio()` por sua vez recebe o caminho do arquivo em que o dicionário foi salvo como argumento de entrada e retorna o dicionário armazenado anteriormente.

## Exemplo de entrada e saída

```console
>>> salvar_dicio({1: 'a', 2: 'b', 3: 'c'}, 'dicio.pickle')
>>> print(carregar_dicio('dicio.pickle'))
# {1: 'a', 2: 'b', 3: 'c'}
```