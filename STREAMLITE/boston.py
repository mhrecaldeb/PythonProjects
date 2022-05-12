# import the needed modules
import pandas as pd
import numpy as np
import streamlit as st

# Data import & columns
df = pd.read_csv('boston.csv')

#df['90s'] = df['minutes']/90

#calc_elements = ['goals', 'assists', 'points']

#for each in calc_elements:
#    df[f'{each}_p90'] = df[each] / df['90s']

radios = list(df['rad'].drop_duplicates())
impuestos = list(df['tax'].drop_duplicates())

# App
st.title(f"Analisis de datos de Boston")

# Sidebar - title & filters
st.sidebar.markdown('### Filtros de Datos')
radios_choice = st.sidebar.multiselect(
    'Escoger los radios:', radios, default=radios)
impuestos_choice = st.sidebar.multiselect(
    "Impuestos:", impuestos, default=impuestos)
crim_choice = st.sidebar.slider(
    'Max Crim:', min_value=df['crim'].min(), max_value=89.0, step=.5, value=89.0)

df = df[df['rad'].isin(radios_choice)]
df = df[df['tax'].isin(impuestos_choice)]
df = df[df['crim'] < crim_choice]

# Main - dataframes
st.markdown('### Boston Dataframe')

st.dataframe(df.sort_values('age',
             ascending=False).reset_index(drop=True))

# Main - charts
st.markdown('### MedV vs Age')

st.vega_lite_chart(df, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'age', 'type': 'quantitative'},
        'y': {'field': 'medv', 'type': 'quantitative'},
        'color': {'field': 'rad', 'type': 'nominal'},
        'tooltip': [{"field": 'rad', 'type': 'nominal'}, {'field': 'medv', 'type': 'quantitative'}, {'field': 'age', 'type': 'quantitative'}],
    },
    'width': 700,
    'height': 400,
})

# st.markdown('### Goals p90 vs Assists p90')

# st.vega_lite_chart(df, {
#     'mark': {'type': 'circle', 'tooltip': True},
#     'encoding': {
#         'x': {'field': 'goals_p90', 'type': 'quantitative'},
#         'y': {'field': 'assists_p90', 'type': 'quantitative'},
#         'color': {'field': 'position', 'type': 'nominal'},
#         'tooltip': [{"field": 'name', 'type': 'nominal'}, {'field': 'cost', 'type': 'quantitative'}, {'field': 'points', 'type': 'quantitative'}],
#     },
#     'width': 700,
#     'height': 400,
# })
