

import streamlit as st
import pandas as pd
import numpy as np
import json
import requests




option = st.selectbox(
    ' ',('Activados', 'Ingresos'))
valor=option


title = st.text_input('Key - event')
valor2=title



def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


def dataframe2():
  st.write("Registro de "+valor)
  #915012158

  geojson_url="https://smartiket-19bb6-default-rtdb.firebaseio.com/"+valor+"/"+valor2+".json"
  df = pd.read_json(geojson_url).T
  df.reset_index(drop=True, inplace=True)  # Restablecer el índice

  st.dataframe(df)  # Same as st.write(df)
  csv = convert_df(df)

  st.download_button(
    label="Descargar registros de "+valor+".csv",
    data=csv,
    file_name=valor+'.csv',
    mime='text/csv',
)

       









if st.button('ver registros'):
    dataframe2()


st.sidebar.markdown('## Ticketsmart Dashboar')
st.sidebar.markdown('<small>© 2023 TicketSmart Technologies, LLC [https://ticketsmart.tech/](https://ticketsmart.tech/)</small>', unsafe_allow_html=True)

st.sidebar.markdown('''<hr>''', unsafe_allow_html=True)
st.sidebar.markdown('''<small>[Ticketsmart v1.0.17](https://ticketsmart.tech/)  | Dic 2023 | [Free version](https://play.google.com/store/apps/details?id=labs.aplication.ticketsmartrelease)</small>''', unsafe_allow_html=True)




