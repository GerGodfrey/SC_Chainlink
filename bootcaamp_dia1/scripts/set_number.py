from brownie import SaveNumber, accounts, config

def set_number():
    account = accounts.add(config["wallets"]["from_key"])
    savenumber = SaveNumber[-1] #trabajo con el ultimo despligue de mii contrato 
    tx = savenumber.SetNumber(20, {'from': account})
    return tx 
def main():
    set_number()