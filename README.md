# Avaliador de Força de Senha 🔐

Bem-vindo ao **Avaliador de Força de Senha**, uma ferramenta Python robusta e simples para avaliar e gerar senhas seguras! Seja para verificar a força da sua senha atual ou criar uma nova com segurança criptográfica, esta ferramenta é perfeita para você! 🚀

## Funcionalidades 🌟

- **Análise de Força de Senha**:
  - Avalia senhas com base em critérios de segurança essenciais:
    - Presença de números, letras maiúsculas, minúsculas e caracteres especiais.
    - Verifica a ausência de palavras comuns e fracas (ex.: "senha", "123456").
    - Recomenda um tamanho mínimo de 12 caracteres para maior segurança.
  - Fornece dicas claras e práticas para melhorar senhas fracas.
- **Geração de Senhas Seguras**:
  - Cria senhas aleatórias usando o módulo `secrets` do Python para máxima segurança.
  - Garante pelo menos uma letra maiúscula, minúscula, número e caractere especial.
- **Interface de Linha de Comando**:
  - CLI intuitiva com `argparse` para avaliar ou gerar senhas com facilidade.
  - Inclui tratamento de erros para entradas inválidas.
- **Leve e Sem Dependências**:
  - Usa apenas bibliotecas padrão do Python (`string`, `argparse`, `secrets`).

## Instalação ⚙️

1. **Clone o Repositório**:

   ```bash
   git clone https://github.com/lucasmobileit/AvaliadorSenhas.git
   cd AvaliadorSenhas
   ```

2. **Requisitos**:

   - Python 3.6 ou superior.
   - Sem dependências externas! 🎉

3. **Salve e Execute**:

   - Salve o código como `avaliador_senha.py`.
   - Execute-o no terminal com o Python.

## Como Usar 📋

Use os seguintes comandos para interagir com a ferramenta:

### Verificar uma Senha

Avalie a força de uma senha:

```bash
python avaliador_senha.py --senha "MinhaSenha123!"
```

**Exemplo de Saída**:

```
[!] Senhas com menos de 12 caracteres não são consideradas tão seguras.

➡ O nível da sua senha é: Boa! 🙂
```

### Gerar uma Senha

Crie uma senha segura com o tamanho desejado:

```bash
python avaliador_senha.py --gerar 14
```

**Exemplo de Saída**:

```
[!] Sua senha foi gerada: X9#mP2k@L5nQwR
Nenhuma sugestão necessária.

➡ O nível da sua senha é: Excelente! 😃
```

### Exemplo de Erro

Tente gerar uma senha com tamanho inválido:

```bash
python avaliador_senha.py --gerar 6
```

**Exemplo de Saída**:

```
[X] Erro ao gerar senha: A senha precisa ter pelo menos 8 caracteres.
```

### Ajuda

Veja as opções disponíveis:

```bash
python avaliador_senha.py --help
```

**Exemplo de Saída**:

```
usage: avaliador_senha.py [-h] [--senha SENHA] [--gerar GERAR]

Verifica a força de uma senha.

optional arguments:
  -h, --help       show this help message and exit
  --senha SENHA    Senha a ser avaliada.
  --gerar GERAR    Gera uma senha segura com o tamanho indicado.
```

## Como Funciona 🛠️

- **Avaliação de Força (**`complexity_pass`**)**:

  - Pontua as senhas com base em:
    - Números: +1 ponto.
    - Letras maiúsculas e minúsculas: +1 ponto.
    - Caracteres especiais: +1 ponto.
    - Ausência de palavras comuns: +1 ponto.
    - Tamanho ≥ 12 caracteres: +1 ponto (ou -2 se menor).
  - Classifica as senhas como:
    - **Excelente! 😃** (5 pontos).
    - **Boa! 🙂** (3–4 pontos).
    - **Precisa melhorar! 😟** (&lt;3 pontos).
  - Oferece sugestões detalhadas para melhorias.

- **Geração de Senha (**`random_pass`**)**:

  - Garante uma combinação de tipos de caracteres para maior segurança.
  - Usa o módulo `secrets` para aleatoriedade criptograficamente segura.
  - Embaralha a senha final para evitar padrões previsíveis.

- **Tratamento de Erros**:

  - Lida elegantemente com entradas inválidas (ex.: senhas com menos de 8 caracteres).
  - Exibe mensagens de erro claras e úteis.
