# Desafio Técnico - Cadastra

O desafio técnico consiste na coleta e armazenamento de dados de criptomoedas, cujo qual servirá, principalmente, para avaliar as habilidades técnicas na linguagem de programação Python, a capacidade analítica, o conhecimento em boas práticas de programação e a habilidade na manipulação de dados. O objetivo principal é desenvolver um programa que consuma dados de uma API de criptomoedas e os armazene em um banco de dados.

## Descrição do desafio:

O desafio consiste em criar uma aplicação Python que seja capaz de acessar uma API pública de criptomoedas, como o Crypto Market Cap, para extrair informações relevantes sobre diversas criptomoedas disponíveis no mercado. O programa deve ser capaz de coletar dados, como preços, capitalização de mercado, volume de negociação e outras métricas relevantes.

## Arquitetura planejada para o desafio:

-- Diagrama do Miro --

- Conexão com a API
- Salvamento dos dados puxados na camada bronze
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
Devemos salvar os dados sensíveis de acesso a API, como a nossa key individual, em um arquivo separado, que aqui, se chamará "config.py", pois é uma medida de segurança que previne que indivíduos mal intencionados utilizem da key individual da cont.

##
