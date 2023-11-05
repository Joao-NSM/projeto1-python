## Calculator

Projeto de uma calculadora simples. Esse projeto tem o foco de aplicar conhecimentos de desenvolvimento de software de forma incremental.
O projeto é divido em passos para ter um senso de progressão. Cada passo deverá ser executado e registrado na forma de commits. O projeto está divido em N partes. A primeira parte é sincrona usando a arquitetura Client/Server, a segunda parte é assincrona utilizando o broker para notificar o servidor 2 que popula o banco. Os passos são descritos a seguir:

0. Criar um dockerfile com a stack de trabalho.
- Objetivos:
* Aprender a configurar o ambiente de desenvolvimento
* Aprender a utilizar o docker para compartilhar o ambiente de forma transparente.
* Aprender a utilizar o dockerfile

Java/Springboot
C/civetweb
Python/Flask

1. Criar um webserver com o endpoint /hello e deve devolver uma resposta em json com o formato
{
"message" : "Hello Calculador"
}
- Objetivos:
* Aprender a configurar um endpoint
* Realizar uma requisição
* Enviar a resposta com o encoding json

2. Enviar dois números para o servidor Calculator via URL e o servidor deverá fazer uma operação de soma e devolver uma resposta em json
no formato:
{
"value_1" : 10,
"value_2" : 30,
"result" : 40
}
- Objetivos:
* Aprender a enviar dados na requisição via URL
* Ler os parametros da URL e processá-los

3. Alterar o servidor para dar suporte as operações aritiméticas soma, subtração, multiplicação e divisão. Enviar a operação pela URL
e retornar a resposta via json no formato:

{
"operation": "sum",
"value_1" : 10,
"value_2" : 30,
"result" : 42
}

4. Registrar as requisições em um arquivo CSV no seguinte formato:
operation,value_1, value_2, result, date
sum, 10, 10, 20, 1697732730

A data está no formato epoch

5. Criar um endpoint /report, ler o arquivo de devolver os registros armazenados no arquivo no formato json em lista:
[
{
"operation": "sum",
"value_1" : 10,
"value_2" : 30,
"result" : 42,
"date": 2023-10-10T10:23:22
},
{
"operation": "sub",
"value_1" : 10,
"value_2" : 30,
"result" : -20,
"date": 2023-10-10T10:24:22
}
]


6. Criar um tratamento de erro quando uma das informações não forem enviadas, retornar o erro em json no formato:
{
"error": "Value 1 not informed"
}

{
"error": "Missing operator"
}

7. Criar uma tabela em MySQL para registrar os dados da operação, substituindo o armazenamento por arquivo. Utilizar um container para criar a base e a tabela. Criar um arquivo docker compose para gerencia-los.

8. Modificar o endpoint /report para devolver os dados armazenados no banco no formato json:
[
{
"operation": "sum",
"value_1" : 10,
"value_2" : 30,
"result" : 42,
"date": 2023-10-10T10:23:22
},
{
"operation": "sub",
"value_1" : 10,
"value_2" : 30,
"result" : -20,
"date": 2023-10-10T10:24:22
}
]

9. Modificar o endpoint /report para aceitar dados opcionais de intervalos de datas para gerar o dados no periodo selecionado.
Em caso de receber somente a data inicial será mostrada a partir da data informada
Em caso de receber somente a data final será mostrada até a data informada

10. Fazer um teste de carga e levantar o desempenho do servidor no seu momento atual para verificar o total de requisições atendidas.

11. Alterar o servidor para ofertar um pool de threads para aumentar a capacidade de processamento das requisições. Medir novamente o desempenho.

12. Mover a operação do banco para um metodo assincrono.

13. Logar as operações do banco em um arquivo log em caso de erro.

14. Separar a aplicação em dois servidores sendo um para processar os calculos e o segundo para responder aos relatórios

15. Criar um proxy reverso para unificar os dois servidores em um único endereço usando NGINX. Adicionar no docker compose

16. Criar um cliente e consumir os endpoints do servidor, adicionar no docker compose

--- Parte II

01. Criar um branch para a versão assincrona

02. Adicionar um broker no docker compose

03. Remover o banco de dados do servidor que calcula, substituir por uma mensagem e enviar para o tópico no broker.

04. Criar um serviço para consumir o topico para preencher o banco.

05. Criar um serviço de notificação para informar ao usuário que há novos dados no banco de forma periodica


-- Parte III

01. Verificar quantos processamentos foram realizados para cada uma das operações

02. Plotar gráfico dos dados coletados