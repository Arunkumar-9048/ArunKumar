class Calculator:
    def __init__(self):
        self.a= float(input("Enter your 1st number: "))
        self.b= float(input("Enter your 2nd number: "))
        self.operation= input("Enter your Operation: ")
    
        match (self.operation):
            case "+":
               return print(self.a+self.b)
            case "-":
               return print(self.a-self.b)
            case "*":
               return print(self.a*self.b)
            case "/":
               return print(self.a/self.b)
            case _:
                return print("Operation invalid")

ob1= Calculator()

