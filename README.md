# Automacao de Cadastro de Produtos com Python

Projeto pratico desenvolvido para automatizar o cadastro de produtos em um formulario web, simulando uma rotina administrativa comum em empresas. A solucao usa `Python`, `pyautogui` e `pandas` para ler uma base `.csv`, acessar o sistema, preencher os campos automaticamente e repetir o processo para varios itens.

## Por que este projeto e relevante

Este projeto mostra competencias valorizadas em vagas de estagio, como:

- automacao de tarefas repetitivas com Python
- manipulacao de dados tabulares com `pandas`
- integracao entre script e aplicacao web
- organizacao de credenciais com variaveis de ambiente
- atencao a detalhes operacionais, como tempo de carregamento e coordenadas de interface

## Demonstracao do fluxo

O script executa o seguinte processo:

1. abre o navegador
2. acessa a pagina de login
3. realiza autenticacao com credenciais configuradas no ambiente
4. le os produtos do arquivo `produtos.csv`
5. preenche o formulario item por item
6. envia os registros automaticamente

## Tecnologias utilizadas

- Python
- PyAutoGUI
- Pandas
- CSV
- Variaveis de ambiente

## Estrutura do projeto

- `codigo.py`: automacao principal do login e cadastro dos produtos
- `produtos.csv`: base de dados usada no preenchimento automatico
- `auxiliar.py`: apoio para identificar posicoes do mouse na tela
- `pegar_posicao.py`: alternativa para ajuste de coordenadas
- `requirements.txt`: dependencias do projeto

## Como executar

### 1. Instale as dependencias

```bash
pip install -r requirements.txt
```

### 2. Configure as credenciais

PowerShell:

```powershell
$env:LOGIN_EMAIL="seu_email@exemplo.com"
$env:LOGIN_SENHA="sua_senha"
```

### 3. Rode o projeto

```bash
python codigo.py
```

## Diferenciais tecnicos

- Leitura automatizada de dados a partir de arquivo externo
- Repeticao estruturada de cadastro para multiplos produtos
- Separacao basica entre configuracao sensivel e codigo
- Adaptacao a contexto real de automacao desktop, onde resolucao e posicionamento influenciam a execucao

## Pontos de atencao

- O projeto foi desenvolvido para estudo e pratica de automacao.
- Como usa coordenadas de tela, pode exigir ajuste conforme resolucao, zoom e navegador.
- Antes de executar, valide as posicoes com `auxiliar.py` ou `pegar_posicao.py`.
- Nao publique senhas nem arquivos de configuracao com dados sensiveis.

## Objetivo academico

Alem de praticar programacao em Python, este projeto foi criado para demonstrar como uma tarefa operacional manual pode ser transformada em um processo automatizado, reduzindo retrabalho e aumentando produtividade.
