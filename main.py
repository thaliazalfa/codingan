#import library pickle untuk import pickle dari jupyter notebook
import pickle

#import streamlit untuk membuat website 
import streamlit as st
from streamlit_option_menu import option_menu

#import library scikitlearn untuk denormalize variabel hasil,
#supaya hasil prediksi yang keluar bernilai normal dalam satuan detik
from sklearn.preprocessing import MinMaxScaler

#import library untuk insert image
from PIL import Image


scalar = MinMaxScaler()
model = pickle.load(open('estimasi_waktu_mr.sav','rb'))
with open('average_second.pickle', 'rb') as file:
    average_second = pickle.load(file)

#sidebar navigation
with st.sidebar:
    selected = option_menu("Prediksi Kecepatan Mengetik", 
    ["Home", 
    'Prediksi'],
    icons=['bi bi-house-door-fill', 'calculator'],
    default_index=1)

 
#halaman prediksi
if(selected == 'Prediksi'):
    #hitung prediksi  
    st.title('Analisis Kecepatan Mengetik Karyawan PT Lima Master')
    st.write("""
    Untuk mendapatkan prediksi waktu penginputan data, harap lakukan test kecepatan 
    mengetik pada link website yang diterakan di bawah ini
    """)
    website_url = "https://typingtop.com/indonesian/typing-test"

    # Menyisipkan tautan menggunakan Markdown
    st.markdown(f"[Klik disini untuk menguji kecepatan WPM]({website_url})")

    wpm_average = st.number_input('Masukkan Nilai WPM', 0)
    accuracy = st.number_input('Masukkan Nilai Akurasi', 0)
    decimal_accuracy = accuracy/100
    umur = st.number_input('Masukkan Umur', 0)
    gender = st.radio("Pilih jenis kelamin:", ("Laki-laki", "Perempuan"))

    # Mengonversi input ke nilai (perempuan = 0, laki-laki = 1)
    if gender == "Perempuan":
        gender_value = 0
    else:
        gender_value = 1

   

    predict = ''

    if st.button('Pediksi Waktu'):
        predict = model.predict(
            [[wpm_average, decimal_accuracy, umur, gender_value]]
        )
        scalar.fit(average_second)
        denormalized_prediction = scalar.inverse_transform(predict)
        st.write('Estimasi waktu untuk menginput satu data : ', denormalized_prediction/60, ' menit')


if (selected == 'Home') :
    st.title('Selamat Datang!')
    st.text('ayo prediksi kecepatan menginput datamu sekarang!')
    st.image('typing.jpg')
    st.write("""
    Dengan aplikasi prediksi ini, kamu dapat mengetahui berapa estimasi waktu yang kamu 
    butuhkan untuk menginput data. Untuk mengetahui estimasi waktu penginputan data, kamu
    harus melakukan test typing, speed selama satu menit saja!
    """)
