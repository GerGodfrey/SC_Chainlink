from brownie import config, network, accounts, SaveNumber

def main():
    account = accounts.add(config["wallets"]["from_key"])
    print(f"La  cuenta es: {account}")

    savenumber = SaveNumber.deploy({"from": account}) # escoger que cuenta ejecutar la funcion
    return savenumber