# (C)reate (R)ead (U)pdate (D)elete

## Visão Geral
O projeto CRUD é uma interface gráfica feita em Python usando a biblioteca Tkinter.
Ele tem o objetivo de realizar as funções de Criação, Leitura, Atualização e Remoção de dados por meio de três interfaces integradas.
Enquanto a interface de login apenas valida a existência dos dados, a interface de registro recebe e insere os dados no banco de dados local, e a interface de administração altera ou remove esses dados.
## Objetivos
1. Testar os meus conhecimentos de OOP ✅
2. Interface Bonita e Organizada ✅
3. Conexão com banco de dados local ✅


# Instalação
Para instalar e executar este projeto localmente, siga os passos abaixo:

1. Clone o repositório:
`git clone https://github.com/usuario/nome-do-projeto.git`
2. Navegue até o diretório do projeto:
`cd nome-do-projeto`
3. Crie um ambiente virtual (opcional, mas recomendado):
`python -m venv venv`
4. Ative o ambiente virtual:
- Windows:
`venv\Scripts\activate`
- macOS/Linux:
`source venv/bin/activate`
5. Instale as dependências:
`pip install mysql-connector`
`pip install customtkinter`
`pip install Pillow`


*OBS: É necessário um SGDB SQL local para armazenar as informações, como o `MySQL `ou `SQL Server`. Instale algum desses sistemas e guarde as informações de autenticação para inserir no início do programa.*
# Uso
Para abrir a interface, você pode executar o arquivo interface.py ou o arquivo executável dentro da pasta dist:
`python interface.py`

# Funcionalidades Principais
### 1. Banco de dados
- Ao abrir a interface, primeiro você precisa inserir as informações do seu banco de dados local, como: Usuário, Senha e Host.
- Caso você não tenha alterado o padrão, o usuário é "root", a senha está vazia e o host é "localhost".

### 2. Registro
- Na interface, clique no botão Registrar para ser redirecionado para a janela de registro, onde você pode inserir suas informações para realizar o primeiro cadastro no banco de dados.

### 3. Login
- Após realizar o primeiro registro, você pode verificar sua existência no banco de dados inserindo o email e a senha na janela de login. Caso a senha ou o usuário estejam incorretos, uma mensagem de erro aparecerá no terminal e na interface para alertá-lo.

### 4. Administração
- Para entrar na janela de administração, basta digitar "admin" nos campos de email e senha.
- Nesta janela, você pode visualizar, alterar e deletar as informações de qualquer usuário, caso você possua o email.


# Funcionalidades
Neste código, utilizei classes para treinar OOP e deixei tudo no mesmo arquivo para facilitar a transformação em executável. Temos as classes `App`, `loginFrame`, `registerFrame`, `widgets `e `dataControl`:
### A classe `App`
- Ela herda o objeto `Ctk` do tkinter, responsável por criar a interface em si. Nela, defino título, dimensões e algumas configurações iniciais do banco de dados, como iniciar a conexão ao abrir a interface e efetuar a desconexão ao fechá-la. Dessa forma, tenho a interface vazia onde vou adicionando frames para preenchê-la.
- Nesta classe, temos alguns métodos que criei para auxiliar no posicionamento do background e das imagens em geral, na definição de fontes e a importantíssima função de mudar os frames dependendo do frame de origem. Coloquei as funções font e image como staticmethod porque elas não precisavam de uma referência à instância da classe, então acredito que fiz certo.
### A classe `loginFrame`, `registerFrame` e `adminFrame`
- Essas classes funcionam de forma igual com diferentes objetivos pois todas são frames com widgets posicionados e variáveis para armazenar os valores das `Entrys`.
### A classe `widgets`
- Nesta classe, temos alguns widgets criados por mim para reutilizar código e métodos que lidam com a lógica de negócio, se esse é o termo correto.
- Temos vários métodos que funcionam de forma similar, consistindo em um conjunto de widgets organizados de uma forma que eu usei recorrentemente, então resolvi criar uma função para facilitar a minha vida.
- Depois temos as funções `login`, `registro`, `admim` e `showKey`: a função `login`, `registro` e `admim` validam, adicionam, alteram e removem os dados respectivamente, usando funções da classe dataControl além de prover o tratamento de erros visual alterando partes da interface.
- A função `showKey` é usada para os botões de esconder ou exibir a senha
### A classe `dataControl`
- Como o nome já diz ela controla toda a manipulação de informações da interface com os métodos `connect`, `disconnect`, `create`, `read`, `update`, `delete`, `insert`.
- A função `connect` realiza a conexão com o banco de dados ao iniciar a interface e caso não exista cria o esquema e tabela usando a função create.
- A função `disconnect` faz a desconexão com o banco de dados ao fechar a interface e fecha a aplicação.
- As outras funções realizam querys no banco de dados inserindo, removendo ou atualizando as informações.

# Dependências
Essas são as dependências do projeto
- `mysql-connector-python`
Responsável pelo conector entre o python e o servidor local MySQL
- `customtkinter`
Responsável pela criação da interface gráfica. Vale ressaltar que essa lib é uma variante da tkinter porém focada na personalização dos widgets
- `hmac`(built-in)
Responsável por aplicar a função Hash nas strings e compara-las
- `hashlib`(built-in)
Responsável por prover a função Hash em si.
- `re`(built-in)
Responsável por implementar RegEx
- `os`(built-in)
Responsável por fornecer acesso ao caminho dos arquivos no ambiente virtual
