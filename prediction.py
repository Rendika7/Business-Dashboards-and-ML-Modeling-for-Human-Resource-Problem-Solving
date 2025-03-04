import pandas as pd
import joblib

# Memuat pipeline yang telah disimpan
with open('best_model_pipeline.pkl', 'rb') as file_pipeline:
    best_model_pipeline = joblib.load(file_pipeline)

# Membaca file CSV yang benar
inference_data = pd.read_excel("inference_data.xlsx")

# Melakukan prediksi menggunakan pipeline yang telah dilatih
hasil_prediksi = best_model_pipeline.predict(inference_data)

# Add the predicted attrition to the inference_data
inference_data['PredictedAttrition'] = hasil_prediksi

# Menampilkan hasil prediksi
print("Hasil Prediksi:", inference_data[['EmployeeId', 'PredictedAttrition']])