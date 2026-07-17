# Sistem Mimarisi (System Architecture)

## Genel Bakış

NorthCompass, yapay zekâ destekli modüler ve ölçeklenebilir bir kariyer platformu olarak tasarlanmıştır. Sistem, kullanıcının sağladığı CV ile başvurmak istediği iş ilanını analiz ederek kişiselleştirilmiş geri bildirimler üretmektedir.

Sprint 1 kapsamında sistemin temel katmanlı mimarisi oluşturulmuş, modüler kod yapısı kurulmuş ve ilk çalışan prototip geliştirilmiştir.

---

## Sistem Bileşenleri ve Katmanlı Yapı

Proje, sürdürülebilirlik ve bakım kolaylığı açısından modüler bir katman yapısı (Modular Monolith) temel alınarak geliştirilmektedir.

### 1. Sunum ve Giriş Katmanı (Presentation & Input Layer)

**Bileşenler:** `main.py`

**Görevi:** Sistem akışını başlatır, girdi verilerini ilgili modüllere yönlendirir ve analiz sonuçlarını kullanıcıya sunar.

### 2. Veri ve Dosya İşleme Katmanı (Data & File Processing Layer)

**Bileşenler:** `utils/file_reader.py`

**Görevi:** `sample_data/` klasöründeki CV ve iş ilanı metinlerini okuyarak analiz için uygun formata dönüştürür.

### 3. Yapay Zekâ ve Analiz Katmanı (AI & Analysis Layer)

**Bileşenler:** `utils/ai_analyzer.py`, Google Gemini API

**Görevi:** `.env` dosyasında bulunan API anahtarını kullanarak Google Gemini modeli ile iletişim kurar. Hazırlanan istem (prompt) üzerinden CV ve iş ilanını analiz eder, sonuçları uygulamaya döndürür.

---

## Sprint 1 Mimari Akışı

Sprint 1 sonunda sistemin veri akışı aşağıdaki gibidir.

```text
          sample_cv.txt           sample_job.txt
                 │                       │
                 └──────────┬────────────┘
                            │
                            ▼
                utils/file_reader.py
                            │
                            ▼
                       main.py
                            │
                            ▼
                 utils/ai_analyzer.py
                            │
                            ▼
                  Google Gemini API
                            │
                            ▼
                 Analiz Sonucu (Terminal)
```

---

## Sprint 2 Mimari Akışı

Sprint 2 sonunda sistemin veri akışı aşağıdaki gibidir.

```text
          sample_cv_2.txt          sample_job_2.txt
                 │                       │
                 └──────────┬────────────┘
                            │
                            ▼
                utils/file_reader.py
                            │
                            ▼
                       main.py
                            │
                            ▼
              utils/keyword_matcher.py
     (Requirements ayrıştırma + eşleşme skoru,
        eşleşen/eksik beceri listesi üretimi)
                            │
                            ▼
                 utils/ai_analyzer.py
     (skor ve eksik beceriler prompt'a enjekte edilir)
                            │
                            ▼
                  Google Gemini API
     (güçlü yönler, ATS değerlendirmesi, CV önerileri)
                            │
                            ▼
      Analiz Sonucu (Terminal): Deterministik Skor
                + Yapay Zekâ Yorumu
```

---

## Gelecek Sprintlerde Planlanan Mimari

Sprint 1 sonunda sistemin temel analiz akışı başarıyla oluşturulmuş ve ilk çalışan prototip geliştirilmiştir.

İlerleyen sprintlerde mevcut mimarinin aşağıdaki modüllerle genişletilmesi planlanmaktadır:

- ATS Uyum Analiz Modülü
- CV – İş İlanı Eşleşme ve Puanlama Modülü
- CV Geliştirme ve Optimizasyon Modülü
- Ön Yazı (Cover Letter) Oluşturma Modülü
- Yapay Zekâ Destekli Mülakat Simülasyonu
- Kariyer Yol Haritası ve Beceri Analizi
- Kişiselleştirilmiş Öğrenme Önerileri
- Başvuru Takip Sistemi
- Web Tabanlı Kullanıcı Arayüzü

Bu modüller mevcut mimari üzerine kademeli olarak entegre edilerek NorthCompass'un yalnızca CV analizi yapan bir uygulamadan, kullanıcıların iş başvurusu ve kariyer gelişim süreçlerini uçtan uca destekleyen bütünleşik bir yapay zekâ kariyer platformuna dönüştürülmesi hedeflenmektedir.


Sprint 2 sonunda ATS uyumluluk analizi, CV – İş İlanı eşleşme/puanlama ve eksik beceri analizi modülleri deterministik eşleştirme katmanı ve güncellenmiş prompt yapısı ile tamamlanmıştır.

İlerleyen sprintlerde mevcut mimarinin aşağıdaki modüllerle genişletilmesi planlanmaktadır:


Optimize Edilmiş CV Oluşturma Modülü
Ön Yazı (Cover Letter) Oluşturma Modülü
Yapay Zekâ Destekli Mülakat Simülasyonu
Kariyer Yol Haritası ve Beceri Analizi
Kişiselleştirilmiş Öğrenme Önerileri
Başvuru Takip Sistemi
Web Tabanlı Kullanıcı Arayüzü


Bu modüller mevcut mimari üzerine kademeli olarak entegre edilerek NorthCompass'un yalnızca CV analizi yapan bir uygulamadan, kullanıcıların iş başvurusu ve kariyer gelişim süreçlerini uçtan uca destekleyen bütünleşik bir yapay zekâ kariyer platformuna dönüştürülmesi hedeflenmektedir.