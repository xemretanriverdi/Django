notlarDosyasi=open("C:/Users/xemre/Desktop/Python/Django/dosyaalistirma/notlar.txt","r",encoding="utf")
class Ogrenci:

   

    def __init__(self,no,lab1,lab2,lab3):
        self.no=no
        self.lab1=lab1
        self.lab2=lab2
        self.lab3=lab3
        
        
    def ortalama(self):
        toplam =((self.lab1)+(self.lab2)+(self.lab3))/3
        return toplam

    def info(self):
        return(f'{self.no} numaralı ogrenci notları : \nLab1: {self.lab1}\nLab2: {self.lab2}\nLab3: {self.lab3}\nOrtalama:{self.ortalama()}')


notlar=notlarDosyasi.readlines()
dersAdı=notlar[-1]
notlar=notlar[1:-1:]
ogrenciler=[]
for quiz in notlar:
    quiz=quiz[:-1:]
    quiz=quiz.split(" ")
    no=int(quiz[0])
    lab1=float(quiz[1])
    lab2=float(quiz[2])
    lab3=float(quiz[3])
    ogrenciler.append(Ogrenci(no,lab1,lab2,lab3))


girilen="1821221023"
enbuyukOgrenci=Ogrenci(1,0,0,0)
enKucukOgrenci=Ogrenci(1,100,100,100)
enbuyukOgrenciOrt=Ogrenci(1,0,0,0)


for ogrenci in ogrenciler:
    if(ogrenci.lab1>=enbuyukOgrenci.lab1):
        enbuyukOgrenci=ogrenci
    if(ogrenci.ortalama()<enKucukOgrenci.ortalama()):
        enKucukOgrenci=ogrenci

    if(ogrenci.ortalama()>=enbuyukOgrenciOrt.ortalama()):
        enbuyukOgrenciOrt=ogrenci
    


print(f"En Buyuk Lab1 Notu: {enbuyukOgrenci.info()}\n")
print(f"En Kucuk Ortalama: {enKucukOgrenci.info()}\n")
print(f"En Buyuk Ortalama: {enbuyukOgrenciOrt.info()}")

def ekle(Ogrenci):
    with open("C:/Users/xemre/Desktop/Python/Django/dosyaalistirma/notlar.txt","a",encoding="utf") as file:
        
        
        file.write(f"\n{Ogrenci.no} {Ogrenci.lab1} {Ogrenci.lab2} {Ogrenci.lab3}")

        
Emre=Ogrenci(111111,33,34,35)

print(Emre.info())

