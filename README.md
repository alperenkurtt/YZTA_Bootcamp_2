## Takım İsmi
Yapay Zeka Ve Teknolojileri Akademisi Bootcamp 2

## Takım Üyeleri
- ***Ezgigül Karaca*** - Product Owner
- ***Alperen Kurt*** - Scrum Master

## Proje İsmi
Fluentie

## Proje Açıklaması
Fluentie kullanıcıların yabancı dil öğrenme sürecindeki konuşma çekincelerini ortadan kaldırmak için tasarlanmış, yapay zeka destekli etkileşimli bir İngilizce pratik asistanıdır.

Geleneksel dil öğrenme uygulamalarının aksine, kullanıcıyla gerçek bir insan gibi doğal bir sohbet akışı sürdürür. Sohbet esnasında kullanıcının yaptığı gramer, kelime kullanımı veya cümle yapısı hatalarını anlık olarak tespit eder; sohbeti bölmeden, nazik bir şekilde düzeltir ve konunun devam etmesini sağlayacak açık uçlu sorular sorarak pratik süresini maksatlı olarak uzatır.

## Proje Özellikleri
- Anlık Gramer ve Kelime Düzeltmesi
- Akıcı ve Doğal Sohbet Akışı
- Soru Sorma ve Diyaloğu Teşvik Etme
- Sabırlı ve Destekleyici Yaklaşım
- Esnek Konu Çeşitliliği

## Hedef Kitle
- A2 - B2 Seviyesindeki Dil Öğrenicileri
- Konuşma Çekincesi Olanlar
- Maliyet/Zaman Kısıtı Olanlar
- Mülakat veya Sınavlara Hazırlananlar

## Sprint 1 — Mimari + İlk İstek

- Proje yapısı: llm_client.py (OpenRouter'a OpenAI SDK ile bağlanan sarmalayıcı, base_url=https://openrouter.ai/api/v1), prompts.py (system prompt ayrı tutulacak, ileride değiştirmek kolay olsun diye)
- requirements.txt (openai, python-dotenv, streamlit)
- Basit bir test scripti: tek mesaj gönder → gpt-4o-mini cevabı al → terminale yazdır
- Çıktı: API bağlantısının çalıştığının kanıtı (tek seferlik istek-cevap)

## Sprint 2 — Terminalde Tam Sohbet Döngüsü

- Konuşma geçmişi (mesaj listesi: system + user + assistant turn'leri) — botun bağlamı unutmaması için şart
- CLI döngüsü: kullanıcıdan input al → geçmişe ekle → modele gönder → cevabı yazdır → exit/quit ile çıkış
- Temel hata yönetimi (API hatası, boş input, Ctrl+C)
- Çıktı: Terminalde uçtan uca çalışan, hataları düzelten ve sohbete devam eden bot

## Sprint 3 — Streamlit Web Arayüzü

- st.chat_message / st.chat_input ile sohbet arayüzü
- st.session_state ile konuşma geçmişi (Sprint 2'deki mantığın aynısı, sadece terminal yerine web)
- llm_client.py aynen tekrar kullanılacak, kod tekrarı yok
- Çıktı: streamlit run app.py ile tarayıcıda çalışan sohbet botu