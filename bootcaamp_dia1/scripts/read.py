from brownie import SaveNumber

def read():
    savenumber = SaveNumber[-1] #trabajo con el ultimo despligue de mii contrato 
    print(f"El numero almacenado en el contrato inteligente es: {savenumber.numero()}")

def main():
    read()