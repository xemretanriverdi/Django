liste=[1,2,3,4,5]

#iterator = yenileyici






class MyNumberss:
    def __init__(self,start,stop):
        self.start= start 
        self.stop= stop
    

    def __iter__(self):
        return self

    def __next__(self):
        if self.start<=self.start:
            x=self.start
            self.start += 1
            return x

        else:
            raise StopIteration

listem = MyNumberss(1,3)
for x in listem:
    print(x)