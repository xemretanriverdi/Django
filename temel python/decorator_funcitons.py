#decoators

def my_decor(func):
    def wrapper():
        print("fonksiyondan once islemler")
        func()
        print("fonksiyondan sonraki islemler")

    return wrapper


@my_decor #otomatikmen decora gönderir
def sayHello():
    print("Hello")



def sayGreeting():
    print("gretting")


sayHello()
