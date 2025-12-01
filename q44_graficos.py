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
# 1. Carregar CSV
# ============================
df = pd.read_csv("q44_transporte_urbano.csv")

# Padronizar categorias
def classificar(valor):
    v = valor.lower()
    if "sim" in v and "só" not in v:
        return "Sim"
    if "só" in v or "apenas" in v or "parcial" in v:
        return "Parcial"
    return "Não"

df["Categoria"] = df["Situacao"].apply(classificar)

# ============================
# 2. Contagem por Categoria
# ============================
contagem = df["Categoria"].value_counts()

plt.figure(figsize=(7,4))
contagem.plot(kind="bar", color=[VERDE, AMARELO, ROXO])
plt.title("Transporte Escolar para Educandos da EJA – Zona Urbana (Q44)")
plt.ylabel("Quantidade de Municípios")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ============================
# 3. Gráfico de Pizza
# ============================
plt.figure(figsize=(6,6))
plt.pie(contagem, autopct="%1.1f%%", labels=contagem.index,
        colors=[VERDE, AMARELO, ROXO], startangle=90)
plt.title("Distribuição da Garantia de Transporte Escolar – Zona Urbana")
plt.tight_layout()
plt.show()

# ============================
# 4. Heatmap
# ============================
df_bin = pd.DataFrame({
    "Municipio": df["Municipio"],
    "Sim": (df["Categoria"] == "Sim").astype(int),
    "Parcial": (df["Categoria"] == "Parcial").astype(int),
    "Nao": (df["Categoria"] == "Não").astype(int)
}).set_index("Municipio")

plt.figure(figsize=(6,4))
sns.heatmap(df_bin, annot=True, cmap="Purples", cbar=False, fmt="d")
plt.title("Mapa da Garantia de Transporte – Zona Urbana (Q44)")
plt.tight_layout()
plt.show()