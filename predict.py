import joblib
import numpy as np
import pandas as pd

# Kaydedilmiş modeli yükleme
model = joblib.load('dsl_model.pkl')


# Kullanıcıdan veri girişi alma
def get_user_input():
    down_speed = float(input("Downstream Hızı (Mbps): "))
    up_speed = float(input("Upstream Hızı (Mbps): "))
    max_down_speed = float(input("Maksimum Downstream Hızı (Mbps): "))
    max_up_speed = float(input("Maksimum Upstream Hızı (Mbps): "))
    snr_down = float(input("Sinyal Gürültü Oranı Downstream (dB): "))
    snr_up = float(input("Sinyal Gürültü Oranı Upstream (dB): "))
    attenuation_down = float(input("Attenuation Downstream (dB): "))
    attenuation_up = float(input("Attenuation Upstream (dB): "))
    crc_errors = int(input("CRC Hataları: "))
    fec_errors = int(input("FEC Hataları: "))
    hec_errors = int(input("HEC Hataları: "))

    # Kullanıcı verilerini bir veri çerçevesi (DataFrame) olarak düzenleme
    user_data = pd.DataFrame({
        'Downstream Hızı (Mbps)': [down_speed],
        'Upstream Hızı (Mbps)': [up_speed],
        'Maksimum Downstream Hızı (Mbps)': [max_down_speed],
        'Maksimum Upstream Hızı (Mbps)': [max_up_speed],
        'Sinyal Gürültü Oranı Downstream (dB)': [snr_down],
        'Sinyal Gürültü Oranı Upstream (dB)': [snr_up],
        'Attenuation Downstream (dB)': [attenuation_down],
        'Attenuation Upstream (dB)': [attenuation_up],
        'CRC Hataları': [crc_errors],
        'FEC Hataları': [fec_errors],
        'HEC Hataları': [hec_errors]
    })
    return user_data


# Kullanıcıdan veri al
user_data = get_user_input()

# Tahmin yapma
prediction = model.predict(user_data)
prediction_proba = model.predict_proba(user_data)

# Sonuçları gösterme
if prediction[0] == 1:
    print("Bağlantı Durumu: Sağlandı")
else:
    print("Bağlantı Durumu: Sorun Var")

print(f"Sağlandı olasılığı: {prediction_proba[0][1]:.2f}")
print(f"Sorun Var olasılığı: {prediction_proba[0][0]:.2f}")
