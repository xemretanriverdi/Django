#class #object, instanca

class Araba:
    pass #simdilik
    adres='no information'

    def __init__(self,marka,model,year):
        self.marka=marka
        self.model=model
        self.year=year
        print('init methodu calısır')

    def intro(self):
        print(f'{self.marka} {self.model} {self.year} tarihinde {self.adres} şehrinde üretildi' )

    def km(self):
        print(f"Araba {2021-self.year} yasında")

a1= Araba('Bmw','M5',2021)
a1.adres="istanbul"

print(a1.adres)

a1.intro()
a1.km()
    