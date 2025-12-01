import pandas as pd
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
CIANO  = "#008BBC"

# ============================
# 1. CARREGAR CSV
# ============================
df = pd.read_csv("q45_transporte_escolar.csv")

# Padronizar categorias
mapping = {
    "Sim": "Sim",
    "Nao": "Não",
    "Parcial": "Parcial"
}
df["Categoria"] = df["Situacao"].map(mapping)

# ============================
# 2. CONTAGEM POR CATEGORIA
# ============================
contagem = df["Categoria"].value_counts()

plt.figure(figsize=(7,4))
contagem.plot(kind="bar", color=[VERDE, ROXO, AMARELO])
plt.title("Garantia de Transporte Escolar para Educandos da EJA – Zona Rural (Q45)")
plt.ylabel("Quantidade de Municípios")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ============================
# 3. GRÁFICO DE PIZZA
# ============================
plt.figure(figsize=(6,6))
plt.pie(contagem, autopct="%1.1f%%", labels=contagem.index,
        colors=[VERDE, ROXO, AMARELO], startangle=90)
plt.title("Distribuição da Garantia de Transporte Escolar")
plt.tight_layout()
plt.show()

# ============================
# 4. HEATMAP BINÁRIO
# ============================
df_bin = pd.DataFrame({
    "Municipio": df["Municipio"],
    "Sim": (df["Categoria"] == "Sim").astype(int),
    "Nao": (df["Categoria"] == "Não").astype(int),
    "Parcial": (df["Categoria"] == "Parcial").astype(int)
}).set_index("Municipio")

plt.figure(figsize=(6,4))
sns.heatmap(df_bin, annot=True, cmap="Purples", cbar=False, fmt="d")
plt.title("Mapa da Garantia de Transporte Escolar")
plt.tight_layout()
plt.show()