import pickle
import streamlit as st

model = pickle.load(open('prediksi_kematian.sav', 'rb'))

st.title("Prediksi Kematian Pasien Penderita Penyakit Gagal Jantung")

# Membagi visualisasi menjadi 2 kolom
col1, col2 = st.columns(2)

with col1:
    age = st.number_input('input umur', key='age')
    ejection_fraction = st.number_input('input ejection_fraction', key='ejection_fraction')
    serum_creatine = st.number_input('input serum_creatine', key='serum_creatine')
    platelets = st.number_input('input platelets', key='platelets')
    high_blood_pressure = st.selectbox('Punya tekanan darah tinggi? (0=No, 1=Yes)', (0,1), key='high_blood_pressure')

with col2:
    anaemia = st.selectbox('Punya anaemia? (0=No, 1=Yes)', (0,1), key='anaemia')
    diabetes = st.selectbox('Punya penyakit diabetes? (0=No, 1=Yes)', (0,1), key='diabetes')
    serum_sodium = st.number_input('input serum_sodium', key='serum_sodium')
    creatinine_phosphokinase = st.number_input('input creatinine_phosphokinase', key='creatinine_phosphokinase')

if st.button("Prediksi Kematian Pasien"):
    predict = model.predict(
        [[age, anaemia, ejection_fraction, diabetes, serum_creatine, serum_sodium, platelets, creatinine_phosphokinase, high_blood_pressure]]
    )
    if predict[0] == 1:
        death_predict = 'Pasien sudah meninggal sebelum waktu follow-up (1)'
    else:
        death_predict = 'Pasien masih bertahan pada waktu follow-up (0)'
    
    st.success(death_predict)
