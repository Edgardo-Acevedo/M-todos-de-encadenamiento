class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        if(self.account_balance < 0):
            print(f'el saldo de {self.name} es insuficiente')
        return self
    def display_user_balance(self):
        print(f'Su Nombre es {self.name} - Su email es {self.email} - Su Saldo es {self.account_balance}')
        return self
        
# JUANITA
Juanita = Usuario('Juanita', 'Juanita123@gmail.com')
Juanita.make_deposit(100).make_deposit(50).make_deposit(10).make_withdrawal(50).display_user_balance()

# PEDRITO
Pedrito = Usuario('Pedro', 'Pedro@gmail.com')
Pedrito.make_deposit(50).make_deposit(50).make_withdrawal(50).make_withdrawal(60).display_user_balance()

# ESTEBAN
Esteban = Usuario('Esteban', 'EstebanElCuchuflí@gmail.com')
Esteban.make_deposit(200).make_withdrawal(10).make_withdrawal(60).make_withdrawal(15).display_user_balance()


