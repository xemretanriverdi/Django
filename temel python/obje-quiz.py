

class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer

    def chekAnswer(self,answer):
        return (self.answer==answer)

        


q1=Question("En iyi futbol kulübü",["Fenerbahce","Galatasaray","Erzurum","Besiktas"],"Fenerbahce")
q2=Question("En iyi yazılım dili",["Java","C++","Python","C#"],"Python")
q3=Question("En iyi şehir",["Ankara","Erzurum ","Antalya","İstanbul"],"İstanbul")
q4=Question("En iyi lider",["Biden","RTE","Trump","Putin"],"RTE")

liste=[q1,q2,q3,q4]

print(q1.chekAnswer("Fenerbahce"))


class Quiz:
    print("Quiz baslıyor")
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionsIndex=0
        

        

    def sor(self):
        sık=['a','b','c','d']
        sıkIndex=0
        for x in self.questions:
            self.questionsIndex+=1

            print(f"\n \n{self.questionsIndex}.) Soru: {x.text}\n")
            for y in x.choices:
                print(f"{sık[sıkIndex]}.) {y}")
                sıkIndex+=1

            sıkIndex=0
            sonuc=input()
            self.score+=(int(sonuc==x.answer)*25)
        print(f"Total scorenuz: {self.score}")

        



s1 = Quiz(liste)
s1.sor()
    




