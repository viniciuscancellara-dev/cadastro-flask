# Cadastro de Alunos - flask

Sistema de cadastro e gerenciamento de alunos desenvolvido com **Flask (Python), SQLite, HTML, CSS e JavaScript**.

O projeto foi desenvolvido como estudo prático de desenvolvimento web, trabalhando com **Flask, Jinja2, SQLite, validação no front-end e back-end, manipulação do DOM, formulários HTML, segurança de senhas e integração entre aplicação web e banco de dados**.

## Funcionalidades

### Login

- Página de login para acesso ao sistema
- Usuário e senha armazenados no banco de dados
- Senha armazenada utilizando **hash**
- Verificação da senha utilizando `check_password_hash`
- Validação dos campos no front-end utilizando JavaScript
- Mensagens de erro exibidas através de notificações Toast
- Validação das credenciais realizada no back-end

### Cadastro de alunos

Formulário com validação no front-end e no back-end:

- Nome — não pode ser vazio
- Idade — número entre 1 e 120
- E-mail — formato válido e único no banco
- Senha — mínimo de 8 caracteres, contendo:
  - Letra maiúscula
  - Letra minúscula
  - Número
  - Símbolo
- Observação — campo opcional
- Turno — seleção única via radio button
- Linguagens de interesse — múltipla escolha via checkbox
- Estado — seleção única via select

### Validação com JavaScript

- Validação dos campos antes do envio do formulário
- Utilização de eventos como `submit`, `input` e `change`
- Manipulação de elementos HTML através do DOM
- Utilização de `querySelector` e `querySelectorAll`
- Validação de campos obrigatórios
- Criação de mensagens de erro dinamicamente
- Utilização de `classList` para manipulação de classes CSS
- Utilização de `FormData` para trabalhar com dados de formulários
- Sistema de notificações Toast para exibição de mensagens

A validação feita no JavaScript é utilizada para melhorar a experiência do usuário, enquanto o Flask continua responsável pela validação dos dados no back-end.

### Segurança

- Senhas armazenadas utilizando **hash**
- Utilização de `generate_password_hash` e `check_password_hash` do **Werkzeug**
- Senhas não são armazenadas em texto puro no banco de dados
- Validação das senhas realizada no back-end
- Consultas SQL parametrizadas para prevenção de SQL Injection
- Verificação das credenciais realizada no servidor

### Banco de dados

- Persistência utilizando **SQLite3**
- Sem utilização de ORM
- Banco criado automaticamente na primeira execução
- Restrição de e-mail duplicado utilizando `UNIQUE`
- Tratamento de erros de integridade no Python
- Utilização de consultas SQL parametrizadas
- Operações de `SELECT`, `INSERT`, `UPDATE` e `DELETE`

### Visualização dos cadastros

- Página dedicada para visualizar os registros cadastrados
- Dados do SQLite são enviados pelo Flask para os templates
- Utilização de **Jinja2** para percorrer e exibir os registros
- Exibição dos alunos em tabela HTML
- Tabela estilizada utilizando CSS
- Interface com estética baseada em **Glassmorphism**

### Edição dos cadastros

- Seleção de um aluno para edição
- Formulário preenchido automaticamente com os dados existentes
- Alteração dos dados cadastrados
- Validação dos campos antes da atualização
- Atualização dos registros diretamente no SQLite

### Exclusão dos cadastros

- Opção para excluir todos os cadastros
- Exclusão protegida por uma senha de confirmação
- Senha armazenada em uma tabela de configuração no SQLite
- Senha armazenada utilizando hash
- Verificação da senha realizada no back-end com `check_password_hash`
- A exclusão utiliza `DELETE FROM usuarios` somente após a validação

## Tecnologias

- **Python 3**
- **Flask**
- **Werkzeug** — utilizado para hash e verificação de senhas
- **SQLite3** — módulo nativo do Python
- **Jinja2** — sistema de templates utilizado pelo Flask
- **HTML5**
- **CSS3**
- **JavaScript**

A interface utiliza **Glassmorphism** como principal referência visual.

Não são utilizados frameworks de CSS, JavaScript ou ORM.

## Estrutura do projeto

```text
meu_projeto/
│
├── app.py
│
├── instance/
│   └── banco.db
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   ├── index.html
│   ├── inicio.html
│   ├── banco.html
│   └── excluir-banco-validacao.html
│
├── requirements.txt
│
└── README.md

Como rodar o projeto
1. Clone o repositório
git clone https://github.com/viniciuscancellara-dev/cadastro-flask

cd cadastro-flask

2. Instale as dependências
pip install -r requirements.txt

3. Rode a aplicação
python app.py

4. Acesse no navegador
http://127.0.0.1:5000

 ## Desenvolvido por ** Vinicius Cancellara **
