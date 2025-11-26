import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================
#  PALETA ALFA-EJA
# ============================
ROXO_ESCURO = "#651B73"
LILAS       = "#8E2BAF"
VERDE_AGUA  = "#1CB9A3"
AMARELO     = "#FDB913"
ROSA        = "#E62270"
AZUL_CIANO  = "#008BBC"

# ============================
#  1. CARREGAR DADOS 2025
# ============================
df = pd.read_csv("q2_2025.csv")

# Garante tipos numéricos
for col in ["Alfabetizacao", "Anos_Iniciais", "Anos_Finais"]:
    df[col] = df[col].astype(int)

# Total por município em 2025
df["Total_2025"] = df["Alfabetizacao"] + df["Anos_Iniciais"] + df["Anos_Finais"]

# Totais por etapa
tot_etapa = pd.DataFrame({
    "Etapa": ["Alfabetização", "Anos Iniciais", "Anos Finais"],
    "Total": [
        df["Alfabetizacao"].sum(),
        df["Anos_Iniciais"].sum(),
        df["Anos_Finais"].sum()
    ]
})

total_geral_2025 = df["Total_2025"].sum()
print(f"Total geral de educandos na EJA em 2025: {total_geral_2025}")

# ============================
#  2. REGIÕES DOS MUNICÍPIOS
# ============================
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

tot_reg_etapa = df.groupby("Regiao").agg(
    Alfabetizacao=("Alfabetizacao", "sum"),
    Anos_Iniciais=("Anos_Iniciais", "sum"),
    Anos_Finais=("Anos_Finais", "sum"),
    Total_2025=("Total_2025", "sum"),
).reset_index()

# ============================
#  3. GRÁFICO 1 – Barras horizontais:
#     Total por município (ordenado)
# ============================
df_ord = df.sort_values("Total_2025", ascending=True)

plt.figure(figsize=(10, 6))
plt.barh(df_ord["Municipio"], df_ord["Total_2025"], color=AZUL_CIANO)
plt.title("Educandos matriculados na EJA em 2025 por município", fontsize=13, fontweight="bold")
plt.xlabel("Total de educandos em 2025")
plt.ylabel("Município")

for i, v in enumerate(df_ord["Total_2025"]):
    plt.text(v + (df_ord["Total_2025"].max() * 0.01), i, str(v),
             va="center", fontsize=9)

plt.tight_layout()
plt.show()

# ============================
#  4. GRÁFICO 2 – Barras empilhadas:
#     composição por etapa em cada município
# ============================
plt.figure(figsize=(12, 6))
x = np.arange(len(df["Municipio"]))

plt.bar(x, df["Alfabetizacao"], color=ROXO_ESCURO, label="Alfabetização")
plt.bar(x, df["Anos_Iniciais"], bottom=df["Alfabetizacao"],
        color=AZUL_CIANO, label="Anos Iniciais (1ª Etapa)")
plt.bar(x, df["Anos_Finais"],
        bottom=df["Alfabetizacao"] + df["Anos_Iniciais"],
        color=AMARELO, label="Anos Finais (2ª Etapa)")

plt.xticks(x, df["Municipio"], rotation=45, ha="right")
plt.title("Composição dos matriculados por etapa em cada município (2025)", fontsize=13, fontweight="bold")
plt.ylabel("Número de educandos")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# ============================
#  5. GRÁFICO 3 – Barras por etapa
# ============================
plt.figure(figsize=(6, 5))
cores_etapas = [ROXO_ESCURO, AZUL_CIANO, AMARELO]
plt.bar(tot_etapa["Etapa"], tot_etapa["Total"], color=cores_etapas)
plt.title("Total de matriculados na EJA em 2025 por etapa", fontsize=13, fontweight="bold")
plt.ylabel("Número de educandos")
for i, v in enumerate(tot_etapa["Total"]):
    plt.text(i, v + (tot_etapa["Total"].max()*0.01), str(v),
             ha="center", fontsize=10)
plt.tight_layout()
plt.show()

# ============================
#  6. GRÁFICO 4 – Pizza / Donut por etapa
# ============================
plt.figure(figsize=(6, 6))
valores = tot_etapa["Total"]
labels = tot_etapa["Etapa"]
colors = cores_etapas

wedges, texts, autotexts = plt.pie(
    valores,
    labels=labels,
    autopct=lambda p: f"{p:.1f}%\n({int(p*total_geral_2025/100):d})",
    startangle=90,
    colors=colors,
    textprops={"fontsize": 9}
)

centre_circle = plt.Circle((0, 0), 0.60, fc="white")
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Distribuição percentual dos matriculados por etapa – 2025", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.show()

# ============================
#  7. GRÁFICO 5 – Barras agrupadas por região e etapa
# ============================
regioes = tot_reg_etapa["Regiao"].dropna().tolist()
ind = np.arange(len(regioes))
largura = 0.2

plt.figure(figsize=(9, 6))

plt.bar(ind - largura, tot_reg_etapa["Alfabetizacao"],
        width=largura, color=ROXO_ESCURO, label="Alfabetização")
plt.bar(ind, tot_reg_etapa["Anos_Iniciais"],
        width=largura, color=AZUL_CIANO, label="Anos Iniciais")
plt.bar(ind + largura, tot_reg_etapa["Anos_Finais"],
        width=largura, color=AMARELO, label="Anos Finais")

plt.xticks(ind, regioes)
plt.title("Matriculados na EJA em 2025 por região e etapa", fontsize=13, fontweight="bold")
plt.ylabel("Número de educandos")
plt.xlabel("Região")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# ============================
#  8. GRÁFICO 6 – Heatmap município x etapa
# ============================
pivot = df.set_index("Municipio")[["Alfabetizacao", "Anos_Iniciais", "Anos_Finais"]]

plt.figure(figsize=(9, 6))
plt.imshow(pivot.values, aspect="auto", cmap="Blues")
plt.colorbar(label="Matriculados (2025)")

plt.xticks(np.arange(3), ["Alfabetização", "Anos Iniciais", "Anos Finais"], rotation=20)
plt.yticks(np.arange(len(pivot.index)), pivot.index)

plt.title("Heatmap – matriculados por município e etapa (2025)", fontsize=13, fontweight="bold")

for i in range(pivot.shape[0]):
    for j in range(pivot.shape[1]):
        valor = int(pivot.iloc[i, j])
        plt.text(j, i, str(valor), ha="center", va="center", fontsize=8)

plt.tight_layout()
plt.show()

# ============================
#  9. GRÁFICO 7 – Radar por região (opcional, comparando etapas)
# ============================
tot_reg_radar = tot_reg_etapa.dropna(subset=["Regiao"])
if len(tot_reg_radar) > 0:
    categorias = ["Alfabetizacao", "Anos_Iniciais", "Anos_Finais"]
    labels_cat = ["Alfabetização", "Anos Iniciais", "Anos Finais"]
    N = len(categorias)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]  # fechar o círculo

    plt.figure(figsize=(7, 7))
    ax = plt.subplot(111, polar=True)

    cores_regiao = {
        "Norte": AZUL_CIANO,
        "Nordeste I": ROXO_ESCURO,
        "Nordeste II": VERDE_AGUA,
    }

    for _, row in tot_reg_radar.iterrows():
        valores = [row[c] for c in categorias]
        valores += valores[:1]
        ax.plot(angles, valores,
                linewidth=2,
                label=row["Regiao"],
                color=cores_regiao.get(row["Regiao"], LILAS))
        ax.fill(angles, valores,
                alpha=0.1,
                color=cores_regiao.get(row["Regiao"], LILAS))

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels_cat)
    ax.set_title("Perfil de matriculados por região e etapa – 2025", fontsize=13, fontweight="bold", pad=20)
    ax.set_rlabel_position(0)
    plt.legend(loc="upper right", bbox_to_anchor=(1.2, 1.1))
    plt.tight_layout()
    plt.show()
