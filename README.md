# NorthCompass

İş başvurularını daha etkili, kişiselleştirilmiş ve başarılı hale getirmek amacıyla geliştirilen yapay zekâ destekli kariyer platformu.

---

# Takım Bilgileri

**Takım Adı:** Takım-2

| Rol | İsim |
|------|------|
| Product Owner | Ezgigül Karaca |
| Scrum Master | Alperen Kurt |
| Developer | Taha Bozkurt |
| Developer | İlknur Küçükberber |

---

# Ürün Bilgileri

**Ürün Adı:** NorthCompass

## Ürün Açıklaması

NorthCompass, kullanıcıların başvurmayı hedefledikleri iş ilanına göre CV'lerini analiz eden, iş ilanı ile CV arasındaki uyumu değerlendiren ve kişiselleştirilmiş öneriler sunan yapay zekâ destekli bir kariyer platformudur.

## Hedef Kitle

- Üniversite öğrencileri
- Yeni mezunlar
- Staj arayan adaylar
- İş değiştirmek isteyen profesyoneller

## Temel Özellikler

- CV Analizi
- İş İlanı Analizi
- ATS Uyum Analizi
- CV – İş İlanı Eşleşme Analizi
- Eksik Beceri Analizi
- CV Geliştirme Önerileri

---

# Proje Hakkında

Günümüzde birçok aday farklı şirketlere aynı CV ile başvuru yapmaktadır. Ancak her şirket ve her pozisyon farklı teknik beceriler, deneyimler ve anahtar kelimeler beklemektedir. Özellikle ATS (Aday Takip Sistemleri), CV'leri işe alım uzmanlarına ulaşmadan önce belirli kriterlere göre değerlendirmektedir. Bu nedenle adaylar yeterli bilgi ve deneyime sahip olsalar bile, CV'leri iş ilanıyla yeterince uyumlu olmadığı için değerlendirme sürecinin dışında kalabilmektedir.

NorthCompass bu problemi yapay zekâ desteğiyle çözmeyi hedeflemektedir. Sistem, kullanıcının CV'sini ve başvuracağı iş ilanını birlikte analiz ederek güçlü yönleri, geliştirilmesi gereken alanları ve başvuru başarısını artırabilecek önerileri kullanıcıya sunar.

Uzun vadeli hedefimiz yalnızca CV analizi yapan bir araç geliştirmek değil; iş arama sürecinin tamamına rehberlik eden, kullanıcıların kariyer gelişimini destekleyen kapsamlı bir yapay zekâ platformu oluşturmaktır.

---

# Problem

İş arama sürecinde adayların karşılaştığı en önemli problemlerden biri, her başvuru için CV'lerini ilgili pozisyona göre yeniden düzenlemek zorunda olmalarıdır.

Her iş ilanı farklı beceriler, deneyimler ve anahtar kelimeler içermektedir. Buna rağmen birçok aday aynı CV ile farklı pozisyonlara başvurmaktadır. Bu durum ATS sistemlerinde düşük eşleşme oranına neden olmakta ve adayların daha ilk aşamada elenmesine yol açabilmektedir.

Adayların hangi becerilerinin eksik olduğu, CV'lerinde hangi deneyimlerini daha iyi vurgulamaları gerektiği veya başvuru başarılarını artırmak için neleri geliştirmeleri gerektiği konusunda da yeterli geri bildirim sunan kapsamlı bir çözüm bulunmamaktadır.

---

# Çözüm

NorthCompass, kullanıcıların başvuru süreçlerini daha bilinçli ve verimli yönetebilmeleri için yapay zekâ destekli analizler sunmayı amaçlamaktadır.

Platform;

- CV'yi analiz eder.
- İş ilanını analiz eder.
- CV ile iş ilanı arasındaki uyumu değerlendirir.
- ATS uyumluluğu hakkında geri bildirim sunar.
- Eksik beceri ve anahtar kelimeleri belirler.
- CV'nin daha güçlü hale getirilebilmesi için kişiselleştirilmiş öneriler üretir.

---

# Ürün Vizyonu

NorthCompass modüler bir yapıda geliştirilmektedir.

İlk aşamada temel CV analizi ve iş ilanı eşleştirmesi üzerine odaklanılmaktadır. İlerleyen sprintlerde platformun aşağıdaki modüllerle genişletilmesi planlanmaktadır.

## Mevcut Modüller (Sprint 1)

- CV Analizi
- İş İlanı Analizi
- Google Gemini API Entegrasyonu
- Yapay Zekâ Destekli İlk Analiz Akışı

## Planlanan Modüller

- ATS Uyum Puanı
- CV – İş İlanı Eşleşme Skoru
- CV Geliştirme Önerileri
- Yapay Zekâ Destekli Mülakat Simülasyonu
- Ön Yazı (Cover Letter) Oluşturma
- Kariyer Yol Haritası
- Eksik Beceri Analizi
- Öğrenme Önerileri
- Maaş Analizi
- Başvuru Takip Sistemi

Bu yapı sayesinde NorthCompass'un yalnızca CV analizi yapan bir uygulama değil, kullanıcıların kariyer yolculuğunu destekleyen bütünleşik bir platforma dönüşmesi hedeflenmektedir.

---

# Sprint 1

Sprint 1 kapsamında projenin temel altyapısı oluşturulmuş ve ilk çalışabilir prototip geliştirilmiştir.

Bu sprintte tamamlanan çalışmalar:

- GitHub proje yapısının oluşturulması
- Python proje altyapısının hazırlanması
- Google Gemini API entegrasyonu
- Örnek CV ve iş ilanı verilerinin hazırlanması
- İlk analiz akışının geliştirilmesi
- Proje dokümantasyonunun hazırlanması

Sprint 1 sonunda geliştirilen prototip;

- Örnek bir CV dosyasını okuyabilmektedir.
- Örnek bir iş ilanını okuyabilmektedir.
- Her iki metni Google Gemini API ile analiz edebilmektedir.
- CV ile iş ilanı arasındaki uyuma ilişkin yapay zekâ destekli geri bildirim oluşturabilmektedir.

**Not:** Sprint 1 kapsamında kullanıcıdan dosya yükleme özelliği yerine örnek CV ve iş ilanı dosyaları kullanılarak ilk çalışan prototip geliştirilmiştir. Gerçek kullanıcı yükleme desteği ilerleyen sprintlerde eklenecektir.

---

# Kullanılan Teknolojiler

- Python
- Google Gemini API
- python-dotenv
- Git
- GitHub

---

# Proje Yapısı

```text
NorthCompass/
│
├── docs/
│   ├── sprint1.md
│   ├── product_backlog.md
│   ├── user_stories.md
│   ├── architecture.md
│   └── roadmap.md
│
├── sample_data/
│   ├── sample_cv.txt
│   └── sample_job.txt
│
├── utils/
│   ├── ai_analyzer.py
│   └── file_reader.py
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

---

# Kurulum

Projeyi bilgisayarınıza indirin.

```bash
git clone https://github.com/ezgigulkaraca/NorthCompass.git
cd NorthCompass
```

Gerekli kütüphaneleri yükleyin.

```bash
pip install -r requirements.txt
```

`.env.example` dosyasını `.env` olarak kopyalayın ve Google Gemini API anahtarınızı ekleyin.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Projeyi çalıştırın.

```bash
python main.py
```

---

# Gelecek Hedefi

NorthCompass'un amacı yalnızca adayların CV'lerini analiz eden bir uygulama geliştirmek değildir.

Uzun vadede kullanıcıların iş arama sürecini tek bir platform üzerinden yönetebilecekleri yapay zekâ destekli kapsamlı bir kariyer platformu oluşturulması hedeflenmektedir.

Platformun ilerleyen sürümlerinde kullanıcılar;

- Başvurularına özel CV önerileri alabilecek,
- Ön yazı oluşturabilecek,
- Yapay zekâ destekli mülakat simülasyonu yapabilecek,
- Eksik becerilerini analiz edebilecek,
- Kendilerine özel öğrenme önerileri alabilecek,
- Başvurularını tek panel üzerinden takip edebilecek,
- Kariyer gelişimlerini uzun vadeli olarak planlayabilecektir.

---

# Ekip

Bu proje, YZTA Bootcamp kapsamında Scrum metodolojisi kullanılarak geliştirilmektedir.

Sprint 1 sürecinde projenin temel altyapısı oluşturulmuş ve ilk çalışabilir prototip geliştirilmiştir. Proje, sonraki sprintlerde yeni özellikler eklenerek geliştirilmeye devam edecektir.
