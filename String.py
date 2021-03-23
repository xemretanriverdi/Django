website ="http://www.fsmayteam.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

str = ' Hello Word '

print(str.strip()) #basindaki ve sonundaki bosluklari siler
#ls soldaki bosluğu rstrip sağdaki boslugu temizler
print(website.lstrip('/:pth')) #soldan http sildi
print(course.lower()) #tum karakterleri kucultur
print(website.count('a')) #a sayisi
print(website.startswith("www")) #www ile mi basliyor
print(website.endswith("com")) #com ile mi bitiyor
print(course.isalpha()) #alfabetik mi
result ='Baslik'.center(50,'*') # center yerine ljust eklersen sola r just eklersen saga
print(result)