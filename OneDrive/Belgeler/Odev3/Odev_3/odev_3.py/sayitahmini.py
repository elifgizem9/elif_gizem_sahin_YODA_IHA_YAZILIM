# Sayı Tahmin Oyunu Programı

import random # Rastgele sayı üretmek için random içe aktarıyoruz

def sayi_tahmin_oyunu():
    """
    Ana oyun fonksiyonu
    Kullanıcıya 10 tahmin hakkı verir
    """
    
    # Oyun başlığını ekrana yazdır
    
    print("1 ile 100 arasında bir sayı tuttum.")
    print("10 tahmin hakkınız var.\n")
    
    # 1 ile 100 arasında rastgele bir sayı seç
    gizlisayi = random.randint(1, 100)
    
    # Tahmin hakkı sayacını başlat
    tahminhakki = 10
    
    # Kullanıcının doğru tahmin edip etmediğini kontrol etmek için değişken
    kazandi = False
    
    # Oyun döngüsü 10 tahmin hakkı boyunca devam eder
    while tahminhakki > 0:
        
        # Kalan tahmin hakkını göster
        print(f"Kalan tahmin hakkınız: {tahminhakki}")
        
        try:
            # Kullanıcıdan tahmin al
            tahmin = int(input("Tahmininiz: "))
            
            # Tahminin geçerli aralıkta olup olmadığını kontrol et
            if tahmin < 1 or tahmin > 100:
                print("Lütfen 1 ile 100 arasında bir sayı girin.\n")
                continue # Geçersiz girişte tahmin hakkı azalmaz, döngü başa döner
            
            # Tahmin hakkını bir azalt
            tahminhakki -= 1
            
            # Tahmini gizli sayı ile karşılaştır
            if tahmin < gizlisayi:
                # Tahmin küçükse kullanıcıyı bilgilendir
                print("Daha büyük bir sayı söyleyin!\n")
                
            elif tahmin > gizlisayi:
                # Tahmin büyükse kullanıcıyı bilgilendir
                print("Daha küçük bir sayı söyleyin!\n")
                
            else:
                # Tahmin doğruysa oyunu kazan
                kazandi = True
                break # Döngüden çık
        
        except ValueError:
            # Geçersiz giriş durumunda
            print("Geçersiz giriş. Lütfen bir sayı girin.\n")
            continue # Tahmin hakkı azalmaz
    
    # Oyun sonucu değerlendirmesi
    
    if kazandi:
        # Kullanıcı kazandıysa
        kullanilantahmin = 10 - tahminhakki
        print("Doğru tahmin")
        print(f"Doğru sayı: {gizlisayi}")
        print(f"{kullanilantahmin} denemede buldunuz")
        
    else:
        # Tahmin hakkı bittiyse
        print("Maalesef tahmin hakkınız bitti")
        print(f"Doğru sayı: {gizli_sayi} idi")
        print("Bir daha deneyin")


# Programı çalıştır
if __name__ == "__main__":
    sayi_tahmin_oyunu()