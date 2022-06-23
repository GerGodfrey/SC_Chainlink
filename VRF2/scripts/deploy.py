#1
from brownie import VRFv2Consumer, accounts, config

def main():
    account = accounts.add(config["wallets"]["from_key"])
    vfconsumer = VRFv2Consumer.deploy(5667,{"from":account})
    return vfconsumer

    

