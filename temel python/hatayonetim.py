while True:
        try:

            x = int(input('x:'))
            y= int(input('y:'))
            print(x/y)

       # except Exception as ex:
    #    print('Yanlıs bilgii gierdiniz',ex)  genel

        except ZeroDivisionError:
            print("bolunen 0 olamaz")

        except ValueError:
            print("x y e sayısal olmalı")

        else :
            break

        finally:
            print("Valitaon tamamlandı")
 
  





        
        




