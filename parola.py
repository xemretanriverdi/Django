def chec_password(psw):
    import re
    if len(psw)<8:
        raise Exception("Parola en az 8 karakter olmalı")
    
    elif not re.search("[a-z]",psw):
        raise Exception("parola kücük harf icermelidir")
    elif not re.search("[A-Z]",psw):
        raise Exception("parola büyük harf icermelidir")

    elif not re.search("[0-9]",psw):
        raise Exception("parola rakam icermelidir")

    elif  re.search("\s",psw):
        raise Exception("parola bosluk icermemelidir")

    else :

        print("Gecerli parola")


password = "asqwqweqweqweqw"
try:

    chec_password(password)

except Exception as ex:
    print(ex)

else:
    print("Gecerli parola")

finally:
    print("Valitaon tamamlandı")





def _TurkceKarakterKontrol(parola):

    import re

    if re.search("[İÖÜŞĞÇşş]",parola):
        raise Exception("Turkce karakter var")

    else:
        "Parola güncellendi"


while True:
    try:

        parola = (input("Parola giriniz: "))

        _TurkceKarakterKontrol(parola)

    except Exception as ex:
        print(ex)

    else : 
        print("parola onaylandı")
        break
    finally:
        print('kontrol bitti')
    
    

    



