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
# 1. Carregar CSV único
# ============================
df = pd.read_csv("q42_q43_merenda_unificado.csv")

# ============================
# TRATAMENTO PARA A Q43
# ============================

# Classificar respostas
def classificar_43(texto):
    t = texto.lower()
    if "sim" in t and "acredito" not in t:
        return "Sim"
    if "acredito" in t:
        return "Provável"
    return "Não"

df["Categoria_Q43"] = df["Agricultura_Familiar"].apply(classificar_43)

cont43 = df["Categoria_Q43"].value_counts()

# Gráfico de barras Q43
plt.figure(figsize=(6,4))
cont43.plot(kind="bar", color=[VERDE, AMARELO, ROXO])
plt.title("Q43 – 30% da Merenda da Agricultura Familiar")
plt.ylabel("Número de Municípios")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Pizza Q43
plt.figure(figsize=(6,6))
plt.pie(cont43, labels=cont43.index, autopct="%.1f%%",
        colors=[VERDE, AMARELO, ROXO], startangle=90)
plt.title("Distribuição – 30% da Agricultura Familiar")
plt.show()