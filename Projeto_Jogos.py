#Trazer o Pandas para utilização
import pandas as pd 
import numpy as np
import seaborn as sns

games = pd.read_csv("vgscore.csv", header=0)

games.head()

games.shape

games.columns
games.info()

for para_trocar in ["user_Score","VGscore"]:
  games.loc[games[para_trocar] == "N/A  ", para_trocar] = 0


colunas_para_converter = ["user_Score", "VGscore"]
games[colunas_para_converter] = games[colunas_para_converter].apply(pd.to_numeric)

games.info()

games_limpo = games.dropna(subset=['tot_sale'])

games_limpo.isna().sum()
games_limpo.dropna(subset=['na_sale', 'pal_sale', 'jp_sale', 'other_sale'], inplace=True)
games_limpo.isna().sum()
games_limpo.drop(labels=['tot_ship'], axis=1, inplace=True)
games_limpo.head()
games_limpo['tot_sale'] = games_limpo['tot_sale'].str.replace('m', '')
games_limpo['na_sale'] = games_limpo['na_sale'].str.replace('m', '')
games_limpo['jp_sale'] = games_limpo['jp_sale'].str.replace('m', '')
games_limpo['pal_sale'] = games_limpo['pal_sale'].str.replace('m', '')
games_limpo['other_sale'] = games_limpo['other_sale'].str.replace('m', '')

games_limpo['na_sale'] = games_limpo['na_sale'].apply(pd.to_numeric)
games_limpo['tot_sale'] = games_limpo['tot_sale'].apply(pd.to_numeric)
games_limpo['pal_sale'] = games_limpo['pal_sale'].apply(pd.to_numeric)
games_limpo['jp_sale'] = games_limpo['jp_sale'].apply(pd.to_numeric)
games_limpo['other_sale'] = games_limpo['other_sale'].apply(pd.to_numeric)

games_limpo.dtypes

games_limpo.describe()

games_interesse.sort_values(["user_Score", "tot_sale"], ascending = False)

games_interesse = games_limpo[(games_limpo["user_Score"] > 8) & (games_limpo["na_sale"] > 3)]

games_interesse.sort_values(["user_Score", "tot_sale"], ascending = False)

sns.set_theme(style="whitegrid")

sns.set_theme(style="darkgrid")

# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")

# Plot the responses for different events and regions
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmri)