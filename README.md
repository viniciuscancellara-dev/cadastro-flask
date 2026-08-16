# Cadastro de Alunos — Flask + SQLite

Sistema simples de cadastro de alunos, feito com Flask (Python), HTML e CSS puro — sem JavaScript. Os dados são validados no back-end e persistidos em um banco SQLite local. Funcionalidades

- Formulário de cadastro com validação completa no servidor:
  - Nome (não vazio)
  - Idade (número entre 1 e 120)
  - E-mail (formato válido e **único** no banco)
  - Senha (mínimo 8 caracteres, com letra maiúscula, minúscula, número e símbolo)
  - Turno (seleção única via *radio button*)
  - Linguagens de interesse (múltipla escolha via *checkbox*)
  - Estado (seleção única via *select*)
- Persistência dos dados em banco **SQLite3**, sem uso de ORM
- Restrição de e-mail duplicado (`UNIQUE`), com tratamento de erro amigável
- Página inicial com opção de excluir todos os cadastros

##  Tecnologias

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- SQLite3 (módulo nativo do Python, sem dependências externas)
- HTML5 + CSS3 (sem frameworks e sem JavaScript)

##  Estrutura do projeto

```
meu_projeto/
├── app.py            
├── instance/
│   └── banco.db       
├── static/
│   └── style.css      
├── templates/
│   ├── index.html     
│   └── inicio.html    
└── README.md
```

##  Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd meu_projeto
   ```

2. Instale o Flask (caso ainda não tenha):
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

O banco de dados (`instance/banco.db`) e a tabela `usuarios` são criados automaticamente na primeira execução — não é necessário nenhum passo manual de configuração do banco.

##  Estrutura da tabela `usuarios`

| Coluna              | Tipo    | Observação                    |
|---------------------|---------|--------------------------------|
| id                   | INTEGER | Chave primária, autoincremento |
| nome                 | TEXT    | Obrigatório                    |
| idade                | INTEGER | Obrigatório                    |
| email                | TEXT    | Obrigatório e único (`UNIQUE`) |
| senha                | TEXT    | Obrigatório                    |
| observacao           | TEXT    | Opcional                       |
| linguagens_string    | TEXT    | Linguagens escolhidas, separadas por vírgula |
| turno                | TEXT    | Obrigatório                    |
| estado               | TEXT    | Obrigatório                    |

##  Próximos passos (ideias)

- Listar os cadastros em uma tabela HTML
- Permitir excluir um cadastro específico (não só todos de uma vez)
- Hash de senha (ex.: `werkzeug.security`) em vez de texto puro

##  Licença

Projeto de estudo, livre para uso e modificação.

## Desenvolvimento

Projeto desenvolvido por **Vinicius Cancellara**.