# Stone Challenge

Desafio proposto como forma de avaliação técnica.

A API foi desenvolvida para uso simples de requests e retorna JSON como formato escolhido.

## Como rodar a API

- Para usar a API é necessário ter instalado na sua máquina:
    - Python
    - flask
    - sqlalchemy
    - flask_marshmallow
    - flask_sqlalchemy

Após ter instalado todos esses pacotes, siga os passos a seguir:
1. Clone o repositório:
``` git clone https://github.com/brunachaves/stone.challenge.git``` 

2. Mude para o repositório:
``` cd stone.challenge```

3. Rode o arquivo de configuração de base de dados:
``` python3 dbfunc_setup.py```

4. Rode o arquivo para adicionar Funcionários na base de dados:
``` python3 employeesadded.py```

5. Rode o arquivo de API:
``` python3 api.py```

**Obs:** Faça todos os requests para API em localhost:_portaindicadanoterminal_

## Como usar a API
- A API dá acesso a requests básicos e cada um deve obdecer aos parâmetros abaixo:

1. **Acesso ao README:**
Redireciona para o repositório README no Github.

Faça um request em localhost:_portaindicadanoterminal_/

Acesse com o browser para melhor visualização do README.

2. **Criar um novo funcionário:**
Cria um novo funcionário na base de dados respeitando os requisitos.

Faça um request POST em localhost:_portaindicadanoterminal_/employee, de keys name, age e role e respectivos valores

Retorna "Added!" quando bem sucedido.

3. **Mostrar todos os empregados:**
Exibe toda a base de dados de todos os funcionários.

Faça um request GET em localhost:_portaindicadanoterminal_/employee

Retorna a base de dados em formato JSON.

4. **Exibir Funcionário pela id:**
Mostra os dados associados a um funcionário específico de acordo com a id.

Faça um request GET em localhost:_portaindicadanoterminal_/employee/<id>

5. **Atualizar informações de Funcionário por id:**
Atualiza as informações de um Funcionário de id específica registradas na Base de dados.

Faça um request PUT em localhost:_portaindicadanoterminal_/employee/<id>

6. **Deletar registro de Funcionário por id:**
Deleta os registros de um Funcionário de id específica da Base de dados.

Faça um request DELETE em localhost:_portaindicadanoterminal_/employee/<id>


## Como interromper a aplicação:

No terminal, pressione CTRL + C para interromper a aplicação
