numero = int(input("Digite um número: "))

def numero_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def imprimir_primos_de_1_a_100():
    """Função que imprime todos os números primos de 1 a 100"""
    print("Números primos de 1 a 100:")
    primos = []
    
    for num in range(1, 101):
        if numero_primo(num):
            primos.append(num)
    
    # Imprime os números primos em formato organizado
    for i in range(0, len(primos), 10):  # 10 números por linha
        linha = primos[i:i+10]
        print(" ".join(f"{num:3d}" for num in linha))
    
    print(f"\nTotal de números primos encontrados: {len(primos)}")

# Chama a função para imprimir os primos de 1 a 100
imprimir_primos_de_1_a_100()

# Mantém o código original para testar um número específico
print("\n" + "="*50)
if numero_primo(numero):
    print("O número", numero, "é primo")
else:
    print("O número", numero, "não é primo")
