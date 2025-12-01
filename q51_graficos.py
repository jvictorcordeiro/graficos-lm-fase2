import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================
# PALETA ALFA-EJA
# ============================
ROXO_ESCURO = "#651B73"
LILAS       = "#8E2BAF"
VERDE_AGUA  = "#1CB9A3"
AMARELO     = "#FDB913"
ROSA        = "#E62270"
AZUL_CIANO  = "#008BBC"

# ============================
# 1. CARREGAR DADOS
# ============================
df = pd.read_csv("q51_creja.csv")

# mapear Sim/Não/Não informado para 1/0/NaN
map_bin = {"Sim": 1, "Nao": 0, "Não": 0, "Não informado": np.nan}

bin_cols = ["Autoriza_uso", "Interesse_participar", "Equipe_tecnica"]
for c in bin_cols:
    df[c + "_bin"] = df[c].map(map_bin)

# ============================
# 2. TOTAL DE MUNICÍPIOS QUE RESPONDERAM "SIM"
# ============================
tot_sim = df[[c + "_bin" for c in bin_cols]].sum()
tot_sim.index = ["Autoriza uso", "Interesse em participar", "Possui equipe técnica"]

plt.figure(figsize=(8,5))
plt.bar(tot_sim.index, tot_sim.values,
        color=[ROXO_ESCURO, AZUL_CIANO, VERDE_AGUA])
plt.title("Municípios com resposta 'Sim' para cada aspecto do CREJA")
plt.ylabel("Quantidade de municípios")
plt.xticks(rotation=15, ha="right")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# ============================
# 4. DESAFIOS – CONTAGEM SIMPLES (materiais x equipe)
# ============================
df["Falta_materiais"] = df["Desafios"].str.contains("materiais", case=False, na=False)
df["Falta_equipe"]    = df["Desafios"].str.contains("equipe", case=False, na=False)

desafios_tot = pd.Series({
    "Falta de materiais": df["Falta_materiais"].sum(),
    "Falta de equipe": df["Falta_equipe"].sum()
})

plt.figure(figsize=(6,5))
plt.bar(desafios_tot.index, desafios_tot.values,
        color=[AMARELO, ROSA])
plt.title("Principais desafios citados para colaborar com o CREJA")
plt.ylabel("Número de municípios")
plt.tight_layout()
plt.show()

# ============================
# 5. BARRAS EMPILHADAS – PERFIL POR MUNICÍPIO
# ============================
stack = heat.copy()

plt.figure(figsize=(12,6))
stack.plot(kind="bar", stacked=True,
           color=[ROXO_ESCURO, AZUL_CIANO, VERDE_AGUA])
plt.title("Perfil de colaboração com o CREJA por município")
plt.ylabel("Sim (1) / Não (0)")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Dimensão")
plt.tight_layout()
plt.show()
