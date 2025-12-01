# Kelime Sayacı Programı
# Bu program kullanıcıdan metin alır ve çeşitli istatistikler hesaplar

def kelimesayaci():
   
    # Metin analiz fonksiyonu
    # Program başlayınca ilk aşağıdakiler yazar
    print("Lütfen analiz etmek istediğiniz metni girin:")
    print("Birden fazla satır girebilirsiniz. Bitirmek için boş satırda ENTER'a basın\n")
    
    # Kullanıcıdan metin alınır çok satırlı giriş
    satirlar = [] # Satırları saklamak için boş liste oluştur
    
    while True:
        satir = input() # Her satırı al
        
        if satir == "": # Boş satır girilirse döngüyü kır
            break
        
        satirlar.append(satir) # Satırı listeye ekle
    
    # Tüm satırları tek bir metne birleştir
    metin = " ".join(satirlar)
    
    # Metin boşsa uyarı ver ve çık
    if not metin.strip():
        print("\n Hiç metin girilmedi.")
        return
    
   
    # İSTATİSTİK HESAPLAMALARI
    
    # 1. Toplam karakter sayısı 
    toplamkarakter = len(metin)
    
    # 3. Metni kelimelere ayır
    # split() metodu metni boşluklardan böler ve kelime listesi oluşturur
    kelimeler = metin.split()
    
    # 4. Toplam kelime sayısı
    kelimesayisi = len(kelimeler)
    
    # 5. En uzun kelimenin uzunluğunu bul
    # Eğer kelime varsa, max() fonksiyonu ile en uzun kelimenin uzunluğunu al
    if kelimeler:
        enuzunkelimeuzunlugu = len(max(kelimeler, key=len))
        enuzunkelime = max(kelimeler, key=len)
    else:
        enuzunkelimeuzunlugu = 0
        enuzunkelime = ""
    
    # 6. Kelime tekrarını hesapla
    # Dictionary kullanarak her kelimenin kaç kez geçtiğini say
   
    # Programımız büyük/küçük harf duyarlı değil
    # Yani Python, python ve PYTHON aynı kelime olarak sayılacak
    # Bu nedenle tüm kelimeleri küçük harfe çevireceğiz
    
    kelimefrekansi = {} # Boş sözlük oluştur
    
    for kelime in kelimeler:
        # Her kelimeyi küçük harfe çevir ve noktalama işaretlerini temizle
        kelimetemiz = kelime.lower().strip('.,!?;:"')
        
        # Sözlükte bu kelime varsa sayacı 1 artır, yoksa 1 yap
        if kelimetemiz in kelimefrekansi:
            kelimefrekansi[kelimetemiz] += 1
        else:
            kelimefrekansi[kelimetemiz] = 1
  
    # SONUÇLARI EKRANA YAZDIRMA
    
   
    print("Metin analiz sonuçları")
    
    # Temel istatistikler
    print(f"\n Girilen Metin:")
    print(f"{metin}")
    print(f" • Toplam Karakter Sayısı: {toplamkarakter}")
    print(f" • Toplam Kelime Sayısı : {kelimesayisi}")
    print(f" • En Uzun Kelimenin Uzunluğu : {enuzunkelimeuzunlugu} karakter")
    print(f" • En Uzun Kelime : '{enuzunkelime}'")
    
    # Kelime tekrarını göster
    # < ve > hizzalama işareti > metni sağa yaslar, < metni sola yaslar. Sayılar metin için konsolda kaç karakterlik alan ayrılacağını verir 
    print(f"\n Kelime tekrar tablosu:")
    print(f"{'Kelime':<20} {'Tekrar Sayısı':>15} {'Grafik':<30}") 

    
    # Kelimeleri tekrara göre büyükten küçüğe sırala
    # sorted() fonksiyonu ile sözlüğü sırala
    # key=lambda x: x[1]  değere göre sırala
    # reverse=True büyükten küçüğe
    siralikelimeler = sorted(kelimefrekansi.items(), key=lambda x: x[1], reverse=True)
    
    # Her kelime için frekans bilgisini yazdır
    for kelime, frekans in siralikelimeler:
        # Görsel grafik oluştur
        grafik = " " * frekans
        print(f"{kelime:<20} {frekans:>15} {grafik}")
    
    # En çok tekrar eden kelimeyi bul
    encoktekrareden = max(kelimefrekansi.items(), key=lambda x: x[1])
    print(f"\n En Çok Tekrar Eden Kelime: '{encoktekrareden[0]}' ({encoktekrareden[1]} kez)")

# Programı çalıştır
if __name__ == "__main__":
    kelimesayaci()