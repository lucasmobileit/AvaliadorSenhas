# Gerador de senhas complexas.
import string
from random import choice

# Cores
RED    = '\033[31m'
GREEN  = '\033[32m'
YELLOW = '\033[33m'
WHITE  = '\033[0m'
BLUE   = '\033[34m'

# Variáveis de apoio
alfabeto = string.ascii_letters + string.digits + string.punctuation
senha    = ''

# Funções
def permanecer(resposta):
        if resposta == 'N':
            print(f"{GREEN}Obrigado por utilizar o gerador de senhas TechKey! :){WHITE}")
            return True
        else:
            return False

def conferindo_integer(numero):
    while True:
        try:
            if int(numero) < 8 or int(numero) > 16:
                print(f"{RED}O número deve estar entre 8 e 16.{WHITE}")
                return conferindo_integer(input("\nQuantos caracteres você deseja: "))
            return int(numero)
        except ValueError:
            valor = input("\nDigite um número válido...")

def complexidade(senha):
    tem_pontuacao = any(c in string.punctuation for c in senha)
    tem_digito = any(c in string.digits for c in senha)
    tem_letra = any(c in string.ascii_letters for c in senha)
    return tem_pontuacao and tem_digito and tem_letra

print(f"{GREEN}Seja muito bem-vindo ao gerador de senhas TechKey!{WHITE}")

while True:
    permanencia = input(f"""
Você deseja gerar uma nova senha?{GREEN}

[ENTER] para adicionar.{RED}
[N]     para não.{WHITE}

    """).upper()

    if permanecer(permanencia):
         break

    parametro = conferindo_integer(input(f"""
Quantos caracteres você deseja?{GREEN}
(O mínimo é 8 e o máximo 16)
{BLUE}
    [8]  Caracteres.
    [9]  Caracteres.
    [10] Caracteres.
    [11] Caracteres.
    [12] Caracteres.
    [13] Caracteres.
    [14] Caracteres.
    [15] Caracteres.
    [16] Caracteres.
{WHITE}
    """))

    print(parametro)
    while True:
        for i in range(parametro):
            senha += choice(alfabeto)

        if len(senha) > parametro:
            senha = ''

        if complexidade(senha):
            break

    print(f"\n{WHITE}Sua nova senha é: {YELLOW}{senha}{WHITE}.")
    senha = ''
