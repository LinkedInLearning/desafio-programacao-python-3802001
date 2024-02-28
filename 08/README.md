# Desafio #8: Jogue “forca”

Seu objetivo é implementar uma função chamada `jogo_da_forca()`.

Essa função deverá exibir uma mensagem que exibe uma mensagem para quem joga:

- Mostrando o tema escolhido
- Um underline para cada letra da palavra
- A quantidade de tentativas restantes
- e um campo para entrada de uma letra

Além disso, a mensagem deve se manter na tela e atualizar com cada tentativa. As palavras devem ser escolhidas randomicamente de uma lista de palavras.

O objetivo de quem joga é adivinhar a palavra dentro da quantidade de tentativas disponíveis.

Tentativas incorretas diminuem a quantidade de tentativas restantes. Caso todas as tentativas acabem e a palavra não seja descoberta uma mensagem informando o fim do jogo e a palavra deve ser apresentado.

*Atenção:* Na solução apresentada neste repositório existem 4 temas possíveis. 

## Exemplo de entrada e saída

```console
>>> jogo_da_forca()
```

Com o fim do jogo por exemplo...

```console
Tema: frutas
Palavra: b a _ a _ a
Tentativas restantes: 2
Escolha uma letra: n
Acertou!
Parabéns, você adivinhou a palavra! A palavra era: banana
```