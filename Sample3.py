#Hello everyone
class Hi():
    def __init__(self,name,age):
        self.n=name
        self.a=age
    
class Hello(Hi):
    def __init__(self,name,age,work):
        super().__init__(name,age)
        self.w=work
    def welcome(self):
        print(f"Name : {self.n}\nAge: {self.a}\nWork : {self.w}")


S1=Hello("Vinoth","36","TCS")
S2=Hello("Pavithra","32","TCS")
S1.welcome()
S2.welcome()
