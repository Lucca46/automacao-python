# Automacao de Cadastro de Produtos (Estudo)

Projeto estudantil em Python para automacao de cadastro de produtos com `pyautogui` e `pandas`.

## Requisitos
- Python 3.10+
- Navegador instalado (Edge ou Chrome)

## Instalacao
```bash
pip install -r requirements.txt
```

## Configuracao de credenciais
Use variaveis de ambiente para nao deixar senha no codigo.

PowerShell:
```powershell
$env:LOGIN_EMAIL="seu_email@exemplo.com"
$env:LOGIN_SENHA="sua_senha"
```

## Executar
```bash
python codigo.py
```

## Arquivos do projeto
- `codigo.py`: script principal
- `gabarito.py`: versao de referencia
- `pegar_posicao.py`: utilitario para capturar posicao do mouse
- `produtos.csv`: base de dados para cadastro

## Observacoes
- Coordenadas de clique (`x`, `y`) dependem da resolucao/tela. Ajuste com `pegar_posicao.py`.
- Nunca suba senhas/tokens para o GitHub.
