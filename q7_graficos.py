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
# 1. CARREGAR BASE
# ============================
df = pd.read_csv("q7_professores_2025.csv")

# Total por município
tot_mun = df.groupby("Municipio")["Total"].sum().reset_index()

# Pivot para zonas
pivot_zona = df.pivot_table(index="Municipio", columns="Ciclo_EJA",
                            values="Total", aggfunc="sum", fill_value=0)

pivot_urb_rur = df.pivot(index="Municipio", columns="Ciclo_EJA",
                         values=["Urbana","Rural"]).fillna(0)

# Totais por ciclo
tot_ciclo = df.groupby("Ciclo_EJA")["Total"].sum().reset_index()

# ============================
# 2. BARRA HORIZONTAL – TOTAL POR MUNICÍPIO
# ============================
plt.figure(figsize=(12,7))
tot_mun.sort_values("Total").plot(kind="barh", x="Municipio", y="Total",
                                  color=AZUL_CIANO, legend=False)
plt.title("Professores atuando na EJA em 2025 (por município)", fontsize=14, fontweight="bold")
plt.xlabel("Quantidade de professores")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.show()

# ============================
# 3. BARRAS EMPILHADAS – URBANA vs RURAL
# ============================
df_zona = df.groupby("Municipio")[["Urbana","Rural"]].sum()

plt.figure(figsize=(12,7))
x = np.arange(len(df_zona.index))

plt.bar(x, df_zona["Rural"], color=VERDE_AGUA, label="Rural")
plt.bar(x, df_zona["Urbana"], bottom=df_zona["Rural"],
        color=ROXO_ESCURO, label="Urbana")

plt.xticks(x, df_zona.index, rotation=45, ha="right")
plt.title("Composição dos professores por zona (2025)", fontsize=14, fontweight="bold")
plt.ylabel("Quantidade")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# ============================
# 4. BARRAS – TOTAL POR CICLO
# ============================
plt.figure(figsize=(7,5))
plt.bar(tot_ciclo["Ciclo_EJA"], tot_ciclo["Total"],
        color=[ROXO_ESCURO, AZUL_CIANO, AMARELO])
plt.title("Professores por ciclo da EJA (2025)", fontsize=14, fontweight="bold")
plt.ylabel("Quantidade")
for i,v in enumerate(tot_ciclo["Total"]):
    plt.text(i, v+1, str(v), ha="center")
plt.tight_layout()
plt.show()

# ============================
# 5. PIZZA – ZONA URBANA vs RURAL (TOTAL)
# ============================
total_urb = df["Urbana"].sum()
total_rur = df["Rural"].sum()

plt.figure(figsize=(7,7))
plt.pie([total_urb, total_rur], labels=["Urbana","Rural"],
        autopct="%1.1f%%",
        colors=[ROXO_ESCURO, VERDE_AGUA])
plt.title("Distribuição dos professores por zona – 2025", fontsize=14, fontweight="bold")
plt.show()

# ============================
# 6. HEATMAP – MUNICÍPIO x CICLO
# ============================
plt.figure(figsize=(12,7))
plt.imshow(pivot_zona, cmap="Purples", aspect="auto")
plt.colorbar(label="Quantidade")

plt.xticks(range(len(pivot_zona.columns)), pivot_zona.columns, rotation=20)
plt.yticks(range(len(pivot_zona.index)), pivot_zona.index)

plt.title("Heatmap – professores por município e ciclo (2025)", fontsize=14, fontweight="bold")

for i in range(pivot_zona.shape[0]):
    for j in range(pivot_zona.shape[1]):
        val = pivot_zona.iloc[i,j]
        plt.text(j, i, str(int(val)), ha="center",
                 va="center", color="white" if val>40 else "black")

plt.tight_layout()
plt.show()

# ============================
# 7. RADAR – PERFIL POR MUNICÍPIO
# ============================
vals = tot_mun["Total"].tolist()
municipios = tot_mun["Municipio"].tolist()

angles = np.linspace(0, 2*np.pi, len(vals), endpoint=False)
vals = vals + vals[:1]
angles = np.append(angles, angles[0])

plt.figure(figsize=(10,10))
ax = plt.subplot(111, polar=True)

ax.plot(angles, vals, linewidth=2, color=AZUL_CIANO)
ax.fill(angles, vals, alpha=0.15, color=AZUL_CIANO)

ax.set_thetagrids(np.degrees(angles[:-1]), municipios)
plt.title("Radar – quantidade de professores por município (2025)", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()
