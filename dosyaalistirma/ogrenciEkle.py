
def ekle(Ogrenci):
    with open("C:/Users/xemre/Desktop/Python/Django/dosyaalistirma/notlar.txt","a",encoding="utf") as file:
        
        
        file.write(f"\n{Ogrenci.no} {Ogrenci.lab1} {Ogrenci.lab2} {Ogrenci.lab3}")

    