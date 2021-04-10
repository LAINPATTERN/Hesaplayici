from time import sleep as sl

def dialog(yazi:str, sure=0.03):
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


class islem(): #Düzenli dursun diye islemlerin saklanacagi yer.
    import HazirMetinler #Metinleri sakladigim yeri aldim
    import math #pi sayisi icin lazim olacak
    hata = "HATALI VERI TIPI ALGILANDI" #Surekli yazmamak icin degiskene atadim
    
    
    def KupHacmi(self, a):
        try:
            a = float(a) #a = Kenar
        except (TypeError, ValueError):
            return self.hata
        else:
            return str(self.HazirMetinler.KupHacmi.format(kenar = a,
                                                          cevap = a**3))
     
        
    def KarePrizmaHacmi(self, a, h):
        try:
            a, h = float(a), float(h) #a = Kenar|h = Yukseklik
        except (TypeError, ValueError):
            return self.hata
        else:
            return str(self.HazirMetinler.KarePrizmaHacmi.format(kenar = a,
                                                                 yukseklik = h,
                                                                 cevap = (a**2)*h))
            
    
    
    def DikdotrgenPrizmaHacmi(self, a1, a2, a3):
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
        try:
            r, pi = float(r), float(pi) #r = Yaricap
        except (TypeError, ValueError):
            return self.hata
        else:
            return str(self.HazirMetinler.KureHacmi.format(r = r,
                                                           pi = pi,
                                                           cevap = (4/3*pi*(r**3))))


    def SilindirHacmi(self, r, h, pi = math.pi):
        try:
            r, h, pi = float(r), float(h), float(pi) #r = Yaricap|h = Yukseklik
        except (TypeError, ValueError):
            return self.hata
        else:
            return str(self.HazirMetinler.SilindirHacmi.format(r = r, yukseklik=h,
                                                               pi = pi,
                                                               cevap = pi*r**2*h))
            
            
    def KarePiramitHacmi(self, a, h):
        try:
            a, h = float(a), float(h) #a = Taban Alani|h = Yukseklik
        except (TypeError, ValueError):
            return self.hata
        else:
            return str(self.HazirMetinler.KarePiramitHacmi.format(tabanalani = a,
                                                              yukseklik = h,
                                                              cevap = 1/3*a*h))
            
            
    def KoniHacmi(self, r, h, pi = math.pi):
        try:
            r, h, pi = float(r), float(h), float(pi) #r = Yaricap|h = Yukseklik
        except (TypeError, ValueError):
            return self.hata
        else:
            return str(self.HazirMetinler.KoniHacmi.format(r = r,
                                                           yukseklik = h,
                                                           pi = pi,
                                                           cevap = 1/3*r**2*h))
            
            

def debug(): #Hatalari test etmek icin fonksiyon
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
    
    for test in li:
        return str(test)