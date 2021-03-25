import random


result =random.random()*100
result2 =random.uniform(10,100)
result3 =random.randint(1,100) #tamsayı

print(result)
print(result2)
print(result3)



names=['Begüm','Bikem','Ümmügülsüm','Rüya','Ebru']

#result4=names[random.randint(0,len(names))] alttak, kısası
result5=random.choice(names)

print(f"Yakın zamanda {result5} le buluşacaksın")

liste= list(range(20)) #birden ona kadar liste olusturdu
print(liste)
random.shuffle(liste) # listeyi kardı
print(liste)
liste2=random.sample(liste,3) # listedenn 3 rastgele elemanı liste2 ye attı
print(liste2) 