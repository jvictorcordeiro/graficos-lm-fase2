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
#  1. CARREGAR DADOS Q4
# ============================
df = pd.read_csv("q4_profissionais.csv")

# total por município
df["Total"] = df[["Coordenador", "Supervisor", "Orientador", "Outros"]].sum(axis=1)

# totais gerais
tot_geral = df[["Coordenador","Supervisor","Orientador","Outros"]].sum()

# ============================
#  2. REGIÕES
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

tot_regiao = df.groupby("Regiao")[["Coordenador","Supervisor","Orientador","Outros","Total"]].sum().reset_index()

# ============================
#  3. GRÁFICOS
# ============================

# 3.1 Barras horizontais – total por município
df_ord = df.sort_values("Total", ascending=True)

plt.figure(figsize=(10,7))
plt.barh(df_ord["Municipio"], df_ord["Total"], color=AZUL_CIANO)
plt.title("Total de profissionais da equipe pedagógica da EJA por município", fontsize=13, fontweight="bold")
plt.xlabel("Total de profissionais")
for i, v in enumerate(df_ord["Total"]):
    plt.text(v + 0.2, i, str(v), va="center", fontsize=9)
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.show()

# 3.2 Barras empilhadas – composição por município
plt.figure(figsize=(12,7))
x = np.arange(len(df["Municipio"]))

plt.bar(x, df["Coordenador"], color=ROXO_ESCURO, label="Coordenador(a)")
plt.bar(x, df["Supervisor"], bottom=df["Coordenador"], color=LILAS, label="Supervisor(a)")
plt.bar(x, df["Orientador"], bottom=df["Coordenador"] + df["Supervisor"], color=AZUL_CIANO, label="Orientador(a)")
plt.bar(x, df["Outros"], bottom=df["Coordenador"] + df["Supervisor"] + df["Orientador"], color=VERDE_AGUA, label="Outros")

plt.xticks(x, df["Municipio"], rotation=45, ha="right")
plt.title("Composição da equipe pedagógica por município", fontsize=13, fontweight="bold")
plt.ylabel("Número de profissionais")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# 3.3 Barras verticais – totais por cargo
plt.figure(figsize=(7,5))
plt.bar(["Coordenador","Supervisor","Orientador","Outros"],
        tot_geral.values,
        color=[ROXO_ESCURO, LILAS, AZUL_CIANO, VERDE_AGUA])
plt.title("Total de profissionais por cargo (EJA/SME)", fontsize=13, fontweight="bold")
plt.ylabel("Quantidade")
for i, v in enumerate(tot_geral.values):
    plt.text(i, v + 0.5, str(v), ha="center", fontsize=10)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# 3.4 Pizza – distribuição por cargo
plt.figure(figsize=(7,7))
plt.pie(tot_geral.values, labels=tot_geral.index,
        autopct="%1.1f%%",
        colors=[ROXO_ESCURO, LILAS, AZUL_CIANO, VERDE_AGUA],
        wedgeprops={"linewidth":1, "edgecolor":"white"})
plt.title("Distribuição percentual dos profissionais da equipe pedagógica", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.show()

# 3.5 Barras agrupadas – cargos por região
regioes = tot_regiao["Regiao"].dropna().tolist()
ind = np.arange(len(regioes))
largura = 0.2

plt.figure(figsize=(10,6))
plt.bar(ind - largura*1.5, tot_regiao["Coordenador"], width=largura, color=ROXO_ESCURO, label="Coordenador")
plt.bar(ind - largura/2, tot_regiao["Supervisor"], width=largura, color=LILAS, label="Supervisor")
plt.bar(ind + largura/2, tot_regiao["Orientador"], width=largura, color=AZUL_CIANO, label="Orientador")
plt.bar(ind + largura*1.5, tot_regiao["Outros"], width=largura, color=VERDE_AGUA, label="Outros")

plt.xticks(ind, regioes)
plt.title("Profissionais da EJA por região e por cargo", fontsize=13, fontweight="bold")
plt.ylabel("Quantidade")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# 3.7 Radar – perfil médio por região
categorias = ["Coordenador","Supervisor","Orientador","Outros"]
N = len(categorias)
angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
angles += angles[:1]

plt.figure(figsize=(8,8))
ax = plt.subplot(111, polar=True)

cores_regiao = {"Norte": AZUL_CIANO, "Nordeste I": ROXO_ESCURO, "Nordeste II": VERDE_AGUA}

for _, row in tot_regiao.dropna(subset=["Regiao"]).iterrows():
    valores = [row[c] for c in categorias]
    valores += valores[:1]
    ax.plot(angles, valores, linewidth=2, label=row["Regiao"], color=cores_regiao.get(row["Regiao"], ROXO_ESCURO))
    ax.fill(angles, valores, alpha=0.1, color=cores_regiao.get(row["Regiao"], ROXO_ESCURO))

ax.set_xticks(angles[:-1])
ax.set_xticklabels(["Coord.","Super.","Orient.","Outros"])
plt.title("Perfil de profissionais da EJA por região", fontsize=13, fontweight="bold")
plt.legend(loc="upper right", bbox_to_anchor=(1.2, 1.1))
plt.tight_layout()
plt.show()
