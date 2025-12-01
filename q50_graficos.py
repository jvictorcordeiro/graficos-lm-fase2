import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================
# PALETA ALFA-EJA
# ============================
ROXO_ESCURO = "#651B73"
LILAS       = "#8E2BAF"
VERDE_AGUA  = "#1CB9A3"
AMARELO     = "#FDB913"
ROSA        = "#E62270"
AZUL_CIANO  = "#008BBC"
cores=[ROXO_ESCURO,VERDE_AGUA,AMARELO,LILAS,ROSA,AZUL_CIANO]

# ============================
# 1. CARREGAR BASE
# ============================
df = pd.read_csv("q50_materiais.csv")

# Converter Sim/Nao para 1/0
bin_map={"Sim":1,"Nao":0}
for col in df.columns[1:]:
    df[col+"_bin"]=df[col].map(bin_map)

bin_cols=[c for c in df.columns if c.endswith("_bin")]

df_bin=df[ ["Municipio"]+bin_cols ].set_index("Municipio")
df_bin.columns=[
    "Proposta Curricular",
    "Cadernos de Formação",
    "Documentos MEC",
    "Materiais de Fóruns/Encontros",
    "Publicações Locais",
    "Outros"
]

# ============================
# 2. TOTAL POR TIPO DE MATERIAL
# ============================
totais=df_bin.sum().sort_values(ascending=False)

plt.figure(figsize=(12,6))
totais.plot(kind="bar", color=cores)
plt.title("Disponibilidade de Materiais de Formação e Referência (Total por Tipo)")
plt.ylabel("Quantidade de Municípios")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# ============================
# 4. BARRAS EMPILHADAS POR MUNICÍPIO
# ============================
df_bin.plot(kind="bar", stacked=True, figsize=(16,7),
            color=cores)
plt.title("Materiais Disponíveis por Município (Empilhado)")
plt.ylabel("Sim (1) / Não (0)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
