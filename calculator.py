print("Hello, this is Srijan's calculator")

while True:
    print("You can perform arithmetic operations of following types\n")
    print("1.With Real numbers")
    print("2.With Complex numbers")
    choice_calc  = int(input("Enter your choice among 1 or 2\n"))

    if (choice_calc == 1):
        print("You opted for real number calculation")

        print("Now enter two positive number operands")
        ar = int(input("Enter 1st operand: "))
        br = int(input("Enter 2nd operand: "))
        



        class NegValException(Exception):
            if (ar<0 or br<0):
                raise("Negative operands not accepted")

        print("Now enter an arithmaetic operator among these:\n'+'\n'-'\n'*'\n'/'\n")
        ar_op = input("enter the arithmetic operator\n")

        
        

    class Simple:
        
            def __init__(self,a,b):
                self.a1 = a
                self.b1 = b
                

            
            def add(self,a,b):
                return  a + b
                

            def subtract(self,a,b):
                return a - b
                

            def multiply (self,a,b):
                return a * b
                

            def divide (self,a,b):
                return a / b

            def display (self):
                print("Result is: ",end='')
                if (ar_op == '+'):
                    print(self.add(self.a1,self.b1))
                elif (ar_op == '-'):
                    print(self.subtract(self.a1,self.b1))
                elif (ar_op == '*'):
                    print(self.multiply(self.a1,self.b1))
                elif (ar_op == '/'):
                    print(self.divide(self.a1,self.b1))

    if (choice_calc == 1):
        s = Simple(ar,br)
        s.display()

    if (choice_calc == 2):
        print("You opted for complex number calculation")

        print("Enter positive operands only")
        print("Enter real and imaginary parts of first complex number")

        real1 = int(input('real  :'))
        img1 = int(input('imaginary :'))

        print("Enter real and imaginary parts of second complex number")   
        real2 = int(input('real :'))
        img2 = int(input('imaginary :'))

        op_list = [real1,img1,real2,img2]

        class NegValException(Exception):
            if (real1<0 or real2<0  or img1<0 or img2<0):
                raise("Negative operands not accepted")

        print(f"Entered complex numbers are: {real1}+{img1}i and {real2}+{img2}i")   

        print("Now enter an arithmaetic operator among these:\n'+'\n'-'\n'*'\n'/'")
        ar_op = input("enter the arithmetic operator\n")

    class Complex(Simple):
        def __init__(self,*args):
                self.ar = args[0]
                self.aim= args[1]
                self.br = args[2]
                self.bim = args[3]

        def __add__(self):
                res_real = self.ar + self.br
                res_img = self.aim + self.bim
                return complex(res_real,res_img)

        def __sub__(self):
                res_real = self.ar - self.br
                res_img = self.aim - self.bim
                return complex(res_real,res_img)

        def __mul__(self):
                res_real = (self.ar*self.br) - (self.aim*self.bim)
                res_img = (self.ar*self.bim) + (self.aim*self.br)
                return complex(res_real,res_img)

        def __truediv__(self):
                res_real = ((self.ar*self.br) + (self.aim*self.bim))/(self.br**2 + self.bim**2)
                res_img = (-(self.ar*self.bim) + (self.aim*self.br))/(self.br**2 + self.bim**2)
                return complex(res_real,res_img)
                

        def display(self):
                print("Result is: ",end='')
                if (ar_op == '+'):
                    print (self.__add__())
                elif (ar_op == '-'):
                    print (self.__sub__())
                elif (ar_op == '*'):
                    print (self.__mul__())
                elif (ar_op == '/'):
                    print (self.__truediv__())
            

    if (choice_calc == 2):
        c= Complex(*op_list)
        c.display()

    if (choice_calc != 2 and choice_calc !=1):
        print("Invlaid option! Please make your choice again")

    
    choice_quit = input("Do you want to quit?y or n: ")
    if (choice_quit == "y"):
        exit()
