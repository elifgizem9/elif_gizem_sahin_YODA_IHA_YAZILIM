
class BankaHesabi:
# Banka hesabı sınıfı
# Her hesap için ad, soyad, hesap numarası ve bakiye bilgilerini tutar
# Sınıf değişkeni tüm hesaplar için ortak
# Her yeni hesap için otomatik artan hesap numarası
    sonrakihesapno = 1
    
    def __init__(self, ad , soyad, baslangicbakiye =0):
   
            # Constructor metod yeni bir hesap oluşturulduğunda otomatik çalışır
        
            """Parametreler:
            - ad: Hesap sahibinin adı
            - soyad: Hesap sahibinin soyadı
            - baslangicbakiye: İlk bakiye varsayılan 0
            """
        
            # Hesap sahibi bilgileri
            self.ad = ad
            self.soyad = soyad
        
            # Otomatik hesap numarası ata
            self.hesapnumarasi = BankaHesabi.sonrakihesapno
            BankaHesabi.sonrakihesapno += 1 # Bir sonraki hesap için artır
        
            # Başlangıç bakiyesi
            self.bakiye = baslangicbakiye
        
            # Hesap durumu (aktif/pasif)
            self.aktif = True
        
            # İşlem geçmişini saklamak için liste
            self.islemgecmisi = []
        
            # İlk işlemi kaydet
            if baslangicbakiye > 0:
                self.islemgecmisi.append(f"Hesap açılışı: +{baslangicbakiye:.2f} TL")
    
    def parayatir(self, miktar):
        """
        Hesaba para yatırma metodu
        
        Parametre:
        - miktar: Yatırılacak para miktarı
        """
        
        # Hesap aktif mi kontrol et
        if not self.aktif:
            print("\n hata: Bu hesap kapatılmış")
            return False
        
        # Miktar kontrolü negatif veya sıfır olursa
        if miktar <= 0:
            print("\n hata: Geçersiz miktar!")
            print("Para yatırma işlemi için pozitif bir değer girmelisiniz.")
            return False
        
        # Bakiyeyi artır
        self.bakiye += miktar
        
        # İşlemi kaydet
        self.islemgecmisi.append(f"Para yatırma: +{miktar:.2f} TL")
        
        # Başarı mesajı
       
        print("Para yatırma başarılı")
        print(f"Yatırılan Tutar : {miktar:.2f} TL")
        print(f"Güncel Bakiye : {self.bakiye:.2f} TL")
        
        return True
    
    def para_cek(self, miktar):
        """
        Hesaptan para çekme metodu
        
        Parametre:
        - miktar: Çekilecek para miktarı
        """
        
        # Hesap aktif mi kontrol et
        if not self.aktif:
            print("\n Hata: Bu hesap kapatılmış")
            return False
        
        # Miktar kontrolü negatif veya sıfır olursa
        if miktar <= 0:
            print("\n HATA: Geçersiz miktar")
            print("Para çekme işlemi için pozitif bir değer girmelisiniz.")
            return False
        
        # Yetersiz bakiye kontrolü
        if miktar > self.bakiye:
            print("Yetersiz bakiye")
            print(f"Çekmek istediğiniz tutar: {miktar:.2f} TL")
            print(f"Mevcut bakiyeniz : {self.bakiye:.2f} TL")
            print(f"Eksik tutar : {miktar - self.bakiye:.2f} TL")
            return False
        
        # Bakiyeden düş
        self.bakiye -= miktar
        
        # İşlemi kaydet
        self.islemgecmisi.append(f"Para çekme: -{miktar:.2f} TL")
        
        # Başarı mesajı
        print("Para çekme işlemi başarılı")
        print(f"Çekilen Tutar : {miktar:.2f} TL")
        print(f"Kalan Bakiye : {self.bakiye:.2f} TL")
        
        return True
    
    def bakiye_goruntule(self):
        """
        Hesap bakiyesini ve detaylarını gösterme metodu
        """
        
        # Hesap durumu
        durum = "Aktif" if self.aktif else "Kapalı"
        
        # Detaylı bilgiler
        print("Hesap Bilgileri")
        print(f"Hesap Numarası : {self.hesap_numarasi}")
        print(f"Hesap Sahibi : {self.ad} {self.soyad}")
        print(f"Hesap Durumu : {durum}")
        print(f"Güncel Bakiye : {self.bakiye:.2f} TL")
    
    def islemgecmisinigoster(self):
        """
        Hesap işlem geçmişini gösterme metodu
        """
        print("İşlem Geçmişi")
        
        # İşlem geçmişi varsa göster
        if self.islemgecmisi:
            for i, islem in enumerate(self.islemgecmisi, 1):
                print(f"{i}. {islem}")
        else:
            print("Henüz işlem yapılmamış.")
    
    def hesapkapat(self):
        """
        Hesabı kapatma metodu
        """
        
        # Hesap zaten kapalıysa
        if not self.aktif:
            print("\n Bu hesap zaten kapalı")
            return False
        
        # Bakiye varsa hesap kapatılamaz
        if self.bakiye > 0:
            print("Hesap kapatılmadı")
            print(f"Hesabınızda {self.bakiye:.2f} TL bakiye bulunmaktadır.")
            print("Hesabı kapatmak için önce tüm parayı çekmelisiniz.")
            return False
        
        # Hesabı kapat
        self.aktif = False
        self.islemgecmisi.append("Hesap kapatıldı")
        
        print("\n" + "=" * 60)
        print("Hesap başarıyla kapatıldı")
        
        return True


def bankasistemi():
    """
    Ana banka yönetim sistemi
    Kullanıcı arayüzü ve menü işlemleri
    """
    
    # Program başlığı
    print("Banka Hesap Yönetim Sistemi")
    
    # Hesap nesnesi başlangıçta None
    hesap = None
    
    # Ana menü döngüsü
    while True:
    
        print("Ana menü:")
        
        # Menü seçenekleri
        if hesap is None:
            # Hesap yoksa sadece hesap açma seçeneği
            print("1. Yeni Hesap Aç")
            print("0. Çıkış")
        else:
            # Hesap varsa tüm işlemler
            print("1. Para Yatır")
            print("2. Para Çek")
            print("3. Bakiye Görüntüle")
            print("4. İşlem Geçmişi")
            print("5. Hesabı Kapat")
            print("0. Çıkış")
        
        # Kullanıcıdan seçim al
        secim = input("Seçiminiz: ").strip()
        
        # Hesap yoksa ve seçim 1 ise yeni hesap aç
        if hesap is None and secim == '1':
            
            print("Yeni hesap açılış")

            # Hesap sahibi bilgilerini al
            ad = input("Adınız: ").strip()
            soyad = input("Soyadınız: ").strip()
            
            # Ad ve soyad boş olamaz
            if not ad or not soyad:
                print("\n Ad ve soyad boş bırakılamaz")
                continue
            
            # Başlangıç bakiyesi
            try:
                baslangicstr = input("Başlangıç bakiyesi (Enter=0): ").strip()
                baslangicbakiye = float(baslangicstr) if baslangicstr else 0
                
                # Negatif bakiye kontrolü
                if baslangicbakiye < 0:
                    print("\nBaşlangıç bakiyesi negatif olamaz")
                    continue
                
            except ValueError:
                print("\n Geçersiz bakiye değeri")
                continue
            
            # Yeni hesap oluştur
            hesap = BankaHesabi(ad, soyad, baslangicbakiye)
            
            # Başarı mesajı
            print("Hesap başarıyla oluşturuldu")
            print(f"Hesap Numaranız: {hesap.hesapnumarasi}")
            print(f"Hesap Sahibi : {hesap.ad} {hesap.soyad}")
            print(f"Başlangıç Bakiyesi: {hesap.bakiye:.2f} TL")
        
        # Hesap varsa işlem menüsü
        elif hesap is not None:
            
            if secim == '1':
                # Para yatırma
                try:
                    miktar = float(input("\nYatırılacak tutarı girin: "))
                    hesap.parayatir(miktar)
                except ValueError:
                    print("\n Geçersiz tutar")
            
            elif secim == '2':
                # Para çekme
                try:
                    miktar = float(input("\nÇekilecek tutarı girin: "))
                    hesap.paracek(miktar)
                except ValueError:
                    print("\nGeçersiz tutar")
            
            elif secim == '3':
                # Bakiye görüntüleme
                hesap.bakiyegoruntule()
            
            elif secim == '4':
                # İşlem geçmişi
                hesap.islemgecmisinigoster()
            
            elif secim == '5':
                # Hesabı kapatma
                print("\n Dikkat: Bu işlem geri alınamaz!")
                onay = input("Hesabınızı kapatmak istediğinizden emin misiniz? (E/H): ").strip().upper()
                
                if onay == 'E':
                    # Hesabı kapatmayı dene
                    if hesap.hesapkapat():
                        # Hesap başarıyla kapatıldıysa, hesap nesnesini sıfırla
                        hesap = None
            
            elif secim == '0':
                # Çıkış
                print("Sistemden çıkılıyor")
                break
            
            else:
                # Geçersiz seçim
                print("\nGeçersiz seçim. Lütfen menüden bir seçenek seçin.")
        
        # Hesap yoksa ve seçim 0 ise çıkış
        elif hesap is None and secim == '0':
            print("Sistemden çıkılıyor")
            break
        
        else:
            # Geçersiz seçim
            print("\nGeçersiz seçim. Lütfen menüden bir seçenek seçin.")


# Programı çalıştır
if __name__ == "__main__":
    bankasistemi()
    