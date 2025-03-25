# Gerador de Senhas Complexas

## Descrição
O **Gerador de Senhas Complexas** é um script em Python que permite aos usuários gerar senhas seguras e aleatórias. O script garante que as senhas geradas atendam a critérios de complexidade, incluindo a presença de letras, números e caracteres especiais.

## Pré-requisitos
- Python 3.x instalado em seu sistema.

## Instalação
1. **Clone o repositório** ou **baixe o script** para o seu sistema.
2. Certifique-se de que o Python está instalado. Você pode verificar isso executando:
   ```bash
   python --version
   ```

## Uso
Para executar o script, utilize o seguinte comando:
```bash
python gerador_senhas.py
```

### Funcionalidades
- O script solicita que o usuário informe a quantidade de caracteres desejada para a senha, que deve estar entre 8 e 16.
- O usuário pode optar por gerar uma nova senha ou encerrar o programa.
- As senhas geradas incluem letras maiúsculas, minúsculas, números e caracteres especiais, garantindo uma boa complexidade.

### Como Funciona
1. **Entrada do Usuário**: O script pergunta se o usuário deseja gerar uma nova senha.
2. **Validação da Entrada**: O usuário deve fornecer um número de caracteres entre 8 e 16. O script valida a entrada e solicita novamente caso o valor esteja fora do intervalo ou seja inválido.
3. **Geração da Senha**: O script gera uma senha aleatória com a quantidade de caracteres especificada e verifica se a senha atende aos critérios de complexidade.
4. **Exibição da Senha**: Após a geração, a senha é exibida ao usuário.

## Cores
O script utiliza cores para melhorar a experiência do usuário:
- **Vermelho**: Para mensagens de erro.
- **Verde**: Para mensagens de sucesso e boas-vindas.
- **Amarelo**: Para exibir a senha gerada.
- **Branco**: Para mensagens padrão.
- **Azul**: Para destacar opções.

## Exemplo de Execução
```plaintext
Seja muito bem-vindo ao gerador de senhas TechKey!

Você deseja gerar uma nova senha?
[ENTER] para adicionar.
[N] para não.

Quantos caracteres você deseja?
(O mínimo é 8 e o máximo 16)
[8]  Caracteres.
[9]  Caracteres.
[10] Caracteres.
[11] Caracteres.
[12] Caracteres.
[13] Caracteres.
[14] Caracteres.
[15] Caracteres.
[16] Caracteres.

Sua nova senha é: Abc@1234!.
```
