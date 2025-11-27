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
#  1. CARREGAR DADOS
# ============================
df = pd.read_csv("q3_acompanhamento.csv")

# ============================
#  2. REGIÕES DOS MUNICÍPIOS
# ============================
map_regiao = {
    "Oiapoque": "Norte",
    "Carauari": "Norte",
    "Coari": "Norte",
    "Belém": "Norte",

    "Caucaia": "Nordeste I",
    "Fortaleza": "Nordeste I",
    "Icapuí": "Nordeste I",
    "Alto do Rodrigues": "Nordeste I",

    "São Francisco do Conde": "Nordeste II",
    "Conde": "Nordeste II",
    "Ipojuca": "Nordeste II",
    "Cabo de Santo Agostinho": "Nordeste II",
    "Brejo Grande": "Nordeste II",
    "Santa Luzia do Itanhy": "Nordeste II",
}

df["Regiao"] = df["Municipio"].map(map_regiao)

# ============================
#  3. AGRUPAÇÕES
# ============================
tot_nivel = df.groupby("Nivel").size().reset_index(name="Total")

tot_regiao = df.groupby("Regiao").agg(
    Nivel_Medio=("Nivel", "mean"),
    Contagem=("Nivel", "count")
).reset_index()

pivot_heatmap = df.pivot(index="Municipio", columns="Nivel", values="Nivel")
pivot_heatmap = pivot_heatmap.notnull().astype(int)

# ============================
#  4. GRÁFICOS
# ============================

# 4.1 – Barras verticais: total por nível
plt.figure(figsize=(7,5))
plt.bar(tot_nivel["Nivel"], tot_nivel["Total"], color=[ROXO_ESCURO, LILAS, AZUL_CIANO, VERDE_AGUA, AMARELO, ROSA])
plt.xticks(tot_nivel["Nivel"])
plt.title("Distribuição dos níveis de acompanhamento pedagógico", fontsize=13, fontweight="bold")
plt.xlabel("Nível")
plt.ylabel("Total de municípios")
plt.grid(axis="y", alpha=0.3)
for i, v in enumerate(tot_nivel["Total"]):
    plt.text(tot_nivel["Nivel"][i], v+0.1, str(v), ha="center")
plt.tight_layout()
plt.show()

# 4.2 – Barras horizontais por município
df_ord = df.sort_values("Nivel", ascending=True)

plt.figure(figsize=(10,7))
plt.barh(df_ord["Municipio"], df_ord["Nivel"], color=AZUL_CIANO)
plt.title("Nível de acompanhamento pedagógico por município", fontsize=13, fontweight="bold")
plt.xlabel("Nível")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.show()

# 4.4 – Radar por região (médias)
regioes = tot_regiao["Regiao"].tolist()
valores = tot_regiao["Nivel_Medio"].tolist()

angles = np.linspace(0, 2*np.pi, len(regioes), endpoint=False).tolist()
valores += valores[:1]
angles += angles[:1]

plt.figure(figsize=(7,7))
ax = plt.subplot(111, polar=True)
ax.plot(angles, valores, linewidth=2, color=AZUL_CIANO)
ax.fill(angles, valores, alpha=0.15, color=AZUL_CIANO)
ax.set_thetagrids(np.degrees(angles[:-1]), regioes)
plt.title("Nível médio de acompanhamento por região", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.show()

# 4.5 – Heatmap (município x nível)
plt.figure(figsize=(10,6))
plt.imshow(pivot_heatmap, aspect="auto", cmap="Purples")
plt.colorbar(label="Presença do nível (1 = marcado)")
plt.xticks(range(6), ["N0","N1","N2","N3","N4","N5"])
plt.yticks(range(len(pivot_heatmap.index)), pivot_heatmap.index)
plt.title("Heatmap – níveis por município", fontsize=13, fontweight="bold")
for i in range(pivot_heatmap.shape[0]):
    for j in range(pivot_heatmap.shape[1]):
        val = pivot_heatmap.iloc[i,j]
        if val == 1:
            plt.text(j, i, "X", ha="center", va="center", fontsize=10, color="white")
plt.tight_layout()
plt.show()
