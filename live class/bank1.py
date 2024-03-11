class Bank:
    def __init__(self):
        self.bankname ='UBA'
        self.rc_no = "203445"
        self.branch ='Abuja'

    def home(self):
        print(f'''
              welcome to {self.bankname}{self.rc_no},{self.branch}
            1.signup
            2.signin

''')   
bank =Bank()
bank.home()         


