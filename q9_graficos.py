import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ================================
# PALETA ALFA-EJA DA FASE 1
# ================================

cores = ["#651B73", "#8E2BAF", "#1CB9A3", "#FDB913", "#E62270", "#4FC3F7", "#008BBC"]

# ================================
# CARREGAR BASE
# ================================
df = pd.read_csv("q9_articulacao.csv")
df.set_index("Municipio", inplace=True)

# Lista de secretarias
cols = df.columns

# ================================
# 1) TOTAL POR SECRETARIA (barras)
# ================================
totais = df.sum().sort_values(ascending=False)

plt.figure(figsize=(12,6))
totais.plot(kind="bar", color=cores)
plt.title("Número de Municípios com Articulação por Secretaria (2025)")
plt.ylabel("Quantidade de municípios")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# ================================
# 3) BARRAS EMPILHADAS POR MUNICÍPIO
# ================================
df.plot(kind="bar", stacked=True, figsize=(16,7), color=cores)
plt.title("Articulação da EJA com Outras Secretarias — Por Município")
plt.ylabel("Sim (1) ou Não (0)")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Secretarias")
plt.tight_layout()
plt.show()

# ================================
# 4) PIZZA — DISTRIBUIÇÃO GERAL
# ================================
plt.figure(figsize=(10,10))
plt.pie(totais, labels=totais.index, autopct="%1.1f%%",
        colors=cores, startangle=140)
plt.title("Distribuição das Secretarias com Maior Articulação (2025)")
plt.tight_layout()
plt.show()

