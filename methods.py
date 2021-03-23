liste =[12,123,123,1]

liste.append(99)
print(liste)

#map metodu


def kare(x):

    return x**2

numbers=[2,12,13,5]

result = list(map(kare,numbers))
print(result)

result = list(map(lambda num:num**2,numbers))


print(result)