import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ================================
# PALETA ALFA-EJA
# ================================
ROXO_ESCURO = "#651B73"
LILAS       = "#8E2BAF"
VERDE_AGUA  = "#1CB9A3"
AMARELO     = "#FDB913"
ROSA        = "#E62270"
AZUL_CIANO  = "#008BBC"

# ================================
# CARREGAR BASE
# ================================
df = pd.read_csv("q11_jornada.csv")

df.set_index("Municipio", inplace=True)

# ================================
# 1) BARRAS LADO A LADO
# ================================
plt.figure(figsize=(14,6))
df.plot(kind="bar", figsize=(14,6), color=[ROXO_ESCURO, VERDE_AGUA, AMARELO])
plt.title("Jornada Semanal de Trabalho (Gestores / Educadores / Apoio)")
plt.ylabel("Horas por Semana")
plt.xticks(rotation=45, ha="right")
plt.legend(["Gestores", "Educadores", "Equipe de Apoio"])
plt.tight_layout()
plt.show()

# ================================
# 2) BARRAS EMPILHADAS
# ================================
df.plot(kind="bar", stacked=True, figsize=(14,6),
        color=[ROXO_ESCURO, VERDE_AGUA, AMARELO])
plt.title("Jornada Semanal - Distribuição por Município (Empilhado)")
plt.ylabel("Horas")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# ================================
# 3) MÉDIA GERAL (por categoria)
# ================================
plt.figure(figsize=(8,5))
df.mean().plot(kind="bar", color=[ROXO_ESCURO, VERDE_AGUA, AMARELO])
plt.title("Média Geral da Jornada Semanal por Categoria")
plt.ylabel("Horas Semanais")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ================================
# 4) HEATMAP
# ================================
plt.figure(figsize=(12,7))
sns.heatmap(df, annot=True, cmap="Purples", fmt=".0f")
plt.title("Heatmap - Jornada Semanal por Município e Categoria")
plt.tight_layout()
plt.show()


# ================================
# 6) RANKING GERAL (soma das horas)
# ================================
df["Total"] = df.sum(axis=1)

plt.figure(figsize=(12,6))
df["Total"].sort_values(ascending=False).plot(
    kind="bar", color=ROSA
)
plt.title("Ranking — Municípios com Maior Jornada Total de Trabalho (2025)")
plt.ylabel("Horas / Semana (Somatório de categorias)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
