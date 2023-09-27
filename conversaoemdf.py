import pandas as pd
import consumoapi as c

#Aqui, converteremos o nosso arquivo json em dataframe, o que nos facilitará imensamente a manipulação de dados

# Essa é o primeiro dataframe, que será a primeira tabela

df = pd.DataFrame(columns=['ID', 'Name', 'Slug', 'Symbol', 'Price'])

for i in range(0, 100):
  currentItem = c.crypto[i]
  df.loc[i] = [c.crypto[i]['id'], c.crypto[i]['name'], c.crypto[i]['slug'], c.crypto[i]['symbol'], c.crypto[i]['quote']['USD']['price']]


print(df)

# Esse é o segundo dataframe, que será a segunda tabela

df_values = pd.DataFrame(columns=['Name', 'Circulating Supply', 'Price (now)', 'Market Cap', 'Percent Change in 24 hours', 'Volume in 24 hours'])

for i in range(0, 100):
  currentItem = c.crypto[i]
  df_values.loc[i] = [c.crypto[i]['name'], c.crypto[i]['circulating_supply'], c.crypto[i]['quote']['USD']['price'], c.crypto[i]['quote']['USD']['market_cap'], c.crypto[i]['quote']['USD']['percent_change_24h'], c.crypto[i]['quote']['USD']['volume_24h']]


print(df_values)