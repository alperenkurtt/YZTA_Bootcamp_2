# System Architecture

## Genel Bakış

NorthCompass, yapay zekâ destekli modüler bir kariyer platformu olarak tasarlanmıştır. Sistem, kullanıcının yüklediği CV ile başvurmak istediği iş ilanını analiz ederek kişiselleştirilmiş geri bildirimler üretmektedir.

Sprint 1 kapsamında sistemin temel mimarisi oluşturulmuş ve ilk çalışan prototip geliştirilmiştir.

---

## Sistem Bileşenleri

### Kullanıcı

Kullanıcı sisteme;

- CV'sini yükler.
- Başvurmak istediği iş ilanını ekler.

---

### Veri Katmanı

Sistem, yüklenen CV ve iş ilanı metinlerini okuyarak analiz sürecine hazır hale getirir.

Sprint 1 kapsamında örnek veriler `sample_data` klasörü üzerinden okunmaktadır.

---

### Yapay Zekâ Analiz Katmanı

Google Gemini API kullanılarak;

- CV analiz edilir.
- İş ilanı analiz edilir.
- İki metin karşılaştırılır.
- Yapay zekâ tarafından öneriler oluşturulur.

---

### Sonuç Katmanı

Analiz sonucunda kullanıcıya;

- CV değerlendirmesi
- İş ilanı uyumluluğu
- Geliştirme önerileri

sunulmaktadır.

---

## Sprint 1 Mimarisi

Sprint 1 sonunda sistem aşağıdaki akışa sahiptir.

```text
Kullanıcı
     │
     ▼
CV + İş İlanı
     │
     ▼
Python Uygulaması
     │
     ▼
Google Gemini API
     │
     ▼
AI Analizi
     │
     ▼
Analiz Sonucu
```

---

## Gelecek Sprintler

İlerleyen sprintlerde mimariye aşağıdaki modüllerin eklenmesi planlanmaktadır.

- ATS Analiz Modülü
- CV Eşleşme Skoru
- Ön Yazı Oluşturma Modülü
- Yapay Zekâ Destekli Mülakat Modülü
- Kariyer Yol Haritası Modülü
- Başvuru Takip Sistemi
- Web Arayüzü

Bu modüller mevcut mimari üzerine eklenerek sistemin ölçeklenebilir şekilde geliştirilmesi hedeflenmektedir.

