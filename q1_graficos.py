import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  PALETA ALFA-EJA
ROXO_ESCURO = "#651B73"
LILAS       = "#8E2BAF"
VERDE_AGUA  = "#1CB9A3"
AMARELO     = "#FDB913"
ROSA        = "#E62270"
AZUL_CIANO  = "#008BBC"
CINZA_CLARO = "#F2F2F2"


df = pd.read_csv("q1_dados.csv")

df["Ano"] = df["Ano"].astype(int)
df["Matriculados"] = df["Matriculados"].astype(int)
df["Evadidos"] = df["Evadidos"].astype(int)

# Taxa de evasão por linha
df["TaxaEvasao"] = np.where(
    df["Matriculados"] > 0,
    df["Evadidos"] / df["Matriculados"] * 100,
    0
)

# Totais gerais por ano
tot_ano = df.groupby("Ano").agg(
    Matriculados=("Matriculados", "sum"),
    Evadidos=("Evadidos", "sum")
).reset_index()
tot_ano["TaxaEvasao"] = tot_ano["Evadidos"] / tot_ano["Matriculados"] * 100

# Totais por município + ano
tot_mun_ano = df.groupby(["Municipio", "Ano"]).agg(
    Matriculados=("Matriculados", "sum"),
    Evadidos=("Evadidos", "sum")
).reset_index()

# Totais por situação (etapa) + ano
tot_sit_ano = df.groupby(["Situacao", "Ano"]).agg(
    Matriculados=("Matriculados", "sum"),
    Evadidos=("Evadidos", "sum")
).reset_index()
tot_sit = df.groupby("Situacao").agg(
    Matriculados=("Matriculados", "sum"),
    Evadidos=("Evadidos", "sum")
).reset_index()
tot_sit["TaxaEvasao"] = tot_sit["Evadidos"] / tot_sit["Matriculados"] * 100

# Totais por município (somando os anos)
tot_mun = df.groupby("Municipio").agg(
    Matriculados=("Matriculados", "sum"),
    Evadidos=("Evadidos", "sum")
).reset_index()
tot_mun["TaxaEvasao"] = np.where(
    tot_mun["Matriculados"] > 0,
    tot_mun["Evadidos"] / tot_mun["Matriculados"] * 100,
    0
)

#  REGIÕES DOS MUNICÍPIOS
map_regiao = {
    # Região Norte
    "Oiapoque": "Norte",
    "Carauari": "Norte",
    "Coari": "Norte",
    "Belém": "Norte",

    # Região Nordeste I
    "Caucaia": "Nordeste I",
    "Fortaleza": "Nordeste I",
    "Icapuí": "Nordeste I",
    "Alto do Rodrigues": "Nordeste I",

    # Região Nordeste II
    "Araçás": "Nordeste II",
    "São Francisco do Conde": "Nordeste II",
    "Conde": "Nordeste II",
    "Ipojuca": "Nordeste II",
    "Cabo de Santo Agostinho": "Nordeste II",
    "Brejo Grande": "Nordeste II",
    "Santa Luzia do Itanhy": "Nordeste II",
}

df["Regiao"] = df["Municipio"].map(map_regiao)

# Totais por região e ano
tot_reg_ano = df.groupby(["Regiao", "Ano"]).agg(
    Matriculados=("Matriculados", "sum"),
    Evadidos=("Evadidos", "sum")
).reset_index()

tot_reg_ano["TaxaEvasao"] = np.where(
    tot_reg_ano["Matriculados"] > 0,
    tot_reg_ano["Evadidos"] / tot_reg_ano["Matriculados"] * 100,
    0
)

# Totais por região (soma 2022–2024)
tot_reg = df.groupby("Regiao").agg(
    Matriculados=("Matriculados", "sum"),
    Evadidos=("Evadidos", "sum")
).reset_index()

tot_reg["TaxaEvasao"] = np.where(
    tot_reg["Matriculados"] > 0,
    tot_reg["Evadidos"] / tot_reg["Matriculados"] * 100,
    0
)

regioes = tot_reg["Regiao"].dropna().unique()
anos = sorted(df["Ano"].unique())


# ===========================================================
#  GRÁFICO 1 – Linhas: Matriculados e Evadidos por ano
# ===========================================================
plt.figure(figsize=(8, 5))
plt.plot(tot_ano["Ano"], tot_ano["Matriculados"],
         marker="o", linewidth=2, color=AZUL_CIANO, label="Matriculados")
plt.plot(tot_ano["Ano"], tot_ano["Evadidos"],
         marker="o", linewidth=2, color=ROSA, label="Evadidos")
plt.title("Educandos matriculados e evadidos por ano (total geral)", fontsize=13, fontweight="bold")
plt.xlabel("Ano")
plt.ylabel("Número de educandos")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# ===========================================================
#  GRÁFICO 2 – Barras agrupadas: Matriculados x Evadidos por ano
# ===========================================================
x = np.arange(len(tot_ano["Ano"]))
largura = 0.35

plt.figure(figsize=(8, 5))
plt.bar(x - largura/2, tot_ano["Matriculados"], width=largura,
        color=AZUL_CIANO, label="Matriculados")
plt.bar(x + largura/2, tot_ano["Evadidos"], width=largura,
        color=ROSA, label="Evadidos")

plt.xticks(x, tot_ano["Ano"])
plt.title("Matriculados x Evadidos por ano (barras agrupadas)", fontsize=13, fontweight="bold")
plt.xlabel("Ano")
plt.ylabel("Número de educandos")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# ===========================================================
#  GRÁFICO 3 – Barras empilhadas: Matriculados x Evadidos por ano
# ===========================================================
plt.figure(figsize=(8, 5))
plt.bar(tot_ano["Ano"], tot_ano["Matriculados"],
        color=AZUL_CIANO, label="Matriculados")
plt.bar(tot_ano["Ano"], tot_ano["Evadidos"],
        bottom=tot_ano["Matriculados"],
        color=ROSA, label="Evadidos")

plt.title("Distribuição de matriculados e evadidos por ano (empilhado)", fontsize=13, fontweight="bold")
plt.xlabel("Ano")
plt.ylabel("Total de educandos")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# ===========================================================
#  GRÁFICO 4 – Linha: Taxa de evasão geral por ano
# ===========================================================
plt.figure(figsize=(8, 5))
plt.plot(tot_ano["Ano"], tot_ano["TaxaEvasao"],
         marker="o", linewidth=2, color=VERDE_AGUA)
plt.title("Taxa de evasão geral por ano (%)", fontsize=13, fontweight="bold")
plt.xlabel("Ano")
plt.ylabel("Taxa de evasão (%)")
plt.grid(alpha=0.3)
for x_val, y_val in zip(tot_ano["Ano"], tot_ano["TaxaEvasao"]):
    plt.text(x_val, y_val + 0.3, f"{y_val:.1f}%", ha="center", fontsize=9)
plt.tight_layout()
plt.show()

# ===========================================================
#  GRÁFICO 5 – Barras agrupadas por município e ano (Matriculados)
# ===========================================================
municipios = tot_mun_ano["Municipio"].unique()
anos = sorted(tot_mun_ano["Ano"].unique())
n_anos = len(anos)
largura = 0.8 / n_anos  # largura de cada barra dentro do grupo

plt.figure(figsize=(14, 6))
for i, ano in enumerate(anos):
    subset = tot_mun_ano[tot_mun_ano["Ano"] == ano]
    # garante mesma ordem de municípios
    subset = subset.set_index("Municipio").reindex(municipios).reset_index()
    pos = np.arange(len(municipios)) + (i - n_anos/2) * largura + largura/2
    cor = [AZUL_CIANO, ROSA, AMARELO][i % 3]
    plt.bar(pos, subset["Matriculados"], width=largura,
            label=str(ano), color=cor)

plt.xticks(np.arange(len(municipios)), municipios, rotation=45, ha="right")
plt.title("Educandos matriculados por município e ano", fontsize=13, fontweight="bold")
plt.ylabel("Número de educandos")
plt.legend(title="Ano")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# ===========================================================
#  GRÁFICO 6 – Barras agrupadas por município e ano (Evadidos)
# ===========================================================
plt.figure(figsize=(14, 6))
for i, ano in enumerate(anos):
    subset = tot_mun_ano[tot_mun_ano["Ano"] == ano]
    subset = subset.set_index("Municipio").reindex(municipios).reset_index()
    pos = np.arange(len(municipios)) + (i - n_anos/2) * largura + largura/2
    cor = [ROXO_ESCURO, LILAS, VERDE_AGUA][i % 3]
    plt.bar(pos, subset["Evadidos"], width=largura,
            label=str(ano), color=cor)

plt.xticks(np.arange(len(municipios)), municipios, rotation=45, ha="right")
plt.title("Educandos evadidos por município e ano", fontsize=13, fontweight="bold")
plt.ylabel("Número de educandos")
plt.legend(title="Ano")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# ===========================================================
#  GRÁFICO 7 – Heatmap de matriculados por município e ano
# ===========================================================
pivot_mat = tot_mun_ano.pivot(index="Municipio", columns="Ano", values="Matriculados").fillna(0)

plt.figure(figsize=(10, 6))
plt.imshow(pivot_mat, aspect="auto", cmap="Blues")
plt.colorbar(label="Matriculados")
plt.xticks(range(len(anos)), anos)
plt.yticks(range(len(pivot_mat.index)), pivot_mat.index)
plt.title("Heatmap de matriculados por município e ano", fontsize=13, fontweight="bold")

for i in range(pivot_mat.shape[0]):
    for j in range(pivot_mat.shape[1]):
        valor = int(pivot_mat.iloc[i, j])
        plt.text(j, i, str(valor), ha="center", va="center", fontsize=8)

plt.tight_layout()
plt.show()

# ===========================================================
#  GRÁFICO 8 – Heatmap de taxa de evasão por município (média 2022–2024)
# ===========================================================
pivot_taxa = tot_mun.set_index("Municipio")[["TaxaEvasao"]]

plt.figure(figsize=(6, 6))
plt.imshow(pivot_taxa.values, aspect="auto", cmap="PuRd")
plt.colorbar(label="Taxa de evasão (%)")
plt.yticks(range(len(pivot_taxa.index)), pivot_taxa.index)
plt.xticks([0], ["Taxa média 2022–2024"])
plt.title("Heatmap – taxa média de evasão por município", fontsize=13, fontweight="bold")

for i in range(pivot_taxa.shape[0]):
    valor = pivot_taxa["TaxaEvasao"].iloc[i]
    plt.text(0, i, f"{valor:.1f}%", ha="center", va="center", fontsize=8, color="white")
plt.tight_layout()
plt.show()

# ===========================================================
#  GRÁFICO 9 – Barras horizontais: Top 5 municípios em matriculados
# ===========================================================
top5_matriculados = tot_mun.sort_values("Matriculados", ascending=False).head(5)

plt.figure(figsize=(8, 5))
plt.barh(top5_matriculados["Municipio"], top5_matriculados["Matriculados"],
         color=AZUL_CIANO)
plt.title("Top 5 municípios com mais matriculados (2022–2024)", fontsize=13, fontweight="bold")
plt.xlabel("Total de matriculados")
plt.gca().invert_yaxis()
for i, v in enumerate(top5_matriculados["Matriculados"]):
    plt.text(v + (max(top5_matriculados["Matriculados"])*0.01),
             i, str(v), va="center", fontsize=9)
plt.tight_layout()
plt.show()

# ===========================================================
#  GRÁFICO 10 – Barras horizontais: Top 5 municípios em taxa de evasão
#  (considerando apenas quem tem pelo menos 100 matrículas no período)
# ===========================================================
filtro = tot_mun[tot_mun["Matriculados"] >= 100]
top5_taxa = filtro.sort_values("TaxaEvasao", ascending=False).head(5)

plt.figure(figsize=(8, 5))
plt.barh(top5_taxa["Municipio"], top5_taxa["TaxaEvasao"], color=ROSA)
plt.title("Top 5 municípios com maior taxa de evasão", fontsize=13, fontweight="bold")
plt.xlabel("Taxa de evasão (%)")
plt.gca().invert_yaxis()
for i, v in enumerate(top5_taxa["TaxaEvasao"]):
    plt.text(v + 0.3, i, f"{v:.1f}%", va="center", fontsize=9)
plt.tight_layout()
plt.show()

# ===========================================================
#  GRÁFICO 11 – Barras empilhadas por situação (etapa) – Matriculados x Evadidos
# ===========================================================
plt.figure(figsize=(7, 5))
plt.bar(tot_sit["Situacao"], tot_sit["Matriculados"], color=AZUL_CIANO, label="Matriculados")
plt.bar(tot_sit["Situacao"], tot_sit["Evadidos"],
        bottom=tot_sit["Matriculados"], color=ROSA, label="Evadidos")
plt.xticks(rotation=20, ha="right")
plt.title("Distribuição de matriculados e evadidos por etapa (soma 2022–2024)", fontsize=13, fontweight="bold")
plt.ylabel("Número de educandos")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# ===========================================================
#  GRÁFICO 12 – Barras empilhadas por Região (Matriculados x Evadidos, soma 2022–24)
# ===========================================================
plt.figure(figsize=(8, 5))
plt.bar(tot_reg["Regiao"], tot_reg["Matriculados"],
        color=AZUL_CIANO, label="Matriculados")
plt.bar(tot_reg["Regiao"], tot_reg["Evadidos"],
        bottom=tot_reg["Matriculados"],
        color=ROSA, label="Evadidos")

plt.title("Matriculados e evadidos por região (2022–2024)", fontsize=13, fontweight="bold")
plt.ylabel("Número de educandos")
plt.xlabel("Região")
plt.grid(axis="y", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# ===========================================================
#  GRÁFICO 13 – Barras agrupadas por Região e Ano (Matriculados)
# ===========================================================
plt.figure(figsize=(10, 5))

largura = 0.8 / len(anos)
x_base = np.arange(len(regioes))

for i, ano in enumerate(anos):
    sub = tot_reg_ano[tot_reg_ano["Ano"] == ano]
    sub = sub.set_index("Regiao").reindex(regioes).reset_index()
    pos = x_base + (i - len(anos)/2) * largura + largura/2
    cor = [AZUL_CIANO, ROSA, AMARELO][i % 3]
    plt.bar(pos, sub["Matriculados"], width=largura,
            color=cor, label=str(ano))

plt.xticks(x_base, regioes)
plt.title("Matriculados por região e ano", fontsize=13, fontweight="bold")
plt.ylabel("Número de educandos")
plt.xlabel("Região")
plt.grid(axis="y", alpha=0.3)
plt.legend(title="Ano")
plt.tight_layout()
plt.show()

# ===========================================================
#  GRÁFICO 14 – Linha: Taxa de evasão por Região (série temporal)
# ===========================================================
plt.figure(figsize=(10, 5))

cores_regiao = {
    "Norte": AZUL_CIANO,
    "Nordeste I": ROXO_ESCURO,
    "Nordeste II": VERDE_AGUA,
}

for reg in regioes:
    sub = tot_reg_ano[tot_reg_ano["Regiao"] == reg]
    sub = sub.sort_values("Ano")
    plt.plot(sub["Ano"], sub["TaxaEvasao"],
             marker="o",
             linewidth=2,
             color=cores_regiao.get(reg, LILAS),
             label=reg)

plt.title("Taxa de evasão por região e ano (%)", fontsize=13, fontweight="bold")
plt.xlabel("Ano")
plt.ylabel("Taxa de evasão (%)")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
