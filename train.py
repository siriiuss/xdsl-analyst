import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# Veri Yükleme
df = pd.read_csv('dsl_statistics.csv')

# Verilerin İlk 5 Satırını Görüntüleme
print("Verilerin İlk 5 Satırı:")
print(df.head())

# Eksik Verileri Kontrol Etme
print("\nEksik Veriler:")
print(df.isnull().sum())

# Yalnızca sayısal sütunlarda eksik verileri ortalama ile doldurma
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Kategorik Verileri Sayısal Değerlere Dönüştürme
df['Bağlantı Durumu'] = df['Bağlantı Durumu'].map({'sağlandı': 1, 'sorun var': 0})

# Özellikler (X) ve Hedef Değişken (y) Belirleme
X = df.drop('Bağlantı Durumu', axis=1)
y = df['Bağlantı Durumu']

# Veriyi Eğitim ve Test Setlerine Bölme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Oluşturma ve Eğitme
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Test Verisi ile Tahmin Yapma
y_pred = model.predict(X_test)

# Modelin Değerlendirilmesi
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f'\nDoğruluk Oranı: {accuracy:.2f}')
print('\nKarışıklık Matrisi:')
print(conf_matrix)
print('\nSınıflandırma Raporu:')
print(class_report)

# Modeli Kaydetme
joblib.dump(model, 'dsl_model.pkl')
