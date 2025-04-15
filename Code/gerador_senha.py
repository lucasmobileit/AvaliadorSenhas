import string
import argparse
import secrets

class Complexity:
    def complexity_pass(self, password):            
            pontos = 0
            dicas = []
                                
            if any(p in string.digits for p in password):
                pontos += 1
            else:
                dicas.append("[!] Inclua ao menos um número nesta senha.")
            
            if any(p.islower() for p in password) and any(p.isupper() for p in password):
                pontos += 1
            else:
                dicas.append("[!] Faça combinação de minusculas e maiusculas.")

            if any(p in string.punctuation for p in password):
                pontos += 1
            else:
                dicas.append("[!] Adicione caracteres especiais, como !, @, #, etc.")

            # Verificação de palavras comuns
            comuns = ["senha", "password", "admin", "123456", "qwerty"]
            if not any(palavra in password.lower() for palavra in comuns):
                pontos += 1
            else:
                dicas.append("Evite palavras óbvias como 'senha' ou '123456'.")
            
            if len(password) >= 12:
                pontos += 1
            else:
                dicas.append("[!] Senhas com menos de 12 caracteres não são consideradas tão seguras.")
                pontos -= 2
            
            if pontos == 5:
                maturidade = "Excelente! 😃"
            elif pontos >= 3:
                maturidade = "Boa! 🙂"
            else:
                maturidade = "Precisa melhorar! 😟"
            
            nivel = "\n".join(dicas)
            return f"{nivel}\n\n➡ O nível da sua senha é: {maturidade}"
    
    
    def random_pass(self, length):
        if length < 8:
            raise ValueError("A senha precisa ter pelo menos 8 caracteres.")
    
        # Conjunto de caracteres
        chars = string.ascii_letters + string.digits + string.punctuation
    
        # Garante pelo menos um de cada tipo
        senha = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
        ]   
    
        # Preenche o restante
        for _ in range(length - 4):
            senha.append(secrets.choice(chars))
        
        secrets.SystemRandom().shuffle(senha)  # Embaralha com segurança
        return ''.join(senha)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verifica a força de uma senha.")
    parser.add_argument("--senha", type=str, help="Senha a ser avaliada.")
    parser.add_argument("--gerar", type=int, help="Gera uma senha segura com o tamanho indicado.")

    args = parser.parse_args()
    checker = Complexity()

    if args.gerar is not None:
        try:
            senha_aleatoria = Complexity().random_pass(args.gerar)
            print(f"[!] Sua senha foi gerada: {senha_aleatoria}")
            print(checker.complexity_pass(senha_aleatoria))
        except ValueError as erro:
            print(f"[X] Erro ao gerar senha: {erro}")
    elif args.senha:
        try:
            print(checker.complexity_pass(args.senha))
        except ValueError as erro:
             print(f"[X] Erro ao gerar senha: {erro}")
    else:
        print("Use '--senha' para avaliar ou '--gerar' para gerar uma senha.")
