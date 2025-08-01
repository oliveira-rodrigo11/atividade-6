import random
import string

def gerar_senha(tamanho):
    if tamanho < 4:
        print("O tamanho da senha deve ser pelo menos 4 para incluir todos os tipos de caracteres.")
        return None

    # Conjuntos de caracteres
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = "!@#$%&*"

    # Garante pelo menos um de cada tipo
    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Completa o restante da senha com caracteres aleatórios de todos os grupos
    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos
    senha += random.choices(todos_caracteres, k=tamanho - 4)

    # Embaralha os caracteres para não ficar previsível
    random.shuffle(senha)

    # Junta a lista em uma string
    return ''.join(senha)

# Solicita o tamanho da senha ao usuário
try:
    tamanho = int(input("Digite o tamanho da senha desejada (ex: 8, 12, 16): "))
    senha_gerada = gerar_senha(tamanho)
    if senha_gerada:
        print("Senha gerada:", senha_gerada)
except ValueError:
    print("Por favor, digite um número inteiro válido.")
