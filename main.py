import random
class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"{self.n*self.n}")
    def cube(self):
        print(f"{self.n*self.n*self.n}")

    @staticmethod
    def hello():
        print("helllo user!")
    
c=calculator(23)
c.square()
c.cube()
c.hello()

class train(calculator):
    def __init__(slf,name):
        slf.name=name

    def book(self,fro,to):
        print(f"Tickets of {self.name} has been booked {fro} to the {to} and")

    def getstatus(self,trainNo,No_ofseats):
        print(f"the train number is {trainNo} and seat number is {random.randint(222,444)}")


t=train("shashank")
t.book("klb","bnglr")
t.getstatus(1234,random.randint)

class twoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f" the vector is {self.i}i + {self.j}j ")


class threeDvector(twoDvector):
    def __init__(self,k,i,j):
        super().__init__(i,j)
        self.k=k

    def show(self):
        print(f" the vector is {self.i}i + {self.j}j + {self.k}k")

a=twoDvector(1,2)
a.show()

b=threeDvector(4,6,3)
b.show()
