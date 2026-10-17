# Sistema de Cadastro de Alunos

Aplicação web para cadastro e gerenciamento de alunos, desenvolvida com **Python, Flask, SQLite, HTML, CSS e JavaScript**. O projeto reúne autenticação, validação de dados, operações CRUD e uma interface interativa.

**Acesse a aplicação:** [cadastro-flask.onrender.com](https://cadastro-flask.onrender.com)

## Funcionalidades

- **Autenticação:** criação de usuário, login, logout e proteção de páginas por sessão.
- **Cadastro de alunos:** nome, idade, e-mail, senha, observação, linguagens, turno e estado.
- **Validação de dados:** verificações no back-end, incluindo formato dos campos, limites de idade e e-mail duplicado.
- **Gerenciamento de registros:** listagem, edição e exclusão individual de alunos.
- **Confirmação para exclusão:** validação por senha antes de permitir a exclusão.
- **Interface interativa:** mensagens Toast, exibição/ocultação de senha, feedback dos formulários e atualizações com JavaScript.
- **Persistência:** armazenamento dos registros em banco de dados SQLite.

## Tecnologias

| Tecnologia | Utilização |
| --- | --- |
| Python | Lógica da aplicação e validações |
| Flask | Rotas, requisições e renderização das páginas |
| SQLite | Armazenamento dos dados |
| HTML5 e Jinja2 | Estrutura das páginas e templates |
| CSS3 | Layout, responsividade, animações e glassmorphism |
| JavaScript | Eventos, DOM, `FormData`, `fetch()` e mensagens Toast |
| Werkzeug | Hash e verificação de senhas |
| python-dotenv | Carregamento de variáveis de ambiente |
| Gunicorn | Servidor WSGI para execução em produção |

## Estrutura do projeto

```text
ProjetoFLASK/
├── .gitignore
├── README.md
└── meu_projeto/
    ├── app.py
    ├── requirements.txt
    ├── .env                 # arquivo local
    ├── instance/
    │   └── banco.db
    ├── static/
    │   ├── script.js
    │   ├── style.css
    │   └── png/
    │       ├── favicon.png
    │       ├── hidepassword.png
    │       └── showpassword.png
    └── templates/
        ├── 404.html
        ├── banco.html
        ├── excluir-banco-validacao.html
        ├── index.html
        ├── inicio.html
        ├── login.html
        └── sign.html
```

## Executar localmente

### 1. Pré-requisitos

- Python instalado.
- Git, caso queira clonar o repositório.

### 2. Clonar o repositório

```bash
git clone https://github.com/viniciuscancellara-dev/cadastro-flask.git
cd cadastro-flask
```

> Os comandos seguintes consideram que `app.py` e `requirements.txt` estão dentro da pasta `meu_projeto`.

### 3. Criar e ativar o ambiente virtual

Na raiz do repositório:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

No macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instalar as dependências

```bash
pip install -r meu_projeto/requirements.txt
```

### 5. Configurar as variáveis de ambiente

Crie um arquivo `meu_projeto/.env`:

```env
SECRET_KEY=gere_uma_chave_secreta
DELETE_HASH=defina_uma_senha_de_confirmacao
DEBUG_MODE=True
```

- `SECRET_KEY`: chave usada para assinar a sessão do Flask.
- `DELETE_HASH`: valor inicial usado para criar a senha de confirmação de exclusão no banco, quando a configuração ainda não existe.
- `DEBUG_MODE`: ativa o modo de depuração local quando definido como `True`. Em produção, mantenha-o desativado.

Não publique o `.env` nem coloque credenciais reais no repositório. Use valores próprios no seu ambiente.

### 6. Iniciar a aplicação

A aplicação carrega o `.env` a partir do diretório de execução. Entre na pasta do projeto antes de iniciar:

```powershell
cd meu_projeto
python app.py
```

Acesse [http://127.0.0.1:5000](http://127.0.0.1:5000).

Na tela de cadastro de usuário, crie uma conta para entrar na aplicação.

## Segurança implementada

- Hash de senhas com as funções do Werkzeug.
- Verificação de senha por hash, sem comparar senhas em texto puro.
- Rotas protegidas por autenticação de sessão.
- Consultas SQL parametrizadas.
- Validação de dados no servidor.
- Restrição de e-mail duplicado no banco.
- Confirmação por senha antes da exclusão de registros.
- Configurações sensíveis lidas por variáveis de ambiente.

Essas medidas representam proteções básicas para um projeto de estudo; não constituem, por si só, uma auditoria de segurança ou garantia de segurança para uso em produção.

## Autor

**Vinicius Cancellara**

- [GitHub](https://github.com/viniciuscancellara-dev)
- [Projeto em execução](https://cadastro-flask.onrender.com)
