#### Importando bibliotecas

import pandas as pd
import matplotlib.pyplot as plt


##### Manipulando dados

df = pd.read_excel(r'C:\Users\Jhona\OneDrive - Grupo Marista\Clube de Finanças\Clube\Dados\SPX.xlsx', index_col=0, parse_dates=True)
df = df.rename(columns={'S&P 500': 'SP_500'})
dados = df[df.IBOV != '-']
dados = dados[dados.SP_500 != '-']

### Obtendo retornos
dados_pct = dados.pct_change().dropna()
obsv = len(dados_pct)


### Obtendo retornos iguais
obs = dados_pct[dados_pct.IBOV < 0]
obs = obs[obs.SP_500 < 0]
total = len(obs)
print(obsv)
print(total)

### Gráfico de correlação por janelas
n = 60
roll_correl = dados_pct['IBOV'].rolling(n).corr(dados_pct['SP_500']).dropna()


plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(roll_correl.index, roll_correl)
ax.set_xlabel('Data')
ax.set_ylabel('Correlação')
ax.set_title('Correlação IBOV x S&P 500')
ax.legend('Correlação')
plt.show()