import pickle
import streamlit as st

model = pickle.load(open('prediksi_hujan.sav', 'rb'))

st.title("Prediksi Hujan di Australia Algoritma SVM")

# Membagi visualisasi menjadi 2 kolom
col1, col2 = st.columns(2)

with col1:
    Location = st.number_input('input lokasi')
with col2:
    MinTemp = st.number_input('input suhu minimum')
with col1:
    Rainfall = st.number_input('input jumlah curah hujan')
with col2:
    WindGustDir = st.number_input('input arah hembusan angin terkuat')
with col1:
    WindGustSpeed = st.number_input('input kecepatan angin terkuat')
with col2:
    Humidity3pm = st.number_input('input kelembaban')
with col1:
    Pressure9am = st.number_input('input tekanan atmosfer')
with col2:
    RainToday = st.number_input('cuaca hari ini (0=tidak hujan, 1=hujan)')    

predict = ''

if st.button("Prediksi Hujan pada Esok Hari"):
    predict = model.predict(
        [[Location, MinTemp, Rainfall, WindGustDir, WindGustSpeed, Humidity3pm, Pressure9am, RainToday]]
    )
    if(predict[0]==1):
        rain_predict = 'Besok akan turun hujan'
    else:
        rain_predict = 'Besok tidak akan turun hujan'
    
    st.success(rain_predict)
    