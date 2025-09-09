# %%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sqlalchemy import create_engine
# %%
# Conectar ao banco de dados SQLite e ler a tabela
engine = create_engine('sqlite:///..\\data\\processed\\db_dadostse.sqlite3')
df = pd.read_sql_table('tb_porcentagem_genero_partido', con=engine, index_col='SG_PARTIDO')
df_genero_2024 = df.rename(columns={'PORCENTAGEM_FEMININO': 'FEMININO', 'PORCENTAGEM_MASCULINO': 'MASCULINO'})

# %%
# Configurar o estilo do gráfico e plotar
sns.set_theme(style="whitegrid")

cores = ["#FF5E01", "#12C0FA"]
ax = df_genero_2024.plot(kind='barh', stacked=True, color=cores, figsize=(12, 8), width=0.7)

plt.title('Distribuição de Gênero de Candidatos de 2024 por Partido (em %)', fontsize=16)
plt.ylabel('Partido', fontsize=12)
plt.xlabel('Porcentagem (%)', fontsize=12)

for c in ax.containers:
    labels = [f'{v.get_width():.1f}%' if v.get_width() > 0 else '' for v in c]
    ax.bar_label(c, labels=labels, label_type='center', fontsize=10, rotation=0)

plt.legend(title='Gênero', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
# %%
