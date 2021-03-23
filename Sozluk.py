ogrenciler = {}

number =    input("öğrenci no : ")
name =      input("öğrenci ismi : ")
surname =   input("öğrenci soyadı : ")
telefon =   input("öğrenci telefon : ")

ogrenciler.update({number:{
    'ad':name,
    'soyad':surname,
    'telefon': telefon

}})
number =    input("öğrenci no : ")
name =      input("öğrenci ismi : ")
surname =   input("öğrenci soyadı : ")
telefon =   input("öğrenci telefon : ")
        
ogrenciler.update({number:{
    'ad':name,
    'soyad':surname,
    'telefon': telefon

}})


print(ogrenciler)

print('*'*100)


ogrNo = input('ogrenci no giriniz: ')
ogrenci = ogrenciler[ogrNo]
print(ogrenci)

print(f"Ogrenci bilgileri\n {ogrNo} nolu ogrencinin adı: {ogrenci['ad']}") 


