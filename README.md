# Mang Stu

Aplicação web para cadastro e gerenciamento de alunos, feita com **Python, Flask, SQLite, HTML, CSS e JavaScript**. É um projeto de estudo que cresceu junto com o meu aprendizado: começou simples e foi ganhando login, validações, proteção contra abusos e uma interface mais cuidada.

**Online:** [cadastro-flask.onrender.com](https://cadastro-flask.onrender.com)

## Funcionalidades

- **Landing page** de apresentação, com navegação que muda conforme o usuário está logado ou não.
- **Autenticação:** criação de conta, login, logout, rotas protegidas e sessão persistente (cookie permanente com renovação automática).
- **Cadastro de alunos:** nome, idade, e-mail, senha, observação, linguagens, turno e estado.
- **Validação em duas camadas:** no navegador (JavaScript) para resposta rápida e no servidor (Python) para garantir a segurança. Inclui formato dos campos, limite de idade, senha forte e e-mail duplicado.
- **Gerenciamento:** listagem em tabela, edição pelo painel lateral e exclusão individual.
- **Confirmação de exclusão:** é preciso digitar uma senha de confirmação antes de apagar qualquer registro.
- **Interface interativa:** mensagens Toast, mostrar/ocultar senha, envio de formulários com `fetch()` sem recarregar a página.
- **Página 404** personalizada.

## Tecnologias

| Tecnologia | Uso |
| --- | --- |
| Python | Lógica da aplicação e validações |
| Flask | Rotas, sessões e renderização das páginas |
| SQLite | Armazenamento dos dados |
| Jinja2 + HTML5 | Templates dinâmicos |
| CSS3 | Layout responsivo, animações e glassmorphism |
| JavaScript | DOM, eventos, `FormData`, `fetch()` e Toasts |
| Werkzeug | Hash e verificação de senhas |
| Flask-WTF | Proteção CSRF |
| Flask-Limiter | Limite de tentativas (rate limiting) |
| python-dotenv | Variáveis de ambiente |
| Gunicorn | Servidor WSGI para produção |

## Estrutura do projeto

```text
ProjetoFLASK/
├── .gitignore
├── README.md
└── meu_projeto/
    ├── app.py
    ├── requirements.txt
    ├── .env                  # arquivo local (não vai para o GitHub)
    ├── .prettierrc.json
    ├── instance/             # criada localmente; guarda o banco SQLite
    │   └── banco.db
    ├── static/
    │   ├── script.js
    │   ├── style.css
    │   └── png/
    └── templates/
        ├── 404.html
        ├── banco.html
        ├── excluir-banco-validacao.html
        ├── index.html
        ├── inicio.html
        ├── landing.html
        ├── login.html
        └── sign.html
```

## Executar localmente

### 1. Pré-requisitos

- Python 3 instalado
- Git (para clonar o repositório)

### 2. Clonar o repositório

```bash
git clone https://github.com/viniciuscancellara-dev/cadastro-flask.git
cd cadastro-flask
```

### 3. Criar e ativar o ambiente virtual

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instalar as dependências

```bash
pip install -r meu_projeto/requirements.txt
```

### 5. Criar a pasta do banco

O banco SQLite fica em `meu_projeto/instance/`. Essa pasta não é enviada ao GitHub, então crie-a antes da primeira execução:

```bash
mkdir meu_projeto/instance
```

### 6. Configurar as variáveis de ambiente

Crie o arquivo `meu_projeto/.env`:

```env
SECRET_KEY=gere_uma_chave_secreta_longa_e_aleatoria
DELETE_HASH=defina_a_senha_de_confirmacao_de_exclusao
DEBUG_MODE=True
DB_NAME=banco.db
```

| Variável | Para que serve |
| --- | --- |
| `SECRET_KEY` | Assina a sessão do Flask. Use um valor longo e aleatório. |
| `DELETE_HASH` | Senha usada para confirmar exclusões. Na primeira execução ela é transformada em hash e salva na tabela `config`. |
| `DEBUG_MODE` | `True` ativa o modo de depuração local. Em produção, deixe `False`. |
| `DB_NAME` | Nome do arquivo do banco dentro de `instance/`. |

> Nunca publique o `.env` nem use no repositório valores reais de produção.

### 7. Iniciar a aplicação

```bash
cd meu_projeto
python app.py
```

Acesse [http://127.0.0.1:5000](http://127.0.0.1:5000), clique em **Criar Conta**, registre um usuário e faça login.

### Produção

Em produção o app roda com Gunicorn, a partir da pasta `meu_projeto`:

```bash
gunicorn app:app
```

Defina `DEBUG_MODE=False` e configure as mesmas variáveis de ambiente no serviço de hospedagem.

## Segurança implementada

- Senhas com hash (Werkzeug), sem nunca guardar ou comparar texto puro.
- Rotas protegidas por sessão (`login_required`).
- Cookies de sessão com `HttpOnly`, `SameSite=Lax` e `Secure`.
- Proteção CSRF em todos os formulários e requisições `POST`.
- Limite de tentativas de login (5 falhas por minuto) e limites globais por IP.
- Consultas SQL parametrizadas (protege contra SQL Injection).
- Validação no servidor com listas de valores permitidos (turno, estado, linguagens).
- Mensagem de erro igual para "usuário inexistente" e "senha errada" no login.
- Configurações sensíveis em variáveis de ambiente.

São proteções básicas para um projeto de estudo. Não substituem uma auditoria de segurança para uso real.

## Limitações conhecidas e próximos passos

Este projeto está em evolução. O que ainda quero melhorar:

- [ ] Separar o `app.py` em módulos (rotas, banco, validações) usando Blueprints.
- [ ] Criar uma função única para conexão com o banco e para as validações, hoje repetidas em `/cadastrar` e `/editar`.
- [ ] Padronizar as respostas de erro do `/editar` em JSON (algumas ainda retornam texto simples).
- [ ] Criar a pasta `instance/` automaticamente na primeira execução.
- [ ] Ligar cada aluno cadastrado ao usuário que o criou (hoje todo usuário logado vê todos os registros).
- [ ] Trocar o limitador em memória por um armazenamento compartilhado (ex.: Redis) para funcionar com vários workers.
- [ ] Adicionar testes automatizados.

## O que este projeto me ensinou

CRUD completo com SQLite, autenticação e sessões, segurança básica de aplicações web, comunicação front-end/back-end com `fetch()` e JSON, validação em duas camadas e deploy com Gunicorn.

## Autor

**Vinicius Cancellara**

- [GitHub](https://github.com/viniciuscancellara-dev)
- [Projeto em execução](https://cadastro-flask.onrender.com)
