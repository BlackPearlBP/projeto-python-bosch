def verificar_inteiro(texto):
    while True:
        try:
            return int(input(texto))
        except Exception:
            print("\033[31;1mERROR! Digite um valor válido\033[m")
        else:
            break

def verificar_float(texto):
    while True:
        try:
            return float(input(texto))
        except Exception:
            print("\033[31;1mERROR! Digite um valor válido\033[m")
        else:
            break