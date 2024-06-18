import pandas as pd

# Örnek veriler
data = {
    "Downstream Hızı (Mbps)": [50, 20, 35, 15, 40, 10, 45, 30, 25, 50],
    "Upstream Hızı (Mbps)": [10, 5, 8, 3, 9, 2, 12, 6, 4, 11],
    "Maksimum Downstream Hızı (Mbps)": [50, 20, 35, 15, 40, 10, 45, 30, 25, 50],
    "Maksimum Upstream Hızı (Mbps)": [10, 5, 8, 3, 9, 2, 12, 6, 4, 11],
    "Sinyal Gürültü Oranı Downstream (dB)": [30, 25, 28, 22, 29, 20, 31, 27, 26, 32],
    "Sinyal Gürültü Oranı Upstream (dB)": [20, 18, 19, 16, 21, 15, 22, 18, 17, 23],
    "Attenuation Downstream (dB)": [5, 8, 6, 10, 7, 12, 6, 9, 10, 5],
    "Attenuation Upstream (dB)": [2, 3, 2, 4, 3, 5, 2, 3, 4, 2],
    "CRC Hataları": [0, 5, 1, 10, 2, 20, 0, 3, 4, 0],
    "FEC Hataları": [0, 2, 0, 5, 1, 10, 0, 1, 2, 0],
    "HEC Hataları": [0, 1, 0, 2, 0, 5, 0, 1, 1, 0],
    "Bağlantı Durumu": ["sağlandı", "sorun var", "sağlandı", "sorun var", "sağlandı", "sorun var", "sağlandı", "sorun var", "sorun var", "sağlandı"]
}

# DataFrame oluşturma
df = pd.DataFrame(data)

# CSV dosyasına yazma
df.to_csv('dsl_statistics.csv', index=False)

print("dsl_statistics.csv dosyası oluşturuldu.")
