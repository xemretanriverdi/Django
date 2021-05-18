#hata yonetimi ornekleri 

# girilen parolada türkçe karakter varsa belirt


listem=list()
while True:
    deger = input("sayi giriniz: ")
    
    if(deger=='done'):
        
        break   
    try:
        result=(float(deger))

    except ValueError:
        print("Invalid input")
        continue
    
    listem.append(deger)


max=deger
min=deger        
for x in listem:
    if(x>max):
        max=x
    if(x<min):
        min=x
    
    print(listem)


print("max : ",max)
print("min : ",min)





  

