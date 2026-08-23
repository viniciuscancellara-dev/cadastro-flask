# Cadastro de Alunos — Flask + SQLite

Sistema simples de cadastro de alunos desenvolvido com **Flask (Python), HTML e CSS puro**, sem JavaScript e sem ORM.

O projeto foi desenvolvido como estudo prático de desenvolvimento web com Python, trabalhando com **Flask, Jinja2, SQLite, validação no back-end, formulários HTML e integração entre front-end e banco de dados**.

## Funcionalidades

### Cadastro de alunos

Formulário HTML com validação completa no back-end:

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

### Banco de dados

- Persistência utilizando **SQLite3**
- Sem utilização de ORM
- Banco criado automaticamente na primeira execução
- Restrição de e-mail duplicado utilizando `UNIQUE`
- Tratamento de erros de integridade no Python
- Utilização de consultas SQL parametrizadas

### Visualização dos cadastros

- Página dedicada para visualizar os registros cadastrados
- Dados do SQLite são enviados pelo Flask para o template
- Utilização de **Jinja2** para percorrer e exibir os registros em uma tabela HTML
- Tabela estilizada utilizando CSS

### Exclusão dos cadastros

- Opção para excluir todos os cadastros
- Exclusão protegida por uma senha de confirmação
- Senha armazenada em uma tabela de configuração no SQLite
- Verificação da senha realizada no back-end antes da exclusão
- A exclusão utiliza `DELETE FROM usuarios` somente após a validação

## Tecnologias

- **Python 3**
- **Flask**
- **SQLite3** — módulo nativo do Python
- **Jinja2** — sistema de templates utilizado pelo Flask
- **HTML5**
- **CSS3**

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
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── inicio.html
│   ├── banco.html
│   └── excluir-banco-validacao.html
│
└── README.md

##  Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/viniciuscancellara-dev/cadastro-flask
   cd meu_projeto
   ```

2. Instale o Flask (requirements.txt):
   ```bash
   pip install flask
   ```

3. Rode a aplicação:
   ```bash
   python app.py
   ```

4. Acesse no navegador:
   ```
   http://127.0.0.1:5000 
   ```
   
##  Licença

Projeto de estudo, livre para uso e modificação.

## Desenvolvimento

Projeto desenvolvido por **Vinicius Cancellara**.