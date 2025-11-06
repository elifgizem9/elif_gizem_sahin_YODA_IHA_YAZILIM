# Basit Hesap Makinesi Programı
# Bu program kullanıcıdan iki sayı ve işlem alarak matematiksel hesaplama yapar

def hesapmakinesi():
    
    print("Toplama (+), Çıkarma (-), Çarpma (*), Bölme (/) işlemleri")
    
    # Sonsuz döngü kullanıcı 'h' yanıtı verene kadar devam eder
    while True:
        
        try:
            # Kullanıcıdan birinci sayıyı al
            # float() fonksiyonu ile ondalıklı sayı desteği sağlıyoruz
            sayi1 = float(input("Birinci sayıyı girin: "))
            
            # Kullanıcıdan ikinci sayıyı al
            sayi2 = float(input("İkinci sayıyı girin: "))
            
        except ValueError:
            # Sayı yerine harf veya geçersiz karakter girilirse hata yakala
            print("\n hata: Geçerli bir sayı girmelisiniz")
            print("Lütfen tekrar deneyin.\n")
            continue # Döngünün başına dön
        
        # İşlem seçimini al
        print("\n İşlem Seçin:")
        print(" [+] Toplama")
        print(" [-] Çıkarma")
        print(" [*] Çarpma")
        print(" [/] Bölme")
        
        # Kullanıcıdan işlem seçimini al
        islem = input("\n İşleminiz (+, -, *, /): ").strip()
        
        sonuc = None
        
        # İşlem türüne göre hesaplama yap
        if islem == '+':
            # Toplama işlemi
            sonuc = sayi1 + sayi2
            islemadi = "Toplama"
            
        elif islem == '-':
            # Çıkarma işlemi
            sonuc = sayi1 - sayi2
            islemadi = "Çıkarma"
            
        elif islem == '*':
            # Çarpma işlemi
            sonuc = sayi1 * sayi2
            islemadi = "Çarpma"
            
        elif islem == '/':
            # Bölme işlemi
            # Sıfıra bölme kontrolü
            if sayi2 == 0:
                # Sıfıra bölme hatası
                print("hata: Bir sayı sıfıra bölünemez")
                islemadi = "Bölme (Hata)"
                sonuc = None
            else:
                # Normal bölme işlemi
                sonuc = sayi1 / sayi2
                islemadi = "Bölme"
        
        else:
            # Geçersiz işlem seçimi
            print("hata: Geçersiz işlem")
            print("Lütfen +, -, * veya / karakterlerinden birini kullanın.")
            continue # Döngünün başına dön
        
        # Sonucu ekrana yazdır
        if sonuc is not None:
            print(f"{islemadi} İşlemi Sonucu:")
            print(f" {sayi1} {islem} {sayi2} = {sonuc}")
        
        # Kullanıcıya devam etmek isteyip istemediğini sor
        devam = input("Başka bir işlem yapmak ister misiniz evet için E veya EVET hayır için H veya HAYIR girin: ").strip().upper()
        
        # Kullanıcının yanıtını kontrol et
        if devam == 'H' or devam == 'HAYIR':
            # Kullanıcı çıkmak istiyorsa
            print("Hesap makinesinden çıkılıyor")
    
            break # Döngüden çık, program sona ersin
        elif devam == 'E' or devam == 'EVET':
            # Kullanıcı devam etmek istiyorsa
            print("Yeni işlem başlatılıyor")
            continue # Döngü devam etsin
        else:
            # Geçersiz yanıt 
            print("\nGeçersiz yanıt. Yeni işleme devam ediliyor\n")
            continue

# Programı çalıştır
if __name__ == "__main__":
    hesapmakinesi()