#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




#Cargar la data 
#eliminé los saltos de línea en los encabezados de data.xlsx
@st.cache
def load_data():
    try:
        data = pd.read_excel(rf"Data\data.xlsx")
        return data
    except Exception as e:
        st.error(f"Error al cargar la data: {e}")
        return pd.DataFrame()  

df = load_data()

st.title('Monitoreo de calidad de aire QAIRA')

st.info('El presente dashboard contiene información de variables usadas para monitorear la calidad del aire durante el mes de Junio 2021 en el Ovalo de Miraflores - Lima, Perú.', icon="ℹ️")

st.link_button("Ir al dataset",  "https://www.datosabiertos.gob.pe/dataset/monitoreo-de-calidad-de-aire-qaira%C2%A0-municipalidad-de-miraflores/resource/5ccaf849-33a6-46ff")

st.markdown('<h3 style="color:navy;">1. Datos en tabla (listos para descargar)</h3>', unsafe_allow_html=True)
st.write(df)


pollutants = ['CO (ug/m3)', 'H2S (ug/m3)', 'NO2 (ug/m3)', 'O3 (ug/m3)', 
              'PM10 (ug/m3)', 'PM2.5 (ug/m3)', 'SO2 (ug/m3)']

pollutants_mean = df[pollutants].mean().sort_values(ascending=False)


#Gráfico de barras de los contaminantes 
#pollutants_mean = df[pollutants].mean()
#st.write('Promedio de las variables contaminantes')
#st.bar_chart(pollutants_mean)

# Configurar el estilo de seaborn
sns.set(style="whitegrid")

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
bar_plot = sns.barplot(x=pollutants_mean.index, y=pollutants_mean.values, palette="Blues_r")

# Añadir etiquetas encima de cada barra
for index, value in enumerate(pollutants_mean.values):
    bar_plot.text(index, value + 0.5, round(value, 2), ha='center', va='bottom', fontsize=10)

st.divider()

# Configurar el estilo del gráfico
ax.set(ylabel='Promedio (ug/m3)', xlabel='')
st.markdown('<h3 style="color:navy;">2. Promedio de las variables contaminantes</h3>', unsafe_allow_html=True)
ax.title.set_fontsize(20)
# Mostrar el gráfico en Streamlit
st.pyplot(fig)


st.divider()
#GRAFICO 2: Lineas de tendencia para Humedad, Presión y Temperatura-----------
st.markdown('<h3 style="color:navy;">3. Lineas de tendencia para Humedad, Presión y Temperatura por Día</h3>', unsafe_allow_html=True)

st.info('Seleccione un range de fechas para filtrar las tendencias. Seleccione el rango de escala de eje Y para visualizar mejor cada gráfico.', icon="ℹ️")


df['Fecha'] = pd.to_datetime(df['Fecha'])
daily_means = df.set_index('Fecha').resample('D')[['Humedad (%)', 'Presion (Pa)', 'Temperatura (C)']].mean()


#for column in daily_means.columns:
#    st.line_chart(daily_means[column])


# Asignar una fecha por defecto
default_date = pd.to_datetime('2021-06-01')
default_date2 = pd.to_datetime('2021-06-30')
# Crear el widget date_input con la fecha por defecto
#selected_date = st.date_input('Seleccione una fecha', min_value=df['Fecha'].min(), max_value=df['Fecha'].max(), value=default_date)



# Crear el widget date_input para seleccionar el rango de fechas
date_range = st.date_input('Seleccione el rango de fechas', 
                           min_value=df['Fecha'].min(), 
                           max_value=df['Fecha'].max(), 
                           value=(default_date, default_date2))

# Obtener las fechas de inicio y fin del rango seleccionado
start_date, end_date = date_range

# Filtrar el DataFrame según el rango de fechas seleccionado
filtered_data = daily_means.loc[start_date:end_date]



import altair as alt

st.write('##### Humedad Promedio por Día')
# Personalizar la escala del eje X
y_axis_scale = st.slider('Escala del Eje Y', min_value=0, max_value=100, value=(0,110))

# Filtrar datos según el rango de fechas seleccionado en el eje X
#filtered_data = filtered_data.iloc[y_axis_scale[0]:y_axis_scale[1]]
#for column in filtered_data.columns:
#    st.line_chart(filtered_data[column], use_container_width=True, height=400 ) 

#st.line_chart(filtered_data, use_container_width=True, height=400, key='custom_chart', y_axis_scale=(0, y_axis_scale))
chart = alt.Chart(filtered_data['Humedad (%)'].reset_index()).mark_line(strokeWidth=3).encode(
    x='Fecha:T',
    y=alt.Y('Humedad (%)', scale=alt.Scale(domain=[y_axis_scale[0], y_axis_scale[1]])),
)

st.altair_chart(chart, use_container_width=True)


st.write('##### Presión Promedio por Día')
y_axis_scale2 = st.slider('Escala del Eje Y', min_value=950, max_value=1050, value=(950,1050))
chart2 = alt.Chart(filtered_data['Presion (Pa)'].reset_index()).mark_line(strokeWidth=3).encode(
    x='Fecha:T',
    y=alt.Y('Presion (Pa)', scale=alt.Scale(domain=[y_axis_scale2[0], y_axis_scale2[1]])),
)
st.altair_chart(chart2, use_container_width=True)

st.write('##### Temperatura Promedio por Día')
y_axis_scale3 = st.slider('Escala del Eje Y', min_value=0, max_value=30, value=(0,30))
chart3 = alt.Chart(filtered_data['Temperatura (C)'].reset_index()).mark_line(strokeWidth=3).encode(
    x='Fecha:T',
    y=alt.Y('Temperatura (C)', scale=alt.Scale(domain=[y_axis_scale3[0], y_axis_scale3[1]])),
)
st.altair_chart(chart3, use_container_width=True)

st.divider()

#GRAFICO 3: Mapa de Calor de Temperatura (No me muestra)
st.markdown('<h3 style="color:navy;">4. Mapa de Calor de Temperatura por Día de la semana y Hora</h3>', unsafe_allow_html=True)
temperature_pivot = df.pivot_table(
    values='Temperatura (C)', 
    index=df['Fecha'].dt.hour, 
    columns=df['Fecha'].dt.day_name(),
    aggfunc='mean'
)

plt.figure(figsize=(10, 8))
sns.heatmap(temperature_pivot, cmap='coolwarm', annot=True)
plt.xlabel('WeekDay')
plt.ylabel('Hour')
st.pyplot(plt)
