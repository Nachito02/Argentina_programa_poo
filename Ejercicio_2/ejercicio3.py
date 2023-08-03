# Ejercicio 3 
# Un banco requiere de un software para realizar transferencias entre cuentas de clientes propios del banco. Para ello cuenta con una lista de cuentas identificadas por su CBU. Se requiere que el banco pueda realizar transferencias entre cuentas, crear nuevas cuentas de clientes, eliminar cuentas de clientes, listar las mismas ordenadas por cbu y por saldo ascendente y descendente. El Banco Central que regula a los bancos privados tiene como política que a cada cliente se le otorgue un descubierto de 10000 pesos. Tener en cuenta que el CBU de una cuenta es otorgado por el Banco Central.



class Cuenta:
    def __init__(self, cbu, saldo_inicial):
        self.cbu = cbu
        self.saldo = saldo_inicial
        self.descubierto = 1000


    def transferir(self,otra_cuenta, monto): 
        if monto > self.saldo + self.descubierto:
            return False
        else:
            print(self.cbu)
            self.saldo -= monto
            otra_cuenta.saldo += monto
            print(f"se transfirio {monto} a la cuenta {otra_cuenta.cbu}")
            return

    def obtener_saldo(self):
        return self.saldo
    


class Banco:
    def __init__(self):
        self.cuentas = []

    def crear_cuenta(self, cbu,saldo_inicial = 0):
        cuenta_nueva = Cuenta(cbu, saldo_inicial)
        self.cuentas.append(cuenta_nueva)
        print('Cuenta creada correctamente')
        return
    

    def eliminar_cuenta(self,cbu):
        self.cuentas = [cuenta for cuenta in self.cuentas if cuenta.cbu != cbu]

    def listar_por_cbu(self):
        listado = sorted(self.cuentas, key=lambda cuenta: cuenta.cbu)
        for lista in listado:
             print(lista.cbu) 
        return
    
    def listar_por_saldo_ascendente(self):
         listado = sorted(self.cuentas, key=lambda cuenta: cuenta.saldo)
         for lista in listado:
           print(lista.saldo) 
         return
    
    def listar_por_saldo_descendente(self):
        listado = sorted(self.cuentas, key=lambda cuenta: cuenta.saldo, reverse=True)
        for lista in listado:
            print(lista.saldo)
        return

if __name__ == '__main__':

    banco = Banco()

    banco.crear_cuenta('1234',1000)
    banco.crear_cuenta('1323',2000)

    cuenta1 = banco.cuentas[0]
    cuenta2 = banco.cuentas[1]

    cuenta1.transferir(cuenta2,500)
    banco.listar_por_cbu()
