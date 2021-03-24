#class #object, instanca

class Araba:
    pass #simdilik
    adres='no information'

    def __init__(self,marka,model,year):
        self.marka=marka
        self.model=model
        self.year=year
        print('init methodu calısır')




a1= Araba('Bmw','M5',2021)
a1.adres="istanbul"

print(a1.adres)


    