import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

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
# CARREGAR DADOS
# ================================
df = pd.read_csv("q10_pacto.csv")

# Converter datas quando houver
df["Data"] = df["Data"].replace("", None)
df["Data_formatada"] = df["Data"].apply(lambda x: datetime.strptime(x, "%d/%m/%Y") if isinstance(x, str) else None)

# ================================
# 1) GRÁFICO DE BARRA (ADERIU)
# ================================
plt.figure(figsize=(8,4))
plt.bar(df["Municipio"], [1,1,1], color=ROXO_ESCURO)
plt.title("Municípios que aderiram ao Pacto pela Alfabetização e Qualificação da EJA (2025)")
plt.ylabel("Aderiu (Sim = 1)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# ================================
# 2) LINHA DO TEMPO (DATA DE ADESÃO)
# ================================
df_com_data = df.dropna(subset=["Data_formatada"])

plt.figure(figsize=(10,4))
plt.scatter(df_com_data["Data_formatada"], df_com_data["Municipio"], s=200, color=VERDE_AGUA)

for _, row in df_com_data.iterrows():
    plt.text(row["Data_formatada"], row["Municipio"], row["Data"], va="bottom", ha="center")

plt.title("Linha do Tempo de Adesão ao Pacto (2025)")
plt.xlabel("Data")
plt.ylabel("Município")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.show()

# ================================
# 3) PIZZA (embora todos sejam "Sim")
# ================================
plt.figure(figsize=(6,6))
plt.pie([len(df)], labels=["100% Aderiram"], autopct="%1.1f%%", colors=[VERDE_AGUA])
plt.title("Percentual de Adesão ao Pacto")
plt.show()
