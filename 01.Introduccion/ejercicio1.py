#Ejercicio 1
#Una empresa necesita tener un registro de sus cuentas bancarias. En dichas cuentas se requiere poder depositar dinero, retirar dinero y saber el saldo de las mismas. Cada cuenta es identificada con un código único llamado CBU. Implemente una solución utilizando POO.

class Cuenta: 
    def __init__(self,cbu):

        self.cbu = cbu
        self.balance = 0

    def removeBalance(self, amount):
        if amount  > 0 :
            if(amount > self.balance):
                print(f"No posee saldo sufuciente para hacer el retiro")

            else:
                self.balance -= amount
                print(f"Se retiraron ${amount}, su nuevo saldo es de ${self.balance}")

        else:
            print('Error con el numero ingresado')
            
    def addBalance(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"se depositaron ${amount}. Su nuevo saldo es ${self.balance}")
        else :
            prit(f"El monto deve ser mayor a 0")

    def getBalance(self): 
       print(self.balance)




cuenta1 = Cuenta(123)

cuenta1.getBalance()

cuenta1.addBalance(2000)

cuenta1.removeBalance(1000)