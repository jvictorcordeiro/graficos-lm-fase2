import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================
# PALETA ALFA-EJA
# ============================
ROXO = "#651B73"
LILAS       = "#8E2BAF"
VERDE  = "#1CB9A3"
AMARELO     = "#FDB913"
ROSA        = "#E62270"
CIANO  = "#008BBC"


# ============================
# 1. CARREGAR DADOS
# ============================
df = pd.read_csv("q47_espacos_memoria_eja.csv")

# Padronizar Sim/Nao
bin_map = {
    "Sim": 1,
    "Nao": 0,
    "Sim (Virtual)": 1,
    "": 0,
    np.nan: 0
}

cols_bin = ["Centro_Memoria", "Arquivo_Historico", "Museu_Exposicao", "Outro"]

df_bin = df.copy()
for col in cols_bin:
    df_bin[col + "_bin"] = df_bin[col].map(bin_map)

df_bin = df_bin.set_index("Municipio")[ [c+"_bin" for c in cols_bin] ]
df_bin.columns = ["Centro de Memória", "Arquivo Histórico", "Museu/Exposição", "Outro"]

# ============================
# 2. TOTAIS POR TIPO DE ESPAÇO
# ============================
totais = df_bin.sum().sort_values(ascending=False)

plt.figure(figsize=(9,5))
totais.plot(kind="bar", color=[ROXO, VERDE, AMARELO, CIANO])
plt.title("Existência de Espaços de Memória da EJA nos Municípios")
plt.ylabel("Quantidade de Municípios")
plt.xticks(rotation=15, ha="right")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# ============================
# 4. BARRAS EMPILHADAS
# ============================
df_bin.plot(kind="bar", stacked=True, figsize=(14,6),
            color=[ROXO, VERDE, AMARELO, CIANO])
plt.title("Distribuição dos Espaços de Memória da EJA (Empilhado)")
plt.ylabel("Sim (1) / Não (0)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()