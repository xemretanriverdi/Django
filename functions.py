def factotial (number):
    if not isinstance(number,int): # number int değilse
        raise TypeError(" number must be ann integer")

    if not number >=0 :
        raise ValueError("number must be zero or positive")
    def inner_factorial(number):
        if(number<=1):
            return 1

        return number* inner_factorial(number -1 )
        
    return inner_factorial(number)


print(factotial(3))
