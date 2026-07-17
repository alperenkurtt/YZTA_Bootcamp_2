# Sprint 2 Raporu

## Sprint Bilgileri

* **Sprint:** Sprint 2
* **Proje:** NorthCompass
* **Sprint Amacı:** CV ile iş ilanı arasındaki karşılaştırma mekanizmasını, koddan hesaplanan deterministik bir eşleşme skoru ile desteklemek; yapay zekâ katmanının görevini bu veriler üzerinden nitel yorum üretmeye daraltmak.

---

## Sprint Hedefleri

Sprint 2 kapsamında aşağıdaki hedefler belirlenmiştir ve tamamı başarıyla yerine getirilmiştir:

* Sprint 1'deki tek parça, serbest metin tabanlı analiz akışının yeniden yapılandırılması.
* İş ilanı gereksinimlerini ayrıştırıp CV ile karşılaştıran, deterministik bir eşleştirme modülünün geliştirilmesi.
* Yapay zekâ promptunun, uyum yüzdesini kendi hesaplamak yerine koddan gelen veriyi yorumlayacak şekilde güncellenmesi.
* Gemini API anahtarının güvenli şekilde yapılandırılması ve sistemin gerçek API ile uçtan uca test edilmesi.
* Encoding kaynaklı bir konsol hatasının giderilmesi.
* İkinci bir örnek senaryo ile sistemin doğrulanması.

---

## Sprint Board (Proje Takibi)

Sprint 2 sürecinde görevlerin planlanması, dağıtımı ve takibi GitHub Project Board üzerinde Kanban ilkelerine uygun olarak sürdürülmüştür. İş listesindeki tüm görevler "Done" sütununa taşınarak süreç tamamlanmıştır.

---

## Çalışma Notları — 09.07.2026

* Sprint 1'deki tek parça, serbest metin analiz akışı yeniden yapılandırıldı.
* `utils/keyword_matcher.py` adında yeni bir modül oluşturuldu; iş ilanındaki "Requirements" bölümünü çıkarıp CV ile karşılaştıran, deterministik (koddan hesaplanan) bir eşleşme skoru ve eksik/eşleşen beceri listesi üreten fonksiyonlar yazıldı.
* `utils/ai_analyzer.py` içindeki prompt güncellendi; artık uyum yüzdesi Gemini'den istenmiyor, koddan gelen skor ve eksik beceriler prompt'a veriliyor; Gemini yalnızca güçlü yönler, ATS uyumluluğu değerlendirmesi ve somut CV geliştirme önerileri üretiyor.
* `main.py`, bu yeni akışa göre güncellendi.
* `docs/product_backlog.md`'de PB-06, PB-07, PB-08, PB-09 durumları "Planlandı"dan "Tamamlandı"ya çevrildi.
* Gemini API anahtarı Google AI Studio'dan alınıp `.env` dosyasına eklendi, bağımlılıklar (`google-generativeai`, `python-dotenv`) kuruldu ve proje gerçek API ile uçtan uca test edildi.
* Windows konsolunda Türkçe karakterlerin bozuk çıkmasına neden olan encoding sorunu `sys.stdout.reconfigure(encoding="utf-8")` ile çözüldü.
* Farklı bir senaryoyu test etmek için ikinci bir örnek CV ve iş ilanı (`sample_cv_2.txt`, `sample_job_2.txt` — Veri Analisti pozisyonu) oluşturuldu ve bunlarla da uçtan uca doğrulama yapıldı (%83 eşleşme skoru, doğru sonuçlar).

---

## Tamamlanan Çalışmalar

| Çalışma | Durum |
| :--- | :--- |
| `utils/keyword_matcher.py` modülünün geliştirilmesi | Tamamlandı |
| İş ilanı "Requirements" bölümünün ayrıştırılması (`extract_requirements`) | Tamamlandı |
| Deterministik eşleşme skoru ve eşleşen/eksik beceri listesi üretimi (`match_keywords`) | Tamamlandı |
| `utils/ai_analyzer.py` prompt yapısının güncellenmesi | Tamamlandı |
| `main.py` akışının yeni eşleştirme adımına göre güncellenmesi | Tamamlandı |
| Product Backlog durumlarının güncellenmesi (PB-06, PB-07, PB-08, PB-09) | Tamamlandı |
| Gemini API anahtarının `.env` dosyasına eklenmesi ve bağımlılıkların kurulması | Tamamlandı |
| Sistemin gerçek API ile uçtan uca test edilmesi | Tamamlandı |
| Windows konsolu encoding (Türkçe karakter) sorununun giderilmesi | Tamamlandı |
| İkinci örnek senaryonun (Veri Analisti) hazırlanması ve doğrulanması | Tamamlandı |

---

## Sprint Çıktısı (MVP)

Sprint 2 sonunda geliştirilen sistem aşağıdaki işlevleri gerçekleştirmektedir:

* İş ilanındaki gereksinim listesini otomatik olarak ayrıştırabilmektedir.
* CV ile bu gereksinimleri karşılaştırarak koddan hesaplanan, tutarlı bir eşleşme skoru ile eşleşen/eksik beceri listesi üretebilmektedir.
* Bu deterministik verileri Gemini modeline besleyerek güçlü yönler, ATS uyumluluğu değerlendirmesi ve eksik becerilere dayalı somut CV geliştirme önerileri içeren bir analiz raporu oluşturabilmektedir.
* İkinci bir örnek senaryo (Veri Analisti pozisyonu) üzerinde uçtan uca doğrulanmış, %83 eşleşme skoru ile tutarlı sonuçlar üretmiştir.

---

## Sprint Review (Değerlendirme)

Sprint 2 planlamasına tam uyum sağlanmıştır:

* Uyum yüzdesi hesaplaması yapay zekâdan koda taşınarak sonuçların tutarlılığı ve ölçülebilirliği artırılmıştır.
* Gemini API'nin sorumluluğu, ölçülebilir veriler üzerine nitel yorum eklemekle sınırlandırılarak prompt daha odaklı hale getirilmiştir.
* Sistem gerçek API anahtarı ile uçtan uca test edilmiş ve iki farklı senaryoda doğrulanmıştır.
* Product backlog, tamamlanan işlere göre güncel tutulmuştur.

---

## Sprint Retrospective

### İyi Gidenler

* Eşleştirme mantığının koda taşınması, sonuçların ölçülebilirliğini ve tekrarlanabilirliğini önemli ölçüde artırdı.
* Gemini prompt'unun daraltılması, yapay zekâdan gelen yanıtların daha odaklı ve tutarlı olmasını sağladı.
* Encoding sorunu hızlı bir şekilde tespit edilip çözüldü ve ikinci bir senaryoyla sistem başarıyla doğrulandı.

### Geliştirilecek Noktalar ve Sonraki Sprint Hedefleri

* Sprint 3 kapsamında iş ilanına özel optimize edilmiş CV önerisi ve ön yazı (cover letter) oluşturma modüllerinin geliştirilmesi planlanmaktadır.
* Analiz sonuçlarının terminal çıktısı yerine daha okunabilir/yapılandırılmış bir formatta sunulması değerlendirilecektir.
* Kullanıcıların statik örnek dosyalar yerine kendi CV ve iş ilanı verilerini doğrudan sisteme yükleyebileceği esnek dosya işleme altyapısının kurulması gerekmektedir.
