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
AZUL  = "#008BBC"

# ============================
# 1. CARREGAR DADOS
# ============================
df = pd.read_csv("q49_memoria_eja.csv")

map_bin = {"Sim": 1, "Nao": 0}
df["Atividades_bin"] = df["Atividades_Resgate"].map(map_bin)
df["Memoria_bin"]    = df["Memoria_Viva"].map(map_bin)

plt.figure(figsize=(8,5))

# Valores
valores = [
    df["Atividades_bin"].sum(),
    df["Memoria_bin"].sum()
]

# Labels
labels = [
    "Atividades de Resgate",
    "Memória Viva registrada"
]

# Cores
cores = [ROXO, VERDE]

plt.bar(labels, valores, color=cores)

plt.title("Municípios: Atividades de Resgate e Memória Viva")
plt.ylabel("Quantidade de Municípios")

plt.tight_layout()
plt.show()


# ============================
# 4. HEATMAP — MEMÓRIA x RESGATE
# ============================
heat = df.set_index("Municipio")[["Atividades_bin", "Memoria_bin"]]
heat.columns = ["Atividades de Resgate", "Memória Viva"]

# ============================
# 5. BARRAS EMPILHADAS
# ============================
heat.plot(kind="bar", figsize=(12,6), stacked=True, color=[ROXO, VERDE])
plt.title("Atividades de Memória da EJA — Distribuição por Município")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Sim (1) / Não (0)")
plt.tight_layout()
plt.show()
