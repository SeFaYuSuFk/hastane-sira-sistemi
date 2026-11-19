# Hastane Sıra Sistemi (Tek Yönlü Bağlı Liste)

Kapadokya Üniversitesi **BGY201 Veri Yapıları** dersi kapsamında Python ile geliştirilmiş, tek yönlü bağlı liste (*Singly Linked List*) tabanlı ve **FIFO (İlk Giren İlk Çıkar)** mantığıyla çalışan hastane kayıt ve muayene sıra sistemidir.

- **Öğrenci:** Sefa Yusuf Kütük (`25905007`)
- **Bölüm:** Yazılım Geliştirme

## Özellikler

- **`Hasta` Sınıfı:** Hastanın adı, yaşı ve şikâyet bilgisini tutar.
- **`Node` Sınıfı:** `Hasta` nesnesini ve sonraki düğüme işaret eden `next` referansını tutar.
- **`LinkedList` Sınıfı:** `head` referansı üzerinden sona hasta ekleme (`O(n)`), baştan hasta çıkarma (`O(1)`) ve kayıt sırasına göre listeleme işlemlerini yönetir.
- **Girdi Doğrulama & Uç Durum Koruması:** Boş/hatalı metin ve yaş girişleri, `None` nesne ekleme, boş listeden art arda çıkarma ve uzun listelerde `RecursionError` oluşmaması için iteratif döngü korumaları içerir.
- **Otomatik Test & Stress Doğrulaması:** Ödevdeki 3 sınama senaryosu ile birlikte 30 ve 500 hastalı sınır durum testlerini içerir.

## Çalıştırma

```bash
python SefaYusufKutuk_YazilimGelistirme_Quiz1_Kod.py
```

Menüden:
- `1`: Yeni hasta ekle (ziyaret edilen düğüm sayısını gösterir)
- `2`: Sıradaki hastayı muayeneye al (çıkar)
- `3`: Bekleyen hastaları listele
- `4`: Ödev test senaryolarını ve uç durum doğrulamasını çalıştır
- `0`: Çıkış
