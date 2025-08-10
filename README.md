# 📌 NMF ile Türkçe Haber Konu Modelleme ve Benzerlik Analizi

Bu proje, **Doğrusal Olmayan Matris Çarpanlarına Ayırma (NMF)** yöntemi kullanarak Türkçe haber metinlerinden konu başlıkları çıkarmayı ve belirli bir haber metnine en çok benzeyen diğer haberleri bulmayı amaçlamaktadır.  

---

## 🚀 Projenin Amacı

- Haber metinlerini **TF-IDF** ile sayısal vektörlere dönüştürmek  
- **NMF (Non-negative Matrix Factorization)** ile haberleri konu başlıklarına ayırmak  
- Her konu için en sık geçen **anahtar kelimeleri** bulmak  
- Seçilen bir haber ile **en çok benzerlik gösteren diğer haberleri** tespit etmek  

---

## 📂 Veri Seti

Proje `news.xls` isimli Excel dosyasını kullanır. [Excel_Folder](news.xls).   


---

## 🛠 Kullanılan Kütüphaneler

- **pandas** → Veri işleme  
- **scikit-learn**  
  - `TfidfVectorizer` → TF-IDF vektörizasyonu  
  - `NMF` → Konu modelleme  
  - `normalize` → Benzerlik hesaplama için normalizasyon  
- **numpy** → Sayısal işlemler

---

## 📊 Adım Adım Çalışma Mantığı

1. **Veri Ön İşleme**
   - Boş veriler kontrol edilir (`isna()`).
   - Tekrar eden haberler kaldırılır (`drop_duplicates()`).
   - Türkçe stop-word listesi ile gereksiz kelimeler temizlenir.
   - Satır sonları (`\n`) boşlukla değiştirilir.

2. **TF-IDF Vektörizasyon**
   - Haber metinleri **1-2 kelime grubu (ngram)** olacak şekilde vektörleştirilir.
   - `max_df=0.95` ve `min_df=2` ile çok sık veya çok nadir geçen kelimeler filtrelenir.

3. **NMF Konu Modelleme**
   - `n_components=10` ile 10 farklı konu başlığı bulunur.
   - Her konu için en sık geçen **10 anahtar kelime** yazdırılır.

4. **Benzerlik Hesaplama**
   - **W matrisi** normalize edilir.
   - Seçilen bir haber (ör. `iloc[0]`) ile diğer haberler arasındaki **kosinüs benzerliği** hesaplanır.
   - En çok benzeyen haberler ekrana yazdırılır.

---

## 📌 Örnek Çıktı

```python

from sklearn.preprocessing import normalize

norm_features = normalize(W)

df = pd.DataFrame(norm_features, index=df['content'])

current_topic = df.iloc[0]  

similarity = df.dot(current_topic)

print(similarity.nlargest())

```

**Konu Anahtar Kelimeleri:**


Dışişleri Bakanı Davutoğlu, Yunanistan ile Türkiye arasındaki farlılıkların ortak vizyon ile çözülebileceğini söyledi.  **1.000000**

Milli Savunma Bakanı İsmet Yılmaz da Suriye'deki olaylara ilişkin ABD'nin Türkiye'ye asker gönderdiği iddialarını yalanladı.  **0.999985**

FRANSA ve Türkiye arasında ilişkilerin yeniden ısınması için atağa geçen François Hollande hükümeti, Dışişleri Bakanı Ahmet Davutoğlu ile görüşmeye hazırlanıyor. **0.999977**

Türkiyenin dışişleri bakanı mı, Somalinin milli kahramanı mı? Ahmet Davutoğluna Somalide gösterilen iltifat insana bu soruyu sorduruyor. **0.999934**

İran Dışişleri Bakanlığı Sözcüsü Ramin Mihmanperest, Patriot füze bataryalarının olası savaşta İsraili İran füzelerine karşı koruma amacıyla Türkiyede konuşlandırılmak istendiğini iddia etti. **0.999766**
