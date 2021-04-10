ayrac1= "\n─────────────────────────────────────────────────────────────────"
ayrac2 = "─────────────────────────────────────────────────────────────────\n"



#1
KupHacmi = ayrac1 + """
Kupun bir kenari {kenar} birim ise
hacmi {kenar} * {kenar} * {kenar} = {cevap}

Yani cevap: {cevap} birim kup
""" + ayrac1


#2
KarePrizmaHacmi = ayrac1 + """
Kare prizmanin kare yuzlerinden birinin kenari {kenar} birim,
kare yuzlerin birbirine olan uzakligi {yukseklik} birim ise 
kare prizmanin hacmi ({kenar} * {kenar}) * {yukseklik} = {cevap}

Yani cevap: {cevap} birim kup
""" + ayrac2


#3
DikdotrgenPrizmaHacmi = ayrac1 + """
Dikdortgen prizmanin kenarlari {kenar1}, {kenar2} ve {kenar3} birim ise
dikdörtgen prizmanin hacmi {kenar1} * {kenar2} * {kenar3} = {cevap}

Yani cevap: {cevap} birim kup
""" + ayrac2


#4
KureHacmi = ayrac1 + """
Kurenin yaricapi {r} birim ve pi {pi} ise
kurenin hacmi 4/3 * {pi} * {r} * {r} * {r} = {cevap}

Yani cevap: {cevap} birim kup
""" + ayrac2


#5
SilindirHacmi = ayrac1 + """
Silindirin taban yaricapi {r} birim, 
yuksekligi {yukseklik} birim ve pi {pi} ise
silindirin hacmi {pi} * {r} * {r} * {yukseklik} = {cevap}

Yani cevap: {cevap} birim kup
""" + ayrac2


#6
KarePiramitHacmi = ayrac1 + """
Kare piramitin taban alani {tabanalani} ve yuksekligi {yukseklik} ise
kare piramitin hacmi 1/3 * {tabanalani} * {yukseklik} = {cevap}

Yani cevap: {cevap} birim kup
""" + ayrac2


#7
KoniHacmi = ayrac1 + """
Koninin taban yaricapi {r} birim, yuksekligi {yukseklik} birim ve pi {pi} ise
koninin hacmi 1/3 * {pi} * {r} * {r} * {yukseklik} = {cevap}

Yani cevap: {cevap} birim kup
""" + ayrac2