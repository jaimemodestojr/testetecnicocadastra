# Desafio Técnico - Cadastra

O desafio técnico consiste na coleta e armazenamento de dados de criptomoedas, cujo qual servirá, principalmente, para avaliar as habilidades técnicas na linguagem de programação Python, a capacidade analítica, o conhecimento em boas práticas de programação e a habilidade na manipulação de dados. O objetivo principal é desenvolver um programa que consuma dados de uma API de criptomoedas e os armazene em um banco de dados.

## Descrição do desafio:

O desafio consiste em criar uma aplicação Python que seja capaz de acessar uma API pública de criptomoedas, como o Crypto Market Cap, para extrair informações relevantes sobre diversas criptomoedas disponíveis no mercado. O programa deve ser capaz de coletar dados, como preços, capitalização de mercado, volume de negociação e outras métricas relevantes.

## Arquitetura planejada para o desafio:

-- Diagrama do Miro --

- Conexão com a API utilizando Python
- Salvamento dos dados puxados obtidos em tabela no GCP
- Tratamento e limpeza iniciais dos dados
- Salvamento dos dados puxados na camada prata
- Revisão e tratamento mais aprimorado dos dados
- Salvamento dos dados puxados na camada ouro
- Opcional:
  - Usar dashboards para demonstração;
  - Web app com Streamlit;

Ao final, sugerir futuras implantações e melhorias para o projeto, como por exemplo, chatbot com LLM, web app, etc.

## Primeiro passo - Conexão com a API:

O primeiro passo consiste em conectar com a API do Crypto Market Cap e puxar os dados necessários dela e, para isso, criamos uma conta gratuita para uso básico no mesmo, o qual nos fornecerá uma "key" individual para a API. Com a nossa key em mãos, podemos, utilizando Python, puxar os dados da API, seguindo o código sugerido pela documentação do Crypto Market Cap (https://coinmarketcap.com/api/documentation/v1/) e adaptando-o para o nosso uso.
Devemos salvar os dados sensíveis de acesso a API, como a nossa key individual, em um arquivo separado, que aqui, se chamará "config.py", pois é uma medida de segurança que previne que indivíduos mal intencionados utilizem da key individual da conta.

## Ingestão dos dados:

Ingerimos, a partir da API da Crypto Market Cap, os dados das 10 criptomoedas com mais movimentações no presente momento da ingestão dos dados. São elas:

--- Print da tabela

Usamos a biblioteca Python chamada Pandas para convertermos os dados, que foram ingeridos em formato json, para o formato dataframe, o que nos facilitará imensamente o trabalho de manipulação dos dados.

--- Print do dataframe

Separaremos os dados em 11 tabelas diferentes, a primeira sendo uma tabela mais geral, com os dados das 10 criptomoedas com mais movimentações e, as 10 subsequentes, serão tabelas com detalhamento de cada uma dessas 10 criptomoedas ditas anteriormente.

## Limpeza e tratamento dos dados brutos:

Começaremos a limpeza e o tratamento dos dados brutos analisando se precisaremos fazer algum retoque ou mudança nos dados trazidos da API. Para isso, visualizamos cada uma das 11 tabelas, afim de verificarmos se o conteúdo delas está, aparentemente, correto.

--- print df

Para um volume de dados como esse, isto é, bem baixo, podemos fazer essa análise olhando uma por uma, mas, caso estivéssemos trabalhando com Big Data ou mesmo com banco de dados mais extensos, precisaríamos ser mais generalistas e fazer os tratamentos mais comuns e gerais que são empregados na engenharia de dados, como por exemplo: exclusão de arquivos NULL, exclusão de arquivos falsos ou com erros grotescos, modificação de simbologia de números (geralmente mudando de , para .), entre outros.

## 
