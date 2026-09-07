# 📚 Sistema de Cadastro de Alunos

Sistema web de cadastro e gerenciamento de alunos desenvolvido com **Flask, Python, SQLite, HTML, CSS e JavaScript**.

O projeto foi desenvolvido como prática de desenvolvimento web, reunindo conceitos de **back-end, banco de dados, autenticação, validação de formulários, sessões, CRUD e manipulação do DOM**.

---

## ✨ Funcionalidades

### 🔐 Sistema de login
- Login com usuário e senha.
- Senha armazenada no banco utilizando **hash**.
- Autenticação através de `session` do Flask.
- Proteção das rotas utilizando um **decorator de autenticação**.
- Logout.
- Credenciais iniciais configuradas através de variáveis de ambiente.

### 📝 Cadastro de alunos
- Cadastro de nome.
- Cadastro de idade.
- Cadastro de e-mail.
- Cadastro de senha.
- Campo de observação.
- Seleção de linguagens.
- Seleção de turno.
- Seleção de estado.
- Validação dos dados antes do cadastro.

### 🗄️ Banco de dados
- Utilização do **SQLite**.
- Armazenamento dos alunos de forma persistente.
- Operações de criação, consulta, atualização e exclusão de registros.
- Tratamento de erros de integridade, como e-mails duplicados.

### ✏️ Gerenciamento de alunos
- Visualização dos alunos cadastrados.
- Edição de registros.
- Exclusão de registros.
- Exclusão dos registros do banco mediante confirmação por senha.

### 🎨 Interface
- Interface desenvolvida com HTML e CSS puro.
- Layout responsivo.
- Estilização com efeito **Glassmorphism**.
- Animações e efeitos de `hover` e `focus`.
- Tela de login personalizada.
- Botão para mostrar/ocultar senha.
- Sistema de mensagens utilizando **Toast**.
- Animações de aparecimento e desaparecimento das mensagens.

### ⚙️ JavaScript
- Manipulação do DOM.
- Eventos de formulário.
- Validação de campos.
- Alteração dinâmica de elementos.
- Manipulação de classes CSS.
- Sistema de Toast.
- Mostrar e ocultar senha.
- Feedback visual durante o envio do formulário.

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **Flask**
- **SQLite**
- **HTML5**
- **CSS3**
- **JavaScript**
- **Jinja2**
- **Werkzeug**
- **python-dotenv**
- **Git / GitHub**

O projeto não utiliza frameworks de front-end, ORM ou bibliotecas CSS/JS externas.

---

## 📁 Estrutura do projeto

```text
ProjetoFLASK/
│
├── .gitignore
├── README.md
│
└── meu_projeto/
    │
    ├── app.py
    ├── requirements.txt
    │
    ├── instance/
    │   └── banco.db
    │
    ├── static/
    │   ├── script.js
    │   ├── style.css
    │   │
    │   └── png/
    │       ├── hidepassword.png
    │       └── showpassword.png
    │
    └── templates/
        ├── login.html
        ├── inicio.html
        ├── index.html
        ├── banco.html
        └── excluir-banco-validacao.html

O arquivo .env é utilizado localmente para armazenar informações sensíveis e não deve ser enviado para o GitHub.

🔐 Segurança

O projeto possui algumas medidas básicas de segurança:

Senhas armazenadas utilizando hash através do Werkzeug.
Utilização de check_password_hash() para verificar senhas.
Autenticação baseada em sessão.
Proteção das rotas através de decorator.
Credenciais configuradas através de variáveis de ambiente.
.env incluído no .gitignore.
Consultas SQL utilizando parâmetros para evitar a inserção direta de valores na query.
Variáveis de ambiente

As informações sensíveis são armazenadas em um arquivo .env:

SECRET_KEY=sua_secret_key
LOGIN_USER=seu_usuario
LOGIN_PASSWORD=sua_senha
DELETE_PASSWORD=sua_senha_de_confirmacao

O arquivo .env não deve ser enviado para o repositório.

🚀 Como executar o projeto
1. Clone o repositório
git clone https://github.com/viniciuscancellara-dev/cadastro-flask.git
2. Entre na pasta do projeto
cd cadastro-flask
3. Crie um ambiente virtual

Windows:

python -m venv venv
4. Ative o ambiente virtual

PowerShell:

.\venv\Scripts\Activate.ps1
5. Instale as dependências
pip install -r requirements.txt
6. Configure o .env

Crie um arquivo .env na pasta do projeto e adicione as variáveis necessárias:

SECRET_KEY=sua_secret_key
LOGIN_USER=seu_usuario
LOGIN_PASSWORD=sua_senha
DELETE_PASSWORD=sua_senha_de_confirmacao
7. Execute o Flask
python app.py

Depois, acesse no navegador:

http://127.0.0.1:5000
🧠 Conceitos praticados

Durante o desenvolvimento deste projeto foram praticados diversos conceitos de desenvolvimento web:

Python
Variáveis
Condicionais
Loops
Funções
Tratamento de exceções
Manipulação de strings
Expressões regulares
Programação orientada a objetos
Organização de código
Flask
Rotas
GET e POST
request.form
redirect
render_template
Jinja2
Sessões
Autenticação
Decorators
SQLite / SQL
Criação de tabelas
INSERT
SELECT
UPDATE
DELETE
WHERE
ORDER BY
JOIN
Chaves primárias
Restrições de integridade
Utilização do SQLite através do sqlite3
HTML
Estrutura de páginas
Formulários
Inputs
Labels
Selects
Checkboxes
Radio buttons
Atributos name, id, class e data-*
CSS
Flexbox
Responsividade
Seletores
Pseudo-classes
Animações
Transições
Layouts
Glassmorphism
JavaScript
DOM
getElementById
querySelector
querySelectorAll
Eventos
addEventListener
classList
FormData
Validação de formulários
Manipulação de elementos HTML
🎯 Objetivo do projeto

O objetivo principal deste projeto foi colocar em prática conceitos de desenvolvimento web full-stack, conectando uma interface feita com HTML, CSS e JavaScript a um back-end desenvolvido em Python com Flask e um banco de dados SQLite.

O projeto também serviu como prática para compreender o fluxo:

Usuário
   ↓
HTML / CSS / JavaScript
   ↓
Flask
   ↓
Validação
   ↓
SQLite
   ↓
Resposta para o usuário
🔮 Possíveis melhorias futuras

Algumas funcionalidades que podem ser adicionadas futuramente:

Sistema de usuários com diferentes níveis de permissão.
Paginação dos registros.
Pesquisa e filtros de alunos.
Separação do projeto em diferentes módulos Python.
Melhorias na API e comunicação assíncrona.
Testes automatizados.
Melhorias adicionais de segurança.
Deploy em um servidor.
👤 Autor

Desenvolvido por Vinicius Cancellara como projeto de estudo e prática de desenvolvimento web.

🔗 GitHub

github.com/viniciuscancellara-dev/cadastro-flask

📌 Status

Concluído ✅

Projeto desenvolvido para fins de estudo e prática de desenvolvimento web com Python, Flask, SQLite, HTML, CSS e JavaScript.