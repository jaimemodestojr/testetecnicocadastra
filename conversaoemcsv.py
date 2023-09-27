import pandas as pd
import conversaoemdf

# Agora, convertemos ambos os dataframes para o formato csv, para exportarmos, sem grandes problemas, para o Cloud Storage do GCP

conversaoemdf.df = conversaoemdf.df.to_csv("tabela_geral.csv", index = False)

conversaoemdf.df_values = conversaoemdf.df_values.to_csv("tabela_valores.csv", index = False)