arabalar={}


def arabaEkle():
    barkod=input("Arabanın ID'si: ")
    marka=input("Arabanın Markası: ")
    model=input("Arabanın modeli: ")
    fiyat=input("Arabanın fiyatı: ")
    renk=input("Arabanın  rengi: ")


    arabalar.update({barkod:{
    'marka':marka,
    'model':model,
    'fiyat': fiyat,
    'renk': renk}})


    araba=arabalar[barkod]
    rapor=f"{araba['model']} model {araba['marka']} katologoa eklenmistir\n "
    print(rapor)


arabaEkle()
print(arabalar)
arabalar.clear()

print(arabalar)
