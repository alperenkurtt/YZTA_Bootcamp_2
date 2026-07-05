# Sistem Mimarisi (System Architecture)

## Genel Bakış

NorthCompass, yapay zekâ destekli modüler ve ölçeklenebilir bir kariyer platformu olarak tasarlanmıştır. Sistem, kullanıcının sağladığı CV ile başvurmak istediği iş ilanını analiz ederek kişiselleştirilmiş geri bildirimler üretmektedir. 

Sprint 1 kapsamında sistemin temel katmanlı mimarisi oluşturulmuş, modüler kod yapısı kurulmuş ve ilk çalışan prototip geliştirilmiştir.

---

## Sistem Bileşenleri ve Katmanlı Yapı

Proje, sürdürülebilirlik ve bakım kolaylığı açısından modüler bir katman yapısı (Modular Monolith) temel alınarak geliştirilmektedir.

### 1. Sunum ve Giriş Katmanı (Presentation & Input Layer)
* **Bileşenler:** `main.py`
* **Görevi:** Sistem akışını başlatır, girdi verilerini ilgili modüllere dağıtır ve çıkan analiz sonuçlarını son kullanıcıya veya terminal arayüzüne sunar.

### 2. Veri ve Dosya İşleme Katmanı (Data & File Processing Layer)
* **Bileşenler:** `utils/file_reader.py`
* **Görevi:** `sample_data/` dizininden veya dış kaynaklardan gelen ham CV ve iş ilanı metinlerini okur. Verileri temizleyerek Yapay Zekâ katmanının işleyebileceği string formatına dönüştürür.

### 3. Yapay Zekâ ve Analiz Katmanı (AI & Analysis Layer)
* **Bileşenler:** `utils/ai_analyzer.py`, Google Gemini API
* **Görevi:** Sistem güvenliği için `.env` (python-dotenv) üzerinden beslenen API anahtarını kullanır. Temizlenen metinleri, optimize edilmiş prompt şablonları (Prompt Engineering) eşliğinde Google Gemini modeline iletir ve dönen semantik analiz sonuçlarını işler.

---

## Sprint 1 Mimari Akışı

Sprint 1 sonunda sistem veri akışı ve bileşen etkileşimi şu şekildedir:

```text
[Veri Kaynakları: sample_cv & sample_job]
                  │
                  ▼
      [utils/file_reader.py] (Metin Okuma ve Çeviri)
                  │
                  ▼
             [main.py] (Merkezi Yönetim ve Akış Kontrolü)
                  │
                  ▼
      [utils/ai_analyzer.py] (Prompt Yönetimi & API Güvenliği)
                  │
                  ▼
        [Google Gemini API] (Semantik Analiz Motoru)
                  │
                  ▼
         [Terminal / Çıktı] (Sonuç Raporlama)

---

### Gelecek Sprintlerde Planlanan Mimari Yapı

Sprint 1 sonunda sistemin temel analiz akışı başarıyla oluşturulmuş ve ilk çalışan prototip geliştirilmiştir. İlerleyen sprintlerde mevcut katmanlı mimari, gevşek bağlı (loosely coupled) tasarım ilkelerine uygun olarak aşağıdaki modüllerle genişletilecektir[cite: 1]:

* **ATS Uyum Analiz Modülü:** CV metninin kurumsal tarama sistemlerine uyumluluğunu ölçen semantik kontrol katmanı[cite: 1].
* **CV – İş İlanı Eşleşme ve Puanlama Modülü:** Aday ile pozisyon arasındaki uyumu matematiksel verilere ve skorlara döken analiz motoru[cite: 1].
* **CV Geliştirme ve Optimizasyon Modülü:** Eksik alanları tespit ederek yapay zekâ destekli nokta atışı cümle önerileri sunan yapı[cite: 1].
* **Ön Yazı (Cover Letter) Oluşturma Modülü:** Başvurulacak pozisyona özel, kişiselleştirilmiş ön yazılar üreten üretken yapay zekâ katmanı[cite: 1].
* **Yapay Zekâ Destekli Mülakat Simülasyonu:** Rol bazlı mülakat senaryoları üreten ve adayın yanıtlarını analiz eden interaktif modül[cite: 1].
* **Kariyer Yol Haritası ve Beceri Analizi:** Sektörel trendlere göre adayın profilini inceleyip kariyer patikası çizen veri bileşeni[cite: 1].
* **Kişiselleştirilmiş Öğrenme Önerileri:** Tespit edilen eksik becerileri kapatmak için adaya özel eğitim ve kaynak tavsiye eden motor[cite: 1].
* **Başvuru Takip Sistemi:** Kullanıcının tüm iş süreçlerini tek bir panelden yönetmesini sağlayan CRM benzeri yönetim katmanı[cite: 1].
* **Web Tabanlı Kullanıcı Arayüzü:** Mevcut Python çekirdeğini (core) bir web API'sine bağlayarak son kullanıcıya ulaştıran arayüz entegrasyonu[cite: 1].

Bu modüller, mevcut mimari altyapı üzerine kademeli (incremental) olarak entegre edilecektir[cite: 1]. Böylece NorthCompass'un, yalnızca anlık bir CV analizi yapan dar kapsamlı bir araçtan; kullanıcıların iş arama ve kariyer gelişim süreçlerini uçtan uca destekleyen, yüksek pazar potansiyeline sahip bütünleşik bir **Yapay Zekâ Kariyer Platformuna** dönüştürülmesi hedeflenmektedir[cite: 1].
