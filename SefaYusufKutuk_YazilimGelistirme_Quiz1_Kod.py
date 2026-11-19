"""
BGY201 Veri Yapıları - Quiz Ödevi 1: Hastane Sıra Sistemi
Öğrenci: Sefa Yusuf Kütük (25905007)
Bölüm: Yazılım Geliştirme

Tek yönlü bağlı liste (Singly Linked List) kullanarak FIFO (İlk Giren İlk Çıkar)
mantığıyla çalışan, uç durumlara (edge-case) ve hatalı girdilere karşı korumalı
hastane kayıt ve muayene sıra sistemi.
"""


class Hasta:
    """Her hastanın temel bilgilerini (ad, yaş, şikâyet) tutan sınıf."""

    def __init__(self, ad: str, yas: int, sikayet: str) -> None:
        self.ad = str(ad).strip()
        self.yas = int(yas)
        self.sikayet = str(sikayet).strip()

    def __str__(self) -> str:
        return f"{self.ad} (Yaş: {self.yas}, Şikâyet: {self.sikayet})"


class Node:
    """Tek yönlü bağlı listenin her bir düğümünü temsil eden sınıf."""

    def __init__(self, hasta: Hasta) -> None:
        self.hasta = hasta  # Düğümde saklanan Hasta nesnesi
        self.next = None    # Sonraki düğüme işaret eden referans


class LinkedList:
    """Hastane sırasını tek yönlü bağlı liste ile yöneten sınıf."""

    def __init__(self) -> None:
        # Listenin başlangıç düğümü; liste boşken None değerini alır
        self.head = None

    def bos_mu(self) -> bool:
        """Sıranın boş olup olmadığını kontrol eder."""
        return self.head is None

    def hasta_ekle(self, hasta: Hasta) -> int:
        """
        Yeni hastayı bağlı listenin sonuna (kuyruğun arkasına) ekler ve
        sona ulaşmak için ziyaret edilen düğüm sayısını döndürür.
        Geçersiz nesne gelirse listeyi bozmadan -1 döndürür.
        """
        if not isinstance(hasta, Hasta):
            print("\n[HATA] Geçersiz hasta nesnesi! Sıraya yalnızca Hasta eklenebilir.")
            return -1

        yeni_dugum = Node(hasta)

        # Liste boşsa yeni düğüm doğrudan ilk düğüm (head) olur (0 düğüm ziyaret edilir)
        if self.head is None:
            self.head = yeni_dugum
            return 0

        # Liste boş değilse head'den başlayarak son düğüme (next == None) kadar ilerle
        # (Özyineleme yerine döngü kullanıldığı için çok uzun listelerde RecursionError oluşmaz)
        mevcut = self.head
        ziyaret_sayisi = 1
        while mevcut.next is not None:
            mevcut = mevcut.next
            ziyaret_sayisi += 1

        # Son düğümün next referansını yeni düğüme bağla
        mevcut.next = yeni_dugum
        return ziyaret_sayisi

    def siradaki_hastayi_cikar(self):
        """
        Sıranın başındaki (head) hastayı listeden çıkarır ve muayene bilgisini gösterir.
        Sıra boşsa kullanıcıyı bilgilendirir.
        """
        if self.head is None:
            print("\n[BİLGİ] Sıra boş! Muayene edilecek bekleyen hasta yok.")
            return None

        # İlk düğümü al, head'i bir sonraki düğüme kaydır
        cikarilan_dugum = self.head
        muayene_edilen = cikarilan_dugum.hasta
        self.head = cikarilan_dugum.next  # Tek hasta varsa head otomatik olarak None olur
        cikarilan_dugum.next = None       # Çıkarılan düğümün eski bağlantısını temizle

        print(f"\n[MUAYENE] Sıradaki hasta muayeneye alındı: {muayene_edilen.ad}")
        return muayene_edilen

    def bekleyenleri_listele(self) -> None:
        """Bekleyen tüm hastaları kayıt sırasına göre ad, yaş ve şikâyetleriyle listeler."""
        if self.head is None:
            print("\n[BİLGİ] Sıra boş! Bekleyen hasta bulunmamaktadır.")
            return

        print("\n" + "=" * 60)
        print("BEKLEYEN HASTA SIRASI (Kayıt Sırasına Göre - FIFO)")
        print("=" * 60)

        mevcut = self.head
        sira_no = 1
        zincir_gosterimi = ["HEAD"]

        while mevcut is not None:
            h = mevcut.hasta
            print(f"{sira_no}. Ad: {h.ad} | Yaş: {h.yas} | Şikâyet: {h.sikayet}")
            zincir_gosterimi.append(f"[{h.ad}]")
            mevcut = mevcut.next
            sira_no += 1

        zincir_gosterimi.append("None")
        print("-" * 60)
        print(f"Toplam Bekleyen Hasta: {sira_no - 1}")
        print("Bağlı Liste Yapısı   : " + " -> ".join(zincir_gosterimi))
        print("=" * 60)


def gecerli_metin_al(etiket: str, alan_adi: str) -> str:
    """
    Kullanıcıdan boş olmayan ve en az bir harf içeren geçerli bir metin alır.
    Sadece boşluk, sayı veya sembol girilmesini engeller.
    """
    while True:
        deger = input(etiket).strip()
        if not deger:
            print(f"  [UYARI] {alan_adi} boş bırakılamaz. Lütfen tekrar girin.")
            continue
        if not any(karakter.isalpha() for karakter in deger):
            print(f"  [UYARI] {alan_adi} en az bir harf içermelidir (yalnızca sayı/sembol olamaz).")
            continue
        return deger


def gecerli_yas_al() -> int:
    """Kullanıcıdan 0-130 aralığında geçerli bir tam sayı yaş alır."""
    while True:
        girdi = input("Hastanın Yaşı (0-130): ").strip()
        try:
            yas = int(girdi)
            if 0 <= yas <= 130:
                return yas
            print("  [UYARI] Yaş 0 ile 130 arasında olmalıdır (negatif veya aşırı büyük olamaz).")
        except ValueError:
            print("  [UYARI] Geçersiz yaş! Lütfen ondalıksız bir tam sayı giriniz (örn: 24).")


def kullanicidan_hasta_al() -> Hasta:
    """Kullanıcıdan ad, yaş ve şikâyet bilgilerini alarak Hasta nesnesi oluşturur."""
    print("\n--- Yeni Hasta Kaydı ---")
    ad = gecerli_metin_al("Hastanın Adı Soyadı: ", "Hasta adı")
    yas = gecerli_yas_al()
    sikayet = gecerli_metin_al("Hastanın Şikâyeti: ", "Şikâyet")
    return Hasta(ad, yas, sikayet)


def test_senaryolarini_calistir() -> None:
    """
    Ödev dokümanındaki 3 sınama senaryosunu + uç durum kontrollerini
    temiz (boş) listelerle otomatik olarak çalıştırır.
    """
    print("\n" + "#" * 60)
    print("OTOMATİK TEST SENARYOLARI BAŞLATILIYOR")
    print("#" * 60)

    # 1. SENARYO: Kendi kayıt senaryonuz
    print("\n>>> TEST 1: Kendi Kayıt Senaryonuz")
    print("(3 hasta ekle -> ilk hastayı çıkar -> 4. hastayı ekle -> listele)")
    sira1 = LinkedList()
    sira1.hasta_ekle(Hasta("Ahmet Yılmaz", 34, "Yüksek ateş ve öksürük"))
    sira1.hasta_ekle(Hasta("Zeynep Demir", 27, "Şiddetli baş ağrısı"))
    sira1.hasta_ekle(Hasta("Mehmet Kaya", 52, "Göğüs sıkışması"))
    print("-> 3 hasta sıraya eklendi: Ahmet Yılmaz, Zeynep Demir, Mehmet Kaya")
    sira1.siradaki_hastayi_cikar()
    z4 = sira1.hasta_ekle(Hasta("Elif Çelik", 19, "Bilek burkulması"))
    print(f"-> 4. hasta sıraya eklendi: Elif Çelik (Ziyaret edilen düğüm: {z4})")
    sira1.bekleyenleri_listele()

    # 2. SENARYO: Boş sıra
    print("\n>>> TEST 2: Boş Sıra Kontrolü")
    print("(Boş listede hasta çıkarma ve listeleme denemesi)")
    sira2 = LinkedList()
    sira2.siradaki_hastayi_cikar()
    sira2.bekleyenleri_listele()

    # 3. SENARYO: Tek hastalı sıra
    print("\n>>> TEST 3: Tek Hastalı Sıra Kontrolü")
    print("(1 hasta ekle -> çıkar -> boşaldığını kontrol et -> yeni hasta ekle -> listele)")
    sira3 = LinkedList()
    sira3.hasta_ekle(Hasta("Caner Aksoy", 41, "Mide bulantısı"))
    print("-> Tek hasta eklendi: Caner Aksoy")
    sira3.siradaki_hastayi_cikar()
    print(f"-> Liste boş mu? (head is None): {sira3.bos_mu()}")
    sira3.hasta_ekle(Hasta("Selin Arslan", 29, "Boğaz ağrısı"))
    print("-> Boşalan listeye yeni hasta eklendi: Selin Arslan")
    sira3.bekleyenleri_listele()

    # EKSTRA: Uç durum (stress) doğrulaması
    import contextlib
    import io

    print("\n>>> EKSTRA UÇ DURUM (STRESS) DOĞRULAMASI")
    # 1) 30 hastalı sırada sona ekleme maliyeti (O(n))
    sira_30 = LinkedList()
    for i in range(1, 31):
        sira_30.hasta_ekle(Hasta(f"Hasta {i}", 20 + (i % 50), "Kontrol"))
    z_31 = sira_30.hasta_ekle(Hasta("Hasta 31", 35, "Kontrol"))
    assert z_31 == 30, f"Beklenen 30, gelen {z_31}"
    print(f"[GEÇTİ] 30 hastalı sırada sona ekleme     -> {z_31} düğüm ziyaret edildi (O(n) doğrulandı)")

    # 2) Geçersiz (None) hasta ekleme koruması
    sira_gecersiz = LinkedList()
    with contextlib.redirect_stdout(io.StringIO()):
        sonuc_none = sira_gecersiz.hasta_ekle(None)
    assert sonuc_none == -1 and sira_gecersiz.bos_mu()
    print("[GEÇTİ] Geçersiz (None) hasta ekleme     -> Liste bozulmadan reddedildi")

    # 3) Boş listede art arda 5 çıkarma
    sira_bos = LinkedList()
    with contextlib.redirect_stdout(io.StringIO()):
        sonuclar = [sira_bos.siradaki_hastayi_cikar() for _ in range(5)]
    assert all(x is None for x in sonuclar)
    print("[GEÇTİ] Boş listede art arda 5 çıkarma   -> Çökme olmadan uyarı verdi")

    # 4) 500 hastalı uzun sıra ekle/çıkar (RecursionError kontrolü)
    sira_500 = LinkedList()
    for i in range(500):
        sira_500.hasta_ekle(Hasta(f"Test {i}", 30, "Muayene"))
    with contextlib.redirect_stdout(io.StringIO()):
        for _ in range(500):
            sira_500.siradaki_hastayi_cikar()
    assert sira_500.bos_mu()
    print("[GEÇTİ] 500 hastalı uzun sıra ekle/çıkar -> RecursionError olmadan tamamlandı")

    print("\n" + "#" * 60)
    print("TÜM TEST SENARYOLARI TAMAMLANDI")
    print("#" * 60)


def ana_menu() -> None:
    """Hastane Sıra Sistemi için hata korumalı interaktif konsol menüsü."""
    hastane_sirasi = LinkedList()

    while True:
        print("\n" + "-" * 44)
        print("   HASTANE SIRA SİSTEMİ (TEK YÖNLÜ LİSTE)")
        print("-" * 44)
        print("1. Yeni Hasta Ekle")
        print("2. Sıradaki Hastayı Muayene Et (Çıkar)")
        print("3. Bekleyen Hastaları Listele")
        print("4. Ödev Test Senaryolarını Çalıştır (1-2-3)")
        print("0. Çıkış")
        print("-" * 44)

        try:
            secim = input("Seçiminiz (0-4): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n[BİLGİ] Giriş sonlandırıldı. Sistemden güvenli şekilde çıkılıyor.")
            break

        if secim == "1":
            try:
                yeni_hasta = kullanicidan_hasta_al()
                ziyaret = hastane_sirasi.hasta_ekle(yeni_hasta)
                if ziyaret >= 0:
                    print(f"\n[BAŞARILI] {yeni_hasta.ad} sıranın sonuna eklendi. (Ziyaret edilen düğüm: {ziyaret})")
            except (EOFError, KeyboardInterrupt):
                print("\n\n[BİLGİ] Kayıt işlemi iptal edildi. Ana menüye dönülüyor.")
        elif secim == "2":
            hastane_sirasi.siradaki_hastayi_cikar()
        elif secim == "3":
            hastane_sirasi.bekleyenleri_listele()
        elif secim == "4":
            test_senaryolarini_calistir()
        elif secim == "0":
            print("\nSistemden çıkılıyor. Sağlıklı günler dileriz.")
            break
        else:
            print("\n[UYARI] Geçersiz seçim! Lütfen 0 ile 4 arasında bir değer girin.")


if __name__ == "__main__":
    ana_menu()
