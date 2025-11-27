import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================
# PALETA ALFA-EJA (fase 1)
# ============================
cores = {
    "roxo": "#7E57C2",
    "lilas": "#BA68C8",
    "verde": "#4DB6AC",
    "amarelo": "#FFCA28",
    "rosa": "#F06292",
    "ciano": "#4FC3F7"
}

palette = [cores["roxo"], cores["lilas"], cores["verde"], cores["amarelo"], cores["rosa"], cores["ciano"]]

# ============================
# CARREGAR CSV
# ============================
df = pd.read_csv("q8_deficiencias.csv")

df.fillna(0, inplace=True)

# Apenas colunas numéricas
tipos_def = [
    "Deficiência Visual",
    "Deficiência Auditiva",
    "Surdocegueira",
    "Deficiência Física",
    "Deficiência Intelectual",
    "Transtorno do Espectro Autista",
    "Transtorno de Déficit de Atenção e Hiperatividade"
]

# ======================================================
# 1) GRÁFICO DE BARRAS EMPILHADAS POR MUNICÍPIO
# ======================================================
df.set_index("Municipio")[tipos_def].plot(
    kind="bar",
    stacked=True,
    figsize=(18, 8),
    color=palette
)

plt.title("Alunos da EJA com Deficiência por Município (2025)")
plt.ylabel("Quantidade")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# ======================================================
# 2) GRÁFICO HORIZONTAL (stacked)
# ======================================================
df.set_index("Municipio")[tipos_def].plot(
    kind="barh",
    stacked=True,
    figsize=(12, 10),
    color=palette
)

plt.title("Distribuição de Alunos com Deficiência — Municípios (2025)")
plt.xlabel("Quantidade")
plt.tight_layout()
plt.show()

# ======================================================
# 3) GRÁFICO TOTAL POR TIPO DE DEFICIÊNCIA
# ======================================================
totais = df[tipos_def].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
totais.plot(kind="bar", color=palette)
plt.title("Total de Alunos por Tipo de Deficiência (2025)")
plt.ylabel("Quantidade")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# ======================================================
# 5) PIZZA — Distribuição geral
# ======================================================
plt.figure(figsize=(10, 10))
plt.pie(
    totais,
    labels=totais.index,
    autopct="%1.1f%%",
    colors=palette,
    startangle=140
)
plt.title("Distribuição Geral dos Tipos de Deficiência (2025)")
plt.tight_layout()
plt.show()
