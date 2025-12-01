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
df = pd.read_csv("q46_origem_professores.csv")

# Criar categorias
def classificar(origem):
    texto = str(origem).lower()
    if "própria" in texto or "comunidade" in texto:
        return "Da própria comunidade"
    if "outro" in texto:
        return "De outro lugar"
    return "Indefinido"

df["Categoria"] = df["Origem"].apply(classificar)

# ============================
# 2. CONTAGEM POR CATEGORIA
# ============================
contagem = df["Categoria"].value_counts()

plt.figure(figsize=(7,4))
contagem.plot(kind="bar", color=[ROXO, VERDE, CINZA] if len(contagem) > 2 else [ROXO, VERDE])
plt.title("Origem dos Professores da EJA (Q46)")
plt.ylabel("Quantidade de Municípios")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ============================
# 3. GRÁFICO DE PIZZA
# ============================
plt.figure(figsize=(6,6))
plt.pie(contagem,
        labels=contagem.index,
        autopct="%1.1f%%",
        colors=[ROXO, VERDE, CINZA] if len(contagem) > 2 else [ROXO, VERDE],
        startangle=90)
plt.title("Distribuição da Origem dos Professores da EJA")
plt.tight_layout()
plt.show()

# ============================
# 4. HEATMAP BINÁRIO
# ============================
df_bin = pd.DataFrame({
    "Municipio": df["Municipio"],
    "Propria_Comunidade": df["Categoria"].eq("Da própria comunidade").astype(int),
    "Outro_Lugar": df["Categoria"].eq("De outro lugar").astype(int)
}).set_index("Municipio")

plt.figure(figsize=(6,3))
sns.heatmap(df_bin, annot=True, cmap="Purples", cbar=False, fmt="d")
plt.title("Mapa de Origem dos Professores da EJA")
plt.ylabel("")
plt.tight_layout()
plt.show()

