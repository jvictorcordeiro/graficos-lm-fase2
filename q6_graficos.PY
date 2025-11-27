import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================
#  PALETA ALFA-EJA
# ============================
ROXO_ESCURO = "#651B73"
LILAS       = "#8E2BAF"
VERDE_AGUA  = "#1CB9A3"
AMARELO     = "#FDB913"
ROSA        = "#E62270"
AZUL_CIANO  = "#008BBC"

# ============================
#  1. CARREGAR BASE
# ============================
df = pd.read_csv("q6_escolas_que_deixaram_2025.csv")

# total por município
tot_mun = df.groupby("Municipio")["Quantidade"].sum().reset_index()

# total por zona
tot_zona = df.groupby("Zona")["Quantidade"].sum().reset_index()

# ============================
#  2. BARRA HORIZONTAL - TOTAL POR MUNICÍPIO
# ============================
df_ord = tot_mun.sort_values("Quantidade", ascending=True)

plt.figure(figsize=(12,7))
plt.barh(df_ord["Municipio"], df_ord["Quantidade"], color=AZUL_CIANO)
plt.title("Escolas que deixaram de ofertar EJA em 2025 (por município)", fontsize=14, fontweight="bold")
plt.xlabel("Quantidade de escolas")
plt.grid(axis="x", alpha=0.3)

for i, v in enumerate(df_ord["Quantidade"]):
    plt.text(v + 0.05, i, str(v), va="center")

plt.tight_layout()
plt.show()

# ============================
#  3. BARRAS EMPILHADAS - URBANA x RURAL POR MUNICÍPIO
# ============================
pivot = df.pivot(index="Municipio", columns="Zona", values="Quantidade").fillna(0)

plt.figure(figsize=(12,7))
x = np.arange(len(pivot.index))

plt.bar(x, pivot["Rural"], color=VERDE_AGUA, label="Rural")
plt.bar(x, pivot["Urbana"], bottom=pivot["Rural"], color=ROXO_ESCURO, label="Urbana")

plt.xticks(x, pivot.index, rotation=45, ha="right")
plt.title("Escolas que deixaram de ofertar EJA (zona rural vs urbana)", fontsize=14, fontweight="bold")
plt.ylabel("Quantidade")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# ============================
#  4. GRÁFICO DE PIZZA - TOTAL POR ZONA
# ============================
plt.figure(figsize=(7,7))
plt.pie(tot_zona["Quantidade"], labels=tot_zona["Zona"], autopct='%1.1f%%',
        colors=[VERDE_AGUA, ROXO_ESCURO])
plt.title("Proporção de escolas que deixaram de ofertar EJA por zona", fontsize=14, fontweight="bold")
plt.show()
