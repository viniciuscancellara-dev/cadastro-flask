document.addEventListener("DOMContentLoaded", function () {
//so executa dps q o html inteiro carregar

    // Precisam bater com as regex do lado do Python app.py
    const EMAIL_REGEX = /^[\w.-]+@[\w.-]+\.\w+$/;
    const SENHA_REGEX = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\-_@!#$%^&*()=+])[A-Za-z\d\-_@!#$%^&*()=+]{8,}$/;

    //TOAST

    //essa funcao recebe um array de strings mensagens e desenha o pop-up
    //se nao existe (!container) cria uma do zero com document.createElement e joga ela no body com appendChild ta bom lembra disso

    function mostrarToast(mensagens) {
        let container = document.getElementById("toast-container");
        if (!container) {
            container = document.createElement("div");
            container.id = "toast-container";
            document.body.appendChild(container);
        }

        //aqui monta o cartaozinho: cria uma div class="toast" dentro dela uma ul
        //e pra cada mensagem do array cria um li

        const toast = document.createElement("div");
        toast.className = "toast";

        const lista = document.createElement("ul");
        mensagens.forEach(mensagem => {
            const item = document.createElement("li");
            item.textContent = mensagem;
            lista.appendChild(item);
        });
        toast.appendChild(lista);

        container.appendChild(toast);
        //setTimeout agenda algo pra rodar depois de x milissegundos  depois de 4.5s adiciono a classe toast-saindo 
        // (que no CSS tem uma animation de fade e slide pra fora) so que se eu chamasse toast.remove() na mesma hora
        //  o elemento sumiria instantaneamente e a animação nem apareceria
        setTimeout( () => {
            toast.classList.add("toast-saindo");
            setTimeout( () => {
                toast.remove();
            }, 300);
        }, 4500);
    }

    //validar campos comuns

    function validarCamposComuns(form) {
        const erros = [];

        //essa funcao recebe um form e devolve um array com as mensagens de erro encontradas
        // se nao achar nada errado devolve um array vazio ela e generica de proposito: 
        // tanto o form de cadastro quanto o form de edicao tem campos nome, idade, email, turno, linguagem e estado
        //  com os mesmos name  enteo a mesma funcao serve pros dois

        const nome = form.querySelector('[name="nome"]').value;
        if (nome.trim() === "") {
            erros.push("O nome não pode estar vazio.");
        }

        //no form.querySelector('[name="nome"]') em vez de usar getElementById eu busco pelo atributo name fiz assim porque 
        // id="nome" existe no form de cadastro mas no form de edicao o id e id="edit-nome"

        const campoIdade =form.querySelector('[name="idade"]');
        if (campoIdade === "") {
            erros.push('A idade nao pode estar vazia.')
        } else {
            const idade =parseInt(campoIdade, 10);
            if (isNaN(idade) || idade <= 0 || idade > 120) {
                erros.push("Informe uma idade válida (entre 1 e 120).");
        }}
        

        const email = form.querySelector('[name="email"]').value;
        if (!EMAIL_REGEX.test(email)) {
            erros.push("Informe um email válido.");
        }

        const turnoSelecionado = form.querySelector('[name="turno"]:checked');
        if (!turnoSelecionado) {
            erros.push("Selecione um turno.");
        }

        const linguagensSelecionadas = form.querySelectorAll('[name="linguagem"]:checked');
        if (linguagensSelecionadas.length === 0) {
            erros.push("Selecione pelo menos uma linguagem.");
        }

        const estado = form.querySelector('[name="estado"]').value;
        if (!estado) {
            erros.push("Selecione um estado.");
        }

        return erros;
    }

    //cadastro

    const formCadastro = document.querySelector(".form-cadastro");
    if (formCadastro) {
        formCadastro.addEventListener("submit", event => {
            const erros = validarCamposComuns(formCadastro);

            const senha = formCadastro.querySelector('[name="senha"]').value;
            if (!SENHA_REGEX.test(senha)) {
                erros.push("A senha precisa ter 8+ caracteres, com maiúscula, minúscula, número e símbolo.");
            }

            if (erros.length > 0) {
                event.preventDefault();
                mostrarToast(erros);
            }
        });
    }

    // =========================================================
    // PAGINA BANCO: ABRIR/FECHAR PAINEL DE EDICAO
    // =========================================================
    const botaoEditar = document.getElementById("botao-editar");
    const containerTabela = document.querySelector(".container-tabela");
    const containerEditar = document.querySelector(".container-editar");
    const painelEditar = document.querySelector(".painel-editar");
    const seletorUsuario = document.getElementById("selecionar-usuario");
    const botaoCancelar = document.getElementById("botao-cancelar-edicao");
    const formEditar = document.getElementById("form-editar");

    //so pego referencia de todos que vou precisar mexer uma vez so e guardo em constantes isso evita ficar
    //  chamando document.getElementById toda hora

    if (botaoEditar && painelEditar) {
        botaoEditar.addEventListener("click", () => {
            if (containerTabela) containerTabela.style.display = "none";
            if (containerEditar) containerEditar.style.display = "none";
            painelEditar.style.display = "block";
        });
    }

    if (botaoCancelar && painelEditar) {
        botaoCancelar.addEventListener("click", () => {
            painelEditar.style.display = "none";
            if (containerTabela) containerTabela.style.display = "";
            if (containerEditar) containerEditar.style.display = "";
            if (formEditar) formEditar.reset();
        });
    }

    //quando clica no botao "Editar" escondo a div da tabela e a div dos botoes (display = "none")
    //e mostro o painel de edicao (display = "block")

    // ao escolher um usuario no select preenche os campos com os dados
    // que ja estao guardados nos data da linha correspondente da tabela

    if (seletorUsuario && formEditar) {
        seletorUsuario.addEventListener("change", () => {
            const idSelecionado = seletorUsuario.value;
            if (!idSelecionado) return;

            const linha = document.querySelector('tr[data-id="' + idSelecionado + '"]');
            if (!linha) return;

            //change acontece toda vez que o valor do select muda pego o value da opcao escolhida
            //(que é o id do usuario porque no banco.html eu defini option value="{{ aluno[0] }}" Se estiver vazio 
            // usuario ainda nao escolheu nada idSelecionado seria "" dou um return e nao faz nada

            formEditar.querySelector('[name="nome"]').value = linha.dataset.nome;
            formEditar.querySelector('[name="idade"]').value = linha.dataset.idade;
            formEditar.querySelector('[name="email"]').value = linha.dataset.email;
            formEditar.querySelector('[name="observacao"]').value = linha.dataset.observacao;

            const turnoAtual = linha.dataset.turno;
            formEditar.querySelectorAll('[name="turno"]').forEach(radio => {
                radio.checked = (radio.value === turnoAtual);
            });

            //radio e diferente de input de texto nao da pra so setar .value preciso pegar todos os radios do grupo turno e
            //pra cada um marcar checked = true so se o value dele bater com o turno salvo e false nos outros

            const linguagensAtuais = linha.dataset.linguagens ? linha.dataset.linguagens.split(",") : [];
            formEditar.querySelectorAll('[name="linguagem"]').forEach(checkbox => {
                checkbox.checked = linguagensAtuais.includes(checkbox.value);
            });
            //mesma logica pros checkbox mas eles vem em string ent eu facao um .split(",")
            //  e o linha.dataset.linguagens.split(",") : []; fala que se nao tiver nada pra splita vira um array vazio
            formEditar.querySelector('[name="estado"]').value = linha.dataset.estado;
        });
    }

    // validacao antes de salvar a edicao senha nao entra aqui
    if (formEditar) {
        formEditar.addEventListener("submit", event => {
            const erros = validarCamposComuns(formEditar);

            if (!seletorUsuario.value) {
                erros.push("Selecione um usuário para editar.");
            }

            if (erros.length > 0) {
                event.preventDefault();
                mostrarToast(erros);
            }
        });
    }



    const erroLogin = document.getElementById("erro-login");

    if (erroLogin) {
        mostrarToast([erroLogin.dataset.erro]);
    }

    const formLogin = document.querySelector(".form-login");
    const btnLogin = document.getElementById('btn-login')

    if (formLogin) {
        formLogin.addEventListener("submit", event => {

            const erros = [];

            const usuario = formLogin.querySelector('[name="usuario"]').value.trim();
            const senha = formLogin.querySelector('[name="senha"]').value;

            if (usuario === "") {
                erros.push("Digite seu usuário.");
            }

            if (senha === "") {
                erros.push("Digite sua senha.");
            }

            if (erros.length > 0) {
                event.preventDefault();
                mostrarToast(erros);
                return;
            }
            
            btnLogin.textContent = 'Entrando. . .';
            btnLogin.disabled = true;

        });
    }

    //vizualizar senha do login

    const senha = document.getElementById('login-senha')
    const showpass = document.getElementById('btn-showpass')
    const img = document.getElementById('png-showpass')
    if (showpass) {
        showpass.addEventListener("click", () => {
            if (senha.type === 'password') {
                senha.type = 'text'
                img.src = '/static/png/hidepassword.png'
            } else {senha.type = 'password'
                    img.src = '/static/png/showpassword.png'
            }
        });
    }

    const erroValidacao = document.getElementById("erro-validation");

    if (erroValidacao) {
        console.log("erro funcionou kkkkk:", erroValidacao.dataset.erro);
        mostrarToast([erroValidacao.dataset.erro]);
    }

    const senha_validacao = document.querySelector(".form-validation");

    if (senha_validacao) {
        senha_validacao.addEventListener("submit", event => {

            const erros = [];

            const senha = senha_validacao.querySelector('[name="password"]').value;

            if (senha === "") {
                erros.push("Digite sua senha.");
            }

            if (erros.length > 0) {
                event.preventDefault();
                mostrarToast(erros);
            }
        });
    }
});

// domcontentloaded
// espera o html carregar antes de executar o javascript

// getelementbyid / queryselector
// procura e pega elementos do html

// queryselectorall
// pega varios elementos que combinam com o seletor

// value
// pega o valor digitado ou selecionado em um campo

// textcontent
// altera ou pega o texto de um elemento

// checked
// verifica se checkbox ou radio esta marcado

// addeventlistener
// faz o javascript esperar por um evento como click input change ou submit

// preventdefault
// impede o comportamento padrao do navegador
// no formulario impede o envio quando existe algum erro

// classlist add remove toggle contains
// adiciona remove alterna ou verifica classes css

// foreach
// passa por cada elemento de uma lista

// formdata
// pega os dados preenchidos de um formulario

// get
// pega um valor do formdata

// getall
// pega todos os valores de campos com o mesmo name
// usado principalmente com checkbox

// push
// adiciona um novo erro na lista de erros

// mostrar toast
// cria e mostra as mensagens de erro na tela
// depois de alguns segundos remove o aviso

// login
// primeiro o javascript verifica se usuario e senha foram preenchidos
// se estiver tudo certo deixa o formulario ir para o flask
// o flask faz a verificacao real dos dados no banco
// se o flask devolver um erro o javascript mostra esse erro no toast