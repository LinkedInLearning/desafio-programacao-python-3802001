import re

def eh_palindromo(frase):
    correta = ''.join(re.findall(r'[a-z]+', frase.lower()))
    revertida = correta[::-1]
    return correta == revertida


# comandos usados na vídeo para referência
if __name__ == '__main__':
    print(eh_palindromo("Olá mundo!"))  # False
    print(eh_palindromo("Socorram-me, subi no ônibus em Marrocos!"))  # True