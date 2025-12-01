import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ================================
# PALETA ALFA-EJA
# ================================
ROXO = "#651B73"
LILAS       = "#8E2BAF"
VERDE  = "#1CB9A3"
AMARELO     = "#FDB913"
ROSA        = "#E62270"
CIANO  = "#008BBC"
cores = [ROXO, VERDE, AMARELO, LILAS, ROSA, CIANO]

# ================================
# 1. CARREGAR BASE
# ================================
df = pd.read_csv("q48_documentos_registros_eja.csv")

# converter Sim/Nao para 1/0
bin_map = {"Sim":1, "Nao":0, "Não":0, "":0, np.nan:0}

doc_cols = [
    "Relatorios_Pedagogicos",
    "Fotos_Turmas",
    "Videos_Historia",
    "Publicacoes_EJA",
    "Depoimentos",
    "PPP_Antigos",
    "Registros_Foruns",
    "Outros"
]

df_bin = df[["Municipio"] + doc_cols].copy()
for col in doc_cols:
    df_bin[col] = df_bin[col].map(bin_map)

df_bin.set_index("Municipio", inplace=True)

# ================================
# 2. TOTAL POR TIPO DE DOCUMENTO
# ================================
totais = df_bin.sum().sort_values(ascending=False)

plt.figure(figsize=(12,6))
totais.plot(kind="bar", color=cores)
plt.title("Disponibilidade de Documentos e Registros Históricos da EJA (por tipo)")
plt.ylabel("Quantidade de Municípios")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()



# ================================
# 4. BARRAS EMPILHADAS
# ================================
df_bin.plot(kind="bar", stacked=True, figsize=(16,7),
            color=cores)
plt.title("Documentos Disponíveis por Município (Empilhado)")
plt.ylabel("Sim (1) / Não (0)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
g