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
