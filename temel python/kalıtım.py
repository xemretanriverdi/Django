#Inheriance



class Animal:

    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

        print('Animal Created')

    def Whoıam(self):
        print(f"I am {self.fname}")
        
class Cat(Animal):
    def __init__(self,fname,lname,pati):
        self.pati=pati
        Animal.__init__(self,fname,lname) # super().__init__(fname,lname) yazılabilr
       
        print('Cat Created')
    

    #override üstü tiklemedi
    def Whoıam(self):
        print(f"I am {self.lname}")

    



c1 =Cat('minnos','fıstık','pamuk')


print(c1.fname)
c1.Whoıam()
print(c1.pati)




class Movie:
    def __init__(self,tittle,director,duration):
        self.tittle=tittle
        self.director=director
        self.duration=duration
        print("Movie Objesi Oluşturuldu")

