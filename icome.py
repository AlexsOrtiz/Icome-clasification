# Importa las librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lee el archivo CSV
df = pd.read_csv('income_evaluation.csv')

# Verifica si hay valores nulos
df.isnull().any()

# Renombra las columnas
df = df.rename(columns={
    'age': 'age',
    ' workclass': 'workclass',
    ' fnlwgt': 'final_weight',
    ' education': 'education',
    ' education-num': 'education_num',
    ' marital-status': 'marital_status',
    ' occupation': 'occupation',
    ' relationship': 'relationship',
    ' race': 'race',
    ' sex': 'sex',
    ' capital-gain': 'capital_gain',
    ' capital-loss': 'capital_loss',
    ' hours-per-week': 'hrs_per_week',
    ' native-country': 'native_country',
    ' income': 'income'
})

# Imprime las columnas
print(df.columns)

# Muestra la frecuencia de las ocupaciones con ingresos >50K
print(df[df['income'] == ' >50K']['occupation'].value_counts().head(3))

# Genera la gráfica de barras apilada con colores morado y azul claro
pd.crosstab(df["occupation"], df['income']).plot(kind='barh', stacked=True, figsize=(20, 10), color=['#974fff', '#f9d291'])

# Muestra la gráfica
plt.show()

