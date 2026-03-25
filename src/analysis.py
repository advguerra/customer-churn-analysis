# ============================================
# 📊 Customer Churn Exploratory Analysis
# ============================================

import pandas as pd
import plotly.express as px
import os


# ============================================
# 📂 Load data
# ============================================

df = pd.read_csv("Cancelamentos.csv")


# ============================================
# 🔄 Rename columns (Portuguese → English)
# ============================================

df = df.rename(columns={
    "CustomerID":"customer_id",
    "idade":"age",
    "sexo":"gender",
    "tempo_como_cliente":"tenure",
    "frequencia_uso":"usage_frequency",
    "ligacoes_callcenter":"callcenter_calls",
    "dias_atraso":"delay_days",
    "assinatura":"subscription",
    "duracao_contrato":"contract_duration",
    "total_gasto":"total_spent",
    "meses_ultima_interacao":"months_since_last_interaction",
    "cancelou":"churn",
    "forma_pagamento": "payment_method"
})


# ============================================
# 🔍 Initial Exploration
# ============================================

display(df)


# ============================================
# 🧹 Data cleaning
# ============================================

df = df.dropna()


# ============================================
# 💾 Save cleaned dataset
# ============================================

df.to_csv("clean_data.csv", index=False)

print("\n✅ 'clean_data.csv' successfully saved!")


# ============================================
# 📊 Churn analysis
# ============================================

print(df["churn"].value_counts(normalize=True))


# ============================================
# 📈 Analysis by columns
# ============================================

for coluna in df.columns:
    if coluna != "churn":
        print(df.groupby(coluna)["churn"].mean())


# ============================================
# 📊 Charts
# ============================================

# Create folder for charts
os.makedirs("charts", exist_ok=True)

for coluna in df.columns:
    if coluna != "churn":
        grafico = px.histogram(df, x=coluna, color="churn")
        
        # Save chart
        grafico.write_html(f"charts/churn_by_{coluna}.html")
        
        grafico.show()
