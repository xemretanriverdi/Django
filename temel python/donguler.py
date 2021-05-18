sehirler= ['istanbul','erzurum','ankara','izmir','rize']

for x in sehirler:
    print(x.title()) # bas harf büyütür
    if(x.__len__()>5):
        print(f"{x} sehri 5 harften daha uzundur")


for item in range(1,100,5): # ilk eleman, son eleman, artıs miktarı
    print (item)

print(list(range(10,100,3)))  #liste formatında yazar



years=[1971,1979,1999,1999,2000]
names=['Cemalettin', 'sevda', 'ahmet','emre','zehra']
names=[name.title() for name in names]
ages= [2021-year for year in years]

for item in zip(ages,names):
    print(item)



def asalmi(x):

    q = 2;
    while(q<x):
        

        if(x%q==0):
            return False
            break
        q+=1
    return True
    

print(asalmi(4))
        