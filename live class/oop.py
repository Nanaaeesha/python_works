# class Dust:
#     def __init__(self): #initialization
#       self.first_name = "Abdulazeez"
#       self.last_name ="Aisha"
#       self.age = "24"

#       self.naming()

#     def naming(self):
#         print(f'my name is {self.first_name} {self.last_name}.i am {self.age}')


    
# father = Dust()
# father.naming()


# def call_name(name:str):
#     name= input('first name:').strip()
    
#     x=input('first name:')
#     print('my name is ',name)
#     call_name(x)
class Calculator:
  def __init__(self):
    self.calc_name ='casio'

    self.home()

  def home(self):
    print(f'welcome to{self.calc_name}')
    self.value1=float(input('first value:'))
    self.value2=float(input('second value:'))
    user = input('''
        choose your operation ;  
          1. Addition
          2. subtraction
          #.exit       
      option: ''')
  #   if user=='1':
  #       self.addition()
  #   elif user=='2':
  #         self.subtraction()
  #   elif user=='#' :
  #      exit()
  #   else:
  #      print('invalid option,try again!')
  #      self.home()

  # def addition(self):
  #    print(f'Ans: {self.value1+value2}') 
  #    self.decide() 

  # def subtraction(self):
  #    print(f'Ans: {self.value1-value2}') 
  #    self.decide()                 



# mycalc = Calculator()
# mycalc.home()



#INHERITANCE
class parent:
    def __init__(self) -> None:
        self.surname = 'ojo'
        self.firstname ='mary'
        self.hobby="eating"

        # self.describe()
    def describe(self):
       print(f'my name is{self.firstname}{self.surname},i love {self.hobby}')    

# parent = parent() 
class child(parent): 
    def __init__(self) -> None:
       super().__init__()
       self.firstname = 'maimunah'
       self.hobby='sleeping'

       self.describe()           
# child =child()


class Grandchild(child):
    def __init__(self) -> None:
      child().__init__()
      self.firstname = 'raji'
      self.hobby='playing'

      self.describe()

grandchild=Grandchild()
















