from time import sleep as sl

def dialog(yazi:str, sure=0.03):
    """
    Metni daktilo efektiyle yazdırır.

    Args:
        yazi: Yazdırılacak metin.
        sure: Her karakter arasındaki saniye cinsinden gecikme.
    """
    if type(yazi) != str: #yazi degiskeni string veri tipinde degilse
        return "Hatali veri tipi."

    else:
        for i in yazi:
            if i == " ":
                print(i, end = "", flush = True)
            else:
                print(i, end = "", flush = True)
                sl(sure)
        print("\n")
        pass
    pass


class islem():
    """
    Çeşitli hacim hesaplamaları yapmak için bir sınıf.
    """
    import HazirMetinler #Metinleri sakladigim yeri aldim
    import math #pi sayisi icin lazim olacak
    hata = "HATALI VERI TIPI ALGILANDI" #Surekli yazmamak icin degiskene atadim
    
    
    def KupHacmi(self, a):
        """
        Bir küpün hacmini hesaplar.

        Args:
            a: Küpün bir kenarının uzunluğu.

        Returns:
            Sonucu içeren biçimlendirilmiş bir dize veya bir hata mesajı.
        """
        try:
            a = float(a) #a = Kenar
        except (TypeError, ValueError):
            return self.hata
        else:
            return str(self.HazirMetinler.KupHacmi.format(kenar = a,
                                                          cevap = a**3))
     
        
    def KarePrizmaHacmi(self, a, h):
        """
        Bir kare prizmanın hacmini hesaplar.

        Args:
            a: Kare tabanın bir kenarının uzunluğu.
            h: Prizmanın yüksekliği.

        Returns:
            Sonucu içeren biçimlendirilmiş bir dize veya bir hata mesajı.
        """
        try:
            a, h = float(a), float(h) #a = Kenar|h = Yukseklik
        except (TypeError, ValueError):
            return self.hata
        else:
            return str(self.HazirMetinler.KarePrizmaHacmi.format(kenar = a,
                                                                 yukseklik = h,
                                                                 cevap = (a**2)*h))
            
    
    
    def DikdotrgenPrizmaHacmi(self, a1, a2, a3):
        """
        Bir dikdörtgen prizmanın hacmini hesaplar.

        Args:
            a1: Birinci kenarın uzunluğu.
            a2: İkinci kenarın uzunluğu.
            a3: Üçüncü kenarın uzunluğu.

        Returns:
            Sonucu içeren biçimlendirilmiş bir dize veya bir hata mesajı.
        """
        try:
            a1, a2, a3 = float(a1), float(a2), float(a3) #a[sayi] = Kenar[sayi]
        except (TypeError, ValueError):
            return self.hata
        else:
            return str(self.HazirMetinler.DikdotrgenPrizmaHacmi.format(kenar1 = a1,
                                                                       kenar2 = a2,
                                                                       kenar3 = a3,
                                                                       cevap = a1*a2*a3))


    def KureHacmi(self, r, pi = math.pi):
        """
        Bir kürenin hacmini hesaplar.

        Args:
            r: Kürenin yarıçapı.
            pi: Hesaplamada kullanılacak pi değeri.

        Returns:
            Sonucu içeren biçimlendirilmiş bir dize veya bir hata mesajı.
        """
        try:
            r, pi = float(r), float(pi) #r = Yaricap
        except (TypeError, ValueError):
            return self.hata
        else:
            return str(self.HazirMetinler.KureHacmi.format(r = r,
                                                           pi = pi,
                                                           cevap = (4/3*pi*(r**3))))


    def SilindirHacmi(self, r, h, pi = math.pi):
        """
        Bir silindirin hacmini hesaplar.

        Args:
            r: Silindirin tabanının yarıçapı.
            h: Silindirin yüksekliği.
            pi: Hesaplamada kullanılacak pi değeri.

        Returns:
            Sonucu içeren biçimlendirilmiş bir dize veya bir hata mesajı.
        """
        try:
            r, h, pi = float(r), float(h), float(pi) #r = Yaricap|h = Yukseklik
        except (TypeError, ValueError):
            return self.hata
        else:
            return str(self.HazirMetinler.SilindirHacmi.format(r = r, yukseklik=h,
                                                               pi = pi,
                                                               cevap = pi*r**2*h))
            
            
    def KarePiramitHacmi(self, a, h):
        """
        Bir kare piramidin hacmini hesaplar.

        Args:
            a: Piramidin tabanının alanı.
            h: Piramidin yüksekliği.

        Returns:
            Sonucu içeren biçimlendirilmiş bir dize veya bir hata mesajı.
        """
        try:
            a, h = float(a), float(h) #a = Taban Alani|h = Yukseklik
        except (TypeError, ValueError):
            return self.hata
        else:
            return str(self.HazirMetinler.KarePiramitHacmi.format(tabanalani = a,
                                                              yukseklik = h,
                                                              cevap = 1/3*a*h))
            
            
    def KoniHacmi(self, r, h, pi = math.pi):
        """
        Bir koninin hacmini hesaplar.

        Args:
            r: Koninin tabanının yarıçapı.
            h: Koninin yüksekliği.
            pi: Hesaplamada kullanılacak pi değeri.

        Returns:
            Sonucu içeren biçimlendirilmiş bir dize veya bir hata mesajı.
        """
        try:
            r, h, pi = float(r), float(h), float(pi) #r = Yaricap|h = Yukseklik
        except (TypeError, ValueError):
            return self.hata
        else:
            return str(self.HazirMetinler.KoniHacmi.format(r = r,
                                                           yukseklik = h,
                                                           pi = pi,
                                                           cevap = 1/3*pi*r**2*h))
            
            

def debug():
    """
    Hesaplama fonksiyonlarını rastgele değerlerle test eder.

    Returns:
        Tüm testlerin sonuçlarını içeren bir dize.
    """
    from random import randint #rastgele sayi uretmek icin
    x, y = 1, 8 #deger araligi

    i1 = islem().KupHacmi(randint(x, y))
    i2 = islem().KarePrizmaHacmi(randint(x, y), randint(x, y))
    i3 = islem().DikdotrgenPrizmaHacmi(randint(x, y), randint(x, y), randint(x, y))
    i4 = islem().KureHacmi(randint(x, y))
    i5 = islem().SilindirHacmi(randint(x, y), randint(x, y))
    i6 = islem().KarePiramitHacmi(randint(x, y), randint(x, y))
    i7 = islem().KoniHacmi(randint(x, y), randint(x, y))

    li = [i1, i2, i3, i4, i5, i6, i7]

    return "\n".join(li)