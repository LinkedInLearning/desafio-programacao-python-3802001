def fatores_primos(numero):
    fatores = []
    divisor = 2
    while divisor <= numero:
        if numero % divisor == 0:
            fatores.append(divisor)
            numero = numero // divisor
        else:
            divisor += 1
    return fatores


# comandos usados na vídeo para referência
if __name__ == '__main__':
    print(fatores_primos(630))  # [2, 3, 3, 5, 7]
    print(fatores_primos(13))  # [13]