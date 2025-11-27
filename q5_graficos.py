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
df = pd.read_csv("q5_escolas_turmas_2025.csv")

df["Total_Escolas"] = df["Escolas_Rural"] + df["Escolas_Urbana"]
df["Total_Turmas"]  = df["Turmas_Rural"]  + df["Turmas_Urbana"]

# Totais gerais por município
tot_mun = df.groupby("Municipio")[["Escolas_Rural","Escolas_Urbana",
                                   "Turmas_Rural","Turmas_Urbana",
                                   "Total_Escolas","Total_Turmas"]].sum()

# Totais gerais por ciclo
tot_ciclo = df.groupby("Ciclo_EJA")[["Escolas_Rural","Escolas_Urbana",
                                     "Turmas_Rural","Turmas_Urbana",
                                     "Total_Escolas","Total_Turmas"]].sum()

# ============================
#  2. GRÁFICO – Total de escolas por município
# ============================
plt.figure(figsize=(12,7))
tot_mun["Total_Escolas"].sort_values().plot(kind="barh", color=AZUL_CIANO)
plt.title("Total de escolas que ofertam EJA em 2025 (por município)", fontsize=14, fontweight="bold")
plt.xlabel("Número de escolas")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.show()

# ============================
#  3. GRÁFICO – Total de turmas por município
# ============================
plt.figure(figsize=(12,7))
tot_mun["Total_Turmas"].sort_values().plot(kind="barh", color=ROSA)
plt.title("Total de turmas da EJA em 2025 (por município)", fontsize=14, fontweight="bold")
plt.xlabel("Número de turmas")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.show()

# ============================
#  4. GRÁFICO – Barras empilhadas (turmas rural/urbana)
# ============================
plt.figure(figsize=(14,7))
x = np.arange(len(tot_mun.index))

plt.bar(x, tot_mun["Turmas_Rural"], color=VERDE_AGUA, label="Turmas Rural")
plt.bar(x, tot_mun["Turmas_Urbana"], bottom=tot_mun["Turmas_Rural"],
        color=ROXO_ESCURO, label="Turmas Urbanas")

plt.xticks(x, tot_mun.index, rotation=45, ha="right")
plt.title("Composição das turmas por zona (2025)", fontsize=14, fontweight="bold")
plt.ylabel("Número de turmas")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# ============================
#  5. GRÁFICO – CIRCULAR (escolas rural x urbana)
# ============================
total_rural  = df["Escolas_Rural"].sum()
total_urbana = df["Escolas_Urbana"].sum()

plt.figure(figsize=(7,7))
plt.pie([total_rural, total_urbana],
        labels=["Rural","Urbana"],
        autopct="%1.1f%%",
        colors=[VERDE_AGUA, ROXO_ESCURO])
plt.title("Distribuição percentual das escolas (2025)", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()


# ============================
#  6. GRÁFICO – Radar (perfil por ciclo)
# ============================
ciclos = tot_ciclo.index.tolist()
valores = tot_ciclo["Total_Turmas"].tolist()

angles = np.linspace(0, 2*np.pi, len(ciclos), endpoint=False).tolist()
angles += angles[:1]
valores += valores[:1]

plt.figure(figsize=(7,7))
ax = plt.subplot(111, polar=True)
ax.plot(angles, valores, linewidth=2, color=AZUL_CIANO)
ax.fill(angles, valores, alpha=0.15, color=AZUL_CIANO)
ax.set_thetagrids(np.degrees(angles[:-1]), ciclos)
plt.title("Perfil de turmas por ciclo da EJA – 2025", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()
