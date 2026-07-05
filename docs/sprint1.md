# Sprint 1 Raporu

## Sprint Bilgileri

**Sprint:** Sprint 1

**Proje:** NorthCompass

**Sprint Amacı:**
Projenin temel altyapısını oluşturmak, yapay zekâ entegrasyonunu gerçekleştirmek ve CV ile iş ilanını analiz edebilen ilk çalışabilir prototipi geliştirmek.

---

## Sprint Hedefleri

Sprint 1 kapsamında aşağıdaki hedefler belirlenmiştir.
- GitHub proje yapısının oluşturulması
- Python proje altyapısının hazırlanması
- Google Gemini API entegrasyonunun gerçekleştirilmesi
- Örnek CV ve iş ilanı verilerinin hazırlanması
- İlk analiz akışının geliştirilmesi
- Proje dokümantasyonunun hazırlanması

---

## Sprint Board (Proje Takibi)

Sprint 1 sürecinde görevlerin planlanması, dağıtımı ve takibi GitHub Project Board üzerinden Kanban ilkelerine uygun olarak gerçekleştirilmiştir. Tüm hedefler başarıyla tamamlanmıştır.

![Sprint Board](Sprint 1 Board.png)

---

## Daily Scrum Notları

### Gün 1
- Proje fikri belirlendi ve ürün vizyonu oluşturuldu.
- GitHub deposu (repository) ve temel klasör yapısı kuruldu.

### Gün 2
- README ve temel bağımlılıkları içeren requirements.txt dosyaları hazırlandı.
- Kullanılacak mimari altyapı tartışıldı ve belgelendi.

### Gün 3
- Google Gemini API entegrasyonu tamamlandı ve `ai_analyzer.py` modülü yazıldı.
- Test süreçlerinde kullanılmak üzere örnek CV ve iş ilanı metinleri oluşturuldu.

### Gün 4
- Proje mimarisi modüler hale getirilerek `utils/` altına taşındı.
- Product Backlog, Roadmap, User Stories ve Architecture dokümanları hazırlanarak sprint teslimine hazır hale getirildi.

---

## Tamamlanan Çalışmalar

Sprint boyunca aşağıdaki çalışmalar tamamlanmıştır.

| Çalışma | Durum |
|---------|--------|
| GitHub deposunun oluşturulması | Tamamlandı |
| Proje klasör yapısının hazırlanması | Tamamlandı |
| Python geliştirme ortamının hazırlanması | Tamamlandı |
| Google Gemini API entegrasyonu | Tamamlandı |
| Örnek CV verisinin hazırlanması | Tamamlandı |
| Örnek iş ilanı verisinin hazırlanması | Tamamlandı |
| İlk AI analiz akışının geliştirilmesi | Tamamlandı |
| README hazırlanması | Tamamlandı |
| Product Backlog hazırlanması | Tamamlandı |
| User Stories hazırlanması | Tamamlandı |
| System Architecture hazırlanması | Tamamlandı |
| Roadmap hazırlanması | Tamamlandı |

---

## Sprint Çıktısı (MVP)

Sprint 1 sonunda geliştirilen prototip aşağıdaki işlemleri gerçekleştirebilmektedir:
- Örnek bir CV dosyasını okuyabilmektedir.
- Örnek bir iş ilanı dosyasını okuyabilmektedir.
- Her iki metni Google Gemini API kullanarak analiz edebilmektedir.
- CV ile iş ilanı arasındaki uyuma ilişkin yapay zekâ destekli geri bildirim oluşturabilmektedir.

---

## Sprint Review (Değerlendirme)

Sprint 1 hedefleri eksiksiz şekilde tamamlanmıştır. 
- Projenin temel sürdürülebilir mimarisi oluşturuldu.
- İlk çalışan MVP (Minimum Viable Product) başarıyla geliştirildi.
- Google Gemini API entegrasyonu ile yapay zekâ yetenekleri sisteme dahil edildi.
- Sonraki sprintler için ürün yol haritası (Roadmap) netleştirildi.

---

## Sprint Retrospective

### İyi Gidenler
- Projenin temel mimarisi ve klasör yapısı çok temiz ve modüler kuruldu.
- Yapay zekâ entegrasyonu hedeflenen süreden daha hızlı tamamlandı.
- Dokümantasyon süreçleri (Architecture, Backlog vb.) plana sadık kalınarak eksiksiz yürütüldü.

### Geliştirilecek Noktalar / Sonraki Sprint Hedefleri
- İkinci sprintte komut satırı yerine daha kullanışlı bir kullanıcı arayüzü (UI) geliştirilecek.
- ATS uyumluluk analizi, CV - İş İlanı eşleşme skoru ve eksik beceri analizi gibi daha gelişmiş analiz algoritmaları eklenecek.
- Kullanıcıların kendi CV'lerini doğrudan sisteme yükleyebileceği dinamik dosya yükleme desteği sağlanacak.

