#Primeiro, se faz o import do que será útil no desenvolvimento da aplicação 

import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint
import config
import pandas as pd

#Agora, "chama-se" a API, utilizando da URL fornecida pela documentação do Crypto Market Cap, de onde são puxadas as informações de 10 criptomoedas, seguindo os parâmetros estabelecidos

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'100',
  'convert':'USD'
}

#Aqui, conectamos o nosso código a API, utilizando uma key individual fornecida pelo Crypto Market Cap

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.cryptomarket_api_access_key,
}

#Agora, trazemos os arquivos da API, em formato json

json = requests.get(url, params=parameters, headers=headers).json()

crypto = json['data']

# Aqui, podemos observar como os dados são trazidos da API
pprint.pprint(crypto)