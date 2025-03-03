# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding

Jaya Jaya Maju merupakan perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Meskipun telah menjadi perusahaan besar, Jaya Jaya Maju mengalami kesulitan dalam mengelola karyawan yang berdampak pada tingginya tingkat **attrition rate** (rasio karyawan yang keluar dari total karyawan) yang mencapai lebih dari 10%.

**Tujuan utama dari proyek ini** adalah untuk membantu departemen HR dalam mengidentifikasi faktor-faktor yang mempengaruhi tinggi rendahnya tingkat attrition karyawan dan memberikan solusi berbasis data untuk mengurangi attrition rate.

### Permasalahan Bisnis

1. **Tingginya attrition rate lebih dari 10%** yang berisiko pada efisiensi operasional dan biaya perekrutan yang lebih tinggi.  
   - Dibutuhkan **model klasifikasi** untuk mengidentifikasi karyawan yang berisiko tinggi untuk keluar berdasarkan data historis, seperti umur, jabatan, tingkat kepuasan kerja, dan faktor lainnya.

2. **Kesulitan dalam mengelola data karyawan** yang berdampak pada ketidakteraturan dalam monitoring faktor-faktor yang mempengaruhi keputusan karyawan untuk keluar dari perusahaan.  
   - Dibutuhkan **business dashboard** untuk membantu departemen HR dalam memonitor dan memahami data, serta mengidentifikasi faktor-faktor yang mempengaruhi attrition rate secara lebih visual dan terintegrasi.

3. **Keterbatasan dalam analisis data**, sehingga tidak dapat mengetahui faktor-faktor utama yang menyebabkan attrition.  
   - Dengan adanya **business dashboard**, perusahaan dapat menganalisis dan memvisualisasikan faktor-faktor yang berpengaruh terhadap attrition rate, yang membantu HR dalam membuat keputusan yang lebih tepat dan strategis berdasarkan data yang ada.
berdasarkan permasalahn bisnis diatas ini, buatkana kau cakupan proyek

### Cakupan Proyek

1. **Pengembangan Model Klasifikasi untuk Prediksi Attrition Rate**  
    Membangun **_model klasifikasi_** untuk memprediksi karyawan yang berisiko tinggi keluar berdasarkan **_data historis_**, seperti umur, jabatan, tingkat kepuasan kerja, dan faktor lainnya. Model ini akan dievaluasi menggunakan **_akurasi_**, **_recall_**, **_precision_**, dan **_f1-score_** untuk memilih yang terbaik.

2. **Pembuatan Business Dashboard untuk Monitoring Attrition Rate**  
    Mengembangkan **_business dashboard_** untuk memantau **_attrition rate_** secara real-time, yang akan menampilkan visualisasi faktor-faktor yang mempengaruhi keputusan karyawan untuk keluar, seperti **_kepuasan kerja_** dan **_gaji_**. Dashboard ini juga akan membantu departemen HR dalam memahami data dan mengidentifikasi faktor-faktor penyebab attrition secara lebih visual dan terintegrasi.

3. **Analisis Data dan Visualisasi**  
   Menganalisis **_data karyawan_** untuk mengidentifikasi faktor utama penyebab **_attrition rate_** tinggi. Memberikan laporan dan **_visualisasi_** yang membantu HR memahami penyebabnya dan menyediakan **_rekomendasi_** untuk mengurangi attrition.

4. **Rekomendasi Strategi Retensi**  
   Berdasarkan **_analisis_** dan **_prediksi_**, memberikan **_rekomendasi_** untuk meningkatkan **_retensi_** karyawan. Mengidentifikasi kebijakan atau perubahan yang dapat diterapkan untuk mengurangi risiko attrition di masa depan. Menyusun beberapa **_action items_** yang dapat diikuti oleh perusahaan untuk mencapai target pengurangan attrition dan meningkatkan loyalitas karyawan.

### Persiapan

Sumber data: Untuk menganalisis **attrition rate** dan faktor-faktor yang mempengaruhinya, perusahaan Jaya Jaya Maju telah menyediakan dataset yang dapat digunakan untuk membangun model prediksi dan menganalisis data terkait dengan business Dashboard. Dataset ini dapat diunduh melalui tautan berikut: [Dataset Karyawan Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:

```bash
# 1. Clone GitHub Repository (Contoh Repo)
$ git clone https://github.com/example/repository.git

# 2. Masuk ke Direktori Proyek
$ cd repository

# 3. Buat Environment Conda
$ conda create --name myenv python=3.10

# 4. Aktifkan Environment
$ conda activate myenv

# 5. Install Dependensi dari requirements.txt
$ pip install -r requirements.txt

# 6. Jika selesai digunakan, deaktifkan Environment
$ conda deactivate
```

## Business Dashboard

![Header Dashboard](link/to/img/)

Dashboard **HR Analytics: Workforce Insights & Attrition Monitoring** dirancang untuk membantu **departemen HR** dalam memahami berbagai aspek tenaga kerja dan mengidentifikasi faktor-faktor yang mempengaruhi **attrition rate** karyawan. Dengan visualisasi interaktif yang mudah dipahami, dashboard ini memberikan wawasan mendalam mengenai **kinerja karyawan**, **tingkat kepuasan kerja**, **tingkat attrition**, dan berbagai faktor lainnya yang berkontribusi pada keputusan karyawan untuk tetap bekerja atau keluar dari perusahaan. Dashboard ini juga memungkinkan **HR** untuk memantau **attrition rate** secara real-time dengan berbagai filter seperti **gender**, **usia**, **departemen**, **job role**, **work-life balance**, dan **pendapatan bulanan**. Selain itu, terdapat metrik utama seperti jumlah **karyawan** (**1,470**), **rata-rata usia** (**36.92**), **rata-rata kepuasan kerja** (**2.73**), dan **rata-rata durasi kerja** (**7 tahun**), yang membantu HR dalam mengambil keputusan berbasis data untuk mengurangi **attrition rate** dan meningkatkan retensi karyawan.

![Header Dashboard](link/to/img/)

### **1. Gender vs. Attrition Rate (Chart Pertama)**  
**_Chart ini membandingkan attrition rate antara pria dan wanita._** Berdasarkan grafik ini, **_female_** memiliki **_attrition rate_** yang lebih tinggi (**34.69%**) dibandingkan dengan **_male_** (**38.55%**). Hal ini memberikan indikasi bahwa **_wanita_** cenderung memiliki tingkat keluar yang lebih tinggi dibandingkan dengan pria dalam perusahaan ini.

![Header Dashboard](link/to/img/)

### **2. Departemen vs. Attrition (Chart Kedua)**  
**_Chart ini menunjukkan perbandingan antara jumlah karyawan di setiap departemen dengan tingkat attrition di masing-masing departemen._** **_Research & Development_** memiliki **_attrition rate_** yang paling tinggi dibandingkan dengan **_Sales_** dan **_Human Resources_**. **_Sales_** dan **_Human Resources_** memiliki **_attrition rate_** yang lebih rendah, yang menunjukkan bahwa **_departemen Research & Development_** mungkin perlu diberi perhatian lebih dalam hal retensi karyawan.

![Header Dashboard](link/to/img/)

### **3. Faktor Usia terhadap Attrition (Chart Ketiga)**  
**_Grafik ini membandingkan jumlah karyawan berdasarkan kelompok usia dengan attrition rate yang ada._** **_Kelompok usia 20-30 tahun_** memiliki **_attrition rate_** tertinggi (**45.26%**), menunjukkan bahwa karyawan yang lebih muda cenderung keluar lebih banyak dibandingkan kelompok usia lainnya. Sebaliknya, **_kelompok usia 51+_** memiliki **_attrition rate_** yang lebih rendah (**30.63%**), yang menunjukkan bahwa karyawan yang lebih tua lebih cenderung bertahan.

![Header Dashboard](link/to/img/)

### **4. Job Role vs. Attrition (Chart Keempat)**  
**_Chart ini menunjukkan perbandingan antara jumlah karyawan di setiap job role dengan attrition rate masing-masing._** **_Sales Representative_** dan **_Sales Executive_** memiliki **_attrition rate_** yang lebih tinggi dibandingkan dengan peran lainnya. **_Laboratory Technician_** memiliki **_attrition rate_** yang rendah, yang bisa menunjukkan tingkat kepuasan kerja yang lebih baik di posisi ini. Sebaliknya, **_Research Scientist_** juga menunjukkan **_attrition rate_** yang relatif tinggi.

![Header Dashboard](link/to/img/)

### **5. Work-Life Balance vs. Attrition (Chart Kelima)**  
**_Grafik ini menunjukkan hubungan antara work-life balance dan jumlah karyawan yang keluar._** **_Work-Life Balance_** yang lebih rendah (**Level 2**) menunjukkan **_jumlah karyawan keluar_** yang paling tinggi. Di sisi lain, **_Work-Life Balance Level 3_** (baik) menunjukkan penurunan dalam jumlah karyawan yang keluar, yang menunjukkan pentingnya keseimbangan kerja dan kehidupan pribadi dalam mempertahankan karyawan.

![Header Dashboard](link/to/img/)

### **6. Durasi Kerja vs. Attrition (Chart Keenam)**  
**_Grafik ini membandingkan jumlah karyawan yang bertahan berdasarkan durasi kerja (YearsAtCompany) dengan jumlah karyawan yang keluar._** **_Durasi kerja 3-5 tahun_** menunjukkan **_attrition rate_** yang cukup tinggi. Sebaliknya, karyawan yang berada di perusahaan lebih dari **_20 tahun_** menunjukkan **_attrition rate_** yang sangat rendah, yang bisa menunjukkan bahwa karyawan lama lebih bertahan.

![Header Dashboard](link/to/img/)

### **7. Hubungan antara Monthly Income dan Attrition (Chart Ketujuh)**  
**_Grafik ini menunjukkan rata-rata pendapatan bulanan (MonthlyIncome) dari karyawan yang keluar vs. yang bertahan._** Karyawan dengan pendapatan yang lebih tinggi (**>6,000**) lebih cenderung bertahan dalam perusahaan, sementara karyawan dengan pendapatan lebih rendah (**<5,000**) lebih cenderung keluar. Ini menunjukkan adanya hubungan antara **_gaji_** dan **_retensi karyawan_**.

![Header Dashboard](link/to/img/)

### **8. Rata-rata Job Satisfaction berdasarkan Job Role (Chart Kedelapan)**  
**_Grafik ini menunjukkan perbandingan rata-rata kepuasan kerja (Job Satisfaction) antara peran pekerjaan di perusahaan._** **_Laboratory Technician_** memiliki **_rata-rata kepuasan kerja_** tertinggi (2.56), yang menunjukkan tingkat kepuasan yang lebih tinggi di posisi tersebut. Peran lain seperti **_Sales Executive_** dan **_Research Scientist_** memiliki skor kepuasan yang lebih rendah, yang dapat berhubungan dengan tingginya **_attrition rate_** di posisi tersebut.

![Header Dashboard](link/to/img/)

### **9. Rata-rata Job Satisfaction berdasarkan Monthly Income (Chart Kesembilan)**  
**_Grafik ini membandingkan rata-rata Job Satisfaction dengan Monthly Income._** Karyawan dengan **_gaji lebih tinggi_** memiliki skor kepuasan yang lebih baik, yang bisa menjadi indikator bahwa **_gaji berpengaruh terhadap tingkat kepuasan_** dan **_attrition rate_**.

![Header Dashboard](link/to/img/)

### **10. Rata-rata Job Satisfaction berdasarkan Job Role (Chart Kesepuluh)**  
**_Grafik ini menggambarkan perbandingan antara jumlah karyawan keluar dan rata-rata kepuasan kerja di setiap peran._** **_Research Scientist_** dan **_Sales Representative_** menunjukkan **_rata-rata kepuasan kerja_** yang lebih rendah, yang bisa berkontribusi pada tingginya **_attrition rate_**.








## Model Machine Learning

Model machine learning dibangun untuk memprediksi kemungkinan seorang karyawan akan keluar dari perusahaan berdasarkan data historis. Model ini menggunakan beberapa algoritma, termasuk **Logistic Regression**, **Support Vector Machine (SVM)**, **K-Nearest Neighbor**, dan **Gradient Boosting**. Model ini dilatih menggunakan data karyawan yang sudah ada dan memberikan prediksi tentang potensi attrition pada karyawan baru.

### **Model Comparison**
Performa beberapa model dibandingkan menggunakan beberapa metrik seperti akurasi, presisi, recall, dan skor F1. Berikut adalah hasilnya:

| Model               | Akurasi | Presisi | Recall | Skor F1 |
|---------------------|---------|---------|--------|---------|
| Logistic Regression  | 0.70    | 0.70    | 0.65   | 0.65    |
| SVM                  | 0.80    | 0.80    | 0.75   | 0.76    |
| KNN                  | 0.76    | 0.76    | 0.72   | 0.73    |
| Gradient Boosting    | 0.85    | 0.85    | 0.80   | 0.82    |

**Best Model:**
Setelah mengevaluasi beberapa model, **Gradient Boosting** dipilih sebagai model terbaik Berdasarkan skor F1 dengan skor F1 sebesar **0.82**. Dengan akurasi tertinggi dan interpretabilitas yang lebih baik dalam konteks fitur-fitur yang berkontribusi terhadap attrition rate. 

### **Hasil Inferensi (Model Terbaik)**
Berikut adalah hasil inferensi yang dibuat oleh model **Gradient Boosting**:

| EmployeeId | PrediksiAttrition | AttritionSebenarnya |
|------------|-------------------|---------------------|
| 1041       | 0.00              | 1.00                |
| 184        | 1.00              | 1.00                |
| 1222       | 0.00              | 0.00                |
| 67         | 0.00              | 0.00                |
| 220        | 0.00              | 0.00                |
| 494        | 0.00              | 0.00                |
| 430        | 0.00              | 0.00                |
| 240        | 1.00              | 0.00                |
| 218        | 0.00              | 0.00                |
| 49         | 0.00              | 0.00                |

**Akurasi Inferensi**: **0.80**

### **Feature Importance based on Permutation Importance**

![Feature Importance Plot](https://github.com/Rendika7/Business-Dashboards-and-ML-Modeling-for-Human-Resource-Problem-Solving/blob/main/image/Feature%20Importance%20Plot.png?raw=true)

Berdasarkan grafik **Pentingnya Fitur**, faktor-faktor yang paling mempengaruhi **attrition rate** karyawan adalah **DailyRate**, **OverTime**, dan **MonthlyRate**, yang masing-masing menunjukkan penurunan akurasi sebesar 0.05 dan 0.04 ketika dihapus, menandakan bahwa gaji harian, jumlah lembur, dan gaji bulanan berperan besar dalam keputusan karyawan untuk keluar dari perusahaan. Selain itu, **DistanceFromHome** dan **MonthlyIncome** juga memiliki pengaruh signifikan dengan penurunan akurasi sebesar 0.04 dan 0.03, yang mengindikasikan bahwa jarak rumah ke kantor dan pendapatan bulanan turut mempengaruhi keputusan karyawan. **JobSatisfaction** dan **JobRole** juga berkontribusi pada keputusan attrition, dengan penurunan akurasi masing-masing sebesar 0.03 dan 0.02, yang menunjukkan bahwa kepuasan kerja dan jabatan memiliki dampak penting. Sebaliknya, faktor-faktor seperti **BusinessTravel**, **WorkLifeBalance**, **YearsSinceLastPromotion**, **Education**, **Gender**, **Department**, **JobLevel**, **PerformanceRating**, **StandardHours**, **Over18**, dan **EmployeeCount** tidak memiliki pengaruh yang signifikan terhadap prediksi attrition dalam model ini, dengan penurunan akurasi yang sangat rendah atau nol.








## Conclusion

Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- action item 1
- action item 2
