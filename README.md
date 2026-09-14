# 📚 Sistema de Cadastro de Alunos

Sistema web de cadastro e gerenciamento de alunos desenvolvido com **Flask, Python, SQLite, HTML, CSS e JavaScript**.

O projeto foi desenvolvido como prática de desenvolvimento web, reunindo conceitos de **back-end, banco de dados, autenticação, validação de formulários, sessões, CRUD e manipulação do DOM**.

---

## ✨ Funcionalidades

### 🔐 Sistema de login

* Login com usuário e senha.
* Senha armazenada no banco utilizando **hash**.
* Autenticação através de `session` do Flask.
* Proteção das rotas utilizando um **decorator de autenticação**.
* Logout.
* Credenciais iniciais configuradas através de variáveis de ambiente.

### 📝 Cadastro de alunos

* Cadastro de nome.
* Cadastro de idade.
* Cadastro de e-mail.
* Cadastro de senha.
* Campo de observação.
* Seleção de linguagens.
* Seleção de turno.
* Seleção de estado.
* Validação dos dados antes do cadastro.

### 🗄️ Banco de dados

* Utilização do **SQLite**.
* Armazenamento dos alunos de forma persistente.
* Implementação completa das operações **CRUD**:

  * **Create** — criação de registros.
  * **Read** — consulta e visualização de registros.
  * **Update** — atualização de registros.
  * **Delete** — exclusão de registros.
* Tratamento de erros de integridade, como e-mails duplicados.
* Utilização de consultas SQL parametrizadas.

### ✏️ Gerenciamento de alunos

* Visualização dos alunos cadastrados.
* Edição de registros.
* Exclusão individual de usuários.
* Seleção do usuário que será excluído através de um `select`.
* Confirmação da exclusão através de senha.
* Autorização temporária para exclusão utilizando `session`.
* Remoção da autorização após a exclusão do usuário.

### 🎨 Interface

* Interface desenvolvida com HTML e CSS puro.
* Layout responsivo.
* Estilização com efeito **Glassmorphism**.
* Animações e efeitos de `hover` e `focus`.
* Tela de login personalizada.
* Botão para mostrar/ocultar senha.
* Sistema de mensagens utilizando **Toast**.
* Animações de aparecimento e desaparecimento das mensagens.
* Alteração dinâmica da interface através de JavaScript.

### ⚙️ JavaScript

* Manipulação do DOM.
* Eventos de formulário.
* Validação de campos.
* Alteração dinâmica de elementos.
* Manipulação de classes CSS.
* Sistema de Toast.
* Mostrar e ocultar senha.
* Utilização de `FormData`.
* Manipulação de `input`, `change`, `click` e `submit`.
* Feedback visual durante o preenchimento e envio dos formulários.
* Controle da exibição dos painéis de validação, edição e exclusão.

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **Flask**
* **SQLite**
* **HTML5**
* **CSS3**
* **JavaScript**
* **Jinja2**
* **Werkzeug**
* **python-dotenv**
* **Git / GitHub**

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
```

O arquivo `.env` é utilizado localmente para armazenar informações sensíveis e **não deve ser enviado para o GitHub**.

---

## 🔐 Segurança

O projeto possui algumas medidas básicas de segurança:

* Senhas armazenadas utilizando hash através do **Werkzeug**.
* Utilização de `check_password_hash()` para verificar senhas.
* Autenticação baseada em sessão.
* Proteção das rotas através de decorator.
* Credenciais configuradas através de variáveis de ambiente.
* `.env` incluído no `.gitignore`.
* Consultas SQL utilizando parâmetros para evitar a inserção direta de valores na query.
* Confirmação por senha antes da exclusão de usuários.
* Autorização temporária para exclusão armazenada na sessão.
* Remoção da autorização após a operação de exclusão.

### Variáveis de ambiente

As informações sensíveis são armazenadas em um arquivo `.env`:

```env
SECRET_KEY=sua_secret_key

LOGIN_USER=seu_usuario

LOGIN_PASSWORD=sua_senha

DELETE_PASSWORD=sua_senha_de_confirmacao
```

O arquivo `.env` **não deve ser enviado para o repositório**.

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/viniciuscancellara-dev/cadastro-flask.git
```

### 2. Entre na pasta do projeto

```bash
cd cadastro-flask
```

### 3. Crie um ambiente virtual

Windows:

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Configure o `.env`

Crie um arquivo `.env` na pasta do projeto e adicione as variáveis necessárias:

```env
SECRET_KEY=sua_secret_key

LOGIN_USER=seu_usuario

LOGIN_PASSWORD=sua_senha

DELETE_PASSWORD=sua_senha_de_confirmacao
```

### 7. Execute o Flask

```bash
python app.py
```

Depois, acesse no navegador:

```text
http://127.0.0.1:5000
```

---

## 🧠 Conceitos praticados

Durante o desenvolvimento deste projeto foram praticados diversos conceitos de desenvolvimento web.

### Python

* Variáveis
* Condicionais
* Loops
* Funções
* Tratamento de exceções
* Manipulação de strings
* Expressões regulares
* Programação orientada a objetos
* Organização de código

### Flask

* Rotas
* GET e POST
* `request.form`
* `redirect`
* `render_template`
* Jinja2
* Sessões
* Autenticação
* Decorators

### SQLite / SQL

* Criação de tabelas
* `INSERT`
* `SELECT`
* `UPDATE`
* `DELETE`
* `WHERE`
* `ORDER BY`
* `JOIN`
* Chaves primárias
* Restrições de integridade
* Consultas parametrizadas
* Utilização do SQLite através do `sqlite3`

### HTML

* Estrutura de páginas
* Formulários
* Inputs
* Labels
* Selects
* Checkboxes
* Radio buttons
* Atributos `name`, `id`, `class` e `data-*`

### CSS

* Flexbox
* Responsividade
* Seletores
* Pseudo-classes
* Animações
* Transições
* Layouts
* Glassmorphism

### JavaScript

* DOM
* `getElementById`
* `querySelector`
* `querySelectorAll`
* Eventos
* `addEventListener`
* `classList`
* `FormData`
* Validação de formulários
* Manipulação de elementos HTML
* Eventos `click`, `change` e `submit`
* Controle de interfaces através do DOM

---

## 🎯 Objetivo do projeto

O objetivo principal deste projeto foi colocar em prática conceitos de desenvolvimento web full-stack, conectando uma interface feita com HTML, CSS e JavaScript a um back-end desenvolvido em Python com Flask e um banco de dados SQLite.

O projeto também serviu como prática para compreender o fluxo:

```text
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
```

Além disso, o projeto permitiu compreender na prática o funcionamento de um sistema **CRUD completo**, desde a criação até a exclusão de registros.

---

## 🔮 Possíveis melhorias futuras

Algumas funcionalidades e melhorias que podem ser adicionadas futuramente:

* Sistema de usuários com diferentes níveis de permissão.
* Paginação dos registros.
* Pesquisa e filtros de alunos.
* Separação do projeto em diferentes módulos Python.
* Melhorias na API e comunicação assíncrona.
* Substituição gradual do envio tradicional de formulários HTML por **Fetch API**.
* Utilização de `async/await` para requisições assíncronas com JavaScript.
* Atualização de partes da página sem necessidade de recarregar completamente o navegador.
* Melhor tratamento das respostas do Flask no JavaScript.
* Testes automatizados.
* Melhorias adicionais de segurança.
* Proteção contra CSRF.
* Melhor organização e reutilização do código JavaScript.
* Deploy em um servidor.

### 📡 Futuras melhorias na comunicação Front-end / Back-end

Uma evolução planejada do projeto é substituir alguns envios tradicionais de formulários:

```text
HTML Form
   ↓
POST
   ↓
Flask
   ↓
Nova página
```

por uma comunicação assíncrona utilizando **Fetch API** e `async/await`:

```text
JavaScript
   ↓
fetch()
   ↓
Flask
   ↓
Resposta
   ↓
JavaScript
   ↓
Atualização do DOM
```

Isso permitirá realizar operações como cadastro, edição e exclusão sem necessariamente recarregar a página inteira, tornando a interface mais dinâmica.

---

## 👤 Autor

Desenvolvido por **Vinicius Cancellara** como projeto de estudo e prática de desenvolvimento web.

## 🔗 GitHub

github.com/viniciuscancellara-dev/cadastro-flask

---

## 📌 Status

**Concluído ✅**

Projeto desenvolvido para fins de estudo e prática de desenvolvimento web com **Python, Flask, SQLite, HTML, CSS e JavaScript**.

O projeto atualmente possui um **CRUD completo**, sistema de login, autenticação por sessão, validações, gerenciamento de alunos, edição e exclusão individual de registros com confirmação por senha.
