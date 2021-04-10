import YardimciAraclar

yardimMetni = """
HESAPLAYICIYA HOS GELDİNİZ!
\n\tYapabilecekleriniz:
\t\t1 >>> Kupun Hacmi
\t\t2 >>> Kare Prizmanin Hacmi
\t\t3 >>> Dikdortgen Prizmanin Hacmi
\t\t4 >>> Kurenin Hacmi
\t\t5 >>> Silindirin Hacmi
\t\t6 >>> Kare Piramitin Hacmi
\t\t7 >>> Koninin Hacmi
\t\tc >>> Cikis
\t\td >>> Debug
"""

YardimciAraclar.dialog(yardimMetni, 0.01)

#----------0----1----2----3----4----5----6----7----8-#
secenek = ["1", "2", "3", "4", "5", "6", "7", "c", "d"]

def kapat(): exit("\nKullanici Tarafindan Kapatildi\n")

def secim(secilen:str): #Biraz daha duzenli gozuksun diye uygun ciktiyi ureten fonksiyon
    x = secilen.lower()
    if x not in secenek: #x secenek listesinde yoksa
        return "\nHatali komut!\n\tBu ({}) bir komut degil.".format(x)
    
    elif x not in secenek[0:7]: #x secenek listesinin 0 ve 7 arasindaki (Matematiksel ifadesi>>>"[0,7)") bolgede yoksa
        if x == "c": kapat() #x, c ise konsolu kapat.
        elif x == "d": return YardimciAraclar.debug()
        else: #degilse,
            return "imkansiz secenek" #her ihtimale karsi hata metni
        pass
    
    elif x in secenek[0:7]: return x
    else: return "Bilinmeyen hata"



def islemler(komut:str):
    gecersiz = "\nGECERSIZ VERI\n" #Surekli yazmamak icin degisken
    hesap = YardimciAraclar.islem() #YardimciAraclar.islem() i ornekledim
    
    if komut not in secenek: return komut
    
    elif komut == "1": #---1---#
        while True:
            k = input("\nKupun bir kenarinin kac birim?\n\t>>> ")
            if k == "c": kapat()
            elif k: break
            else: print(gecersiz)
            pass
        return hesap.KupHacmi(k)
    
    elif komut == "2": #---2---#
        while True:
            k = input("\nKare prizmanin kare yuzeylerinden birinin kenari kac birim?\n\t>>> ")
            if k == "c": kapat()
            elif k: break
            else: print(gecersiz)
            pass
        while True:
            h = input("\nKare yuzeylerin birbirine olan uzakligi kac birim?\n\t>>> ")
            if h == "c": kapat()
            elif h: break
            else: print(gecersiz)
            pass
        return hesap.KarePrizmaHacmi(k, h)
    
    elif komut == "3": #---3---#
        while True:
            a1 = input("\nDikdortgen prizmanin ilk kenari kac birim?\n\t>>> ")
            if a1 == "c": kapat()
            elif a1: break
            else: print(gecersiz)
            pass
        while True:
            a2 = input("\nDikdortgen prizmanin diger kenari kac birim?\n\t>>> ")
            if a2 == "c": kapat()
            elif a2: break
            else: print(gecersiz)
            pass
        while True:
            a3 = input("\nDikdortgen prizmanin son kenari kac birim?\n\t>>> ")
            if a3 == "c": kapat()
            elif a3: break
            else: print(gecersiz)
            pass
        return hesap.DikdotrgenPrizmaHacmi(a1, a2, a3)
    
    elif komut == "4": #---4---#
        while True:
            r = input("Kurenin yaricapi kac birim?\n\t>>> ")
            if r == "c": kapat()
            elif r: break
            else: print(gecersiz)
            pass
        while True:
            pi = input("Hacmi hesaplamak icin pi kac alinsin? Bos birakirsaniz pi {} alinacak.\n\t>>> "
                       .format(YardimciAraclar.islem().math.pi))
            if pi == "c": kapat()
            elif not pi:
                return hesap.KureHacmi(r)
            else:
                return hesap.KureHacmi(r,pi)
            break
        pass
    
    elif komut == "5": #---5---#
        while True:
            r = input("Silindirin taban yaricapi kac birim?\n\t>>> ")
            if r == "c": kapat()
            elif r: break
            else: print(gecersiz)
            pass
        while True:
            h = input("Silindirin yuksekligi kac birim?\n\t>>> ")
            if h == "c": kapat()
            elif h: break
            else: print(gecersiz)
            pass
        while True:
            pi = input("Hacmi hesaplamak icin pi kac alinsin? Bos birakirsaniz pi {} alinacak.\n\t>>> "
                       .format(YardimciAraclar.islem().math.pi))
            if pi == "c": kapat()
            elif not pi:
                return hesap.SilindirHacmi(r, h)
            else:
                return hesap.SilindirHacmi(r, h, pi)
            break
        pass
    
    elif komut == "6": #---6---#
        while True:
            a = input("Kare piramitin taban alani kac birim kare?\n\t>>> ")
            if a == "c": kapat()
            elif a: break
            else: print(gecersiz)
            pass
        while True:
            h = input("Kare piramitin yuksekligi kac birim?\n\t>>> ")
            if h == "c": kapat()
            elif h: break
            else: print(gecersiz)
            pass
        return hesap.KarePiramitHacmi(a, h)
    
    elif komut == "7": #---7---#
        while True:
            r = input("Koninin taban yaricapi kac birim?\n\t>>> ")
            if r == "c": kapat()
            elif r: break
            else: print(gecersiz)
            pass
        while True:
            h = input("Koninin yuksekligi kac birim?\n\t>>> ")
            if h == "c": kapat()
            elif h: break
            else: print(gecersiz)
            pass
        while True:
            pi = input("Hacmi hesaplamak icin pi kac alinsin? Bos birakirsaniz pi {} alinacak.\n\t>>> "
                       .format(YardimciAraclar.islem().math.pi))
            if pi == "c": kapat()
            elif not pi:
                return hesap.KoniHacmi(r, h)
            else:
                return hesap.KoniHacmi(r, h, pi)
            break
        pass
    else:
        return "Bilinmeyen hata"
#%% Main
while True:
    try: s = islemler(secim(input(">>> ")))
    except KeyboardInterrupt: exit("\nKullanici tarafindan zorla kapatildi\n")
    print(s)