#3
from brownie import VRFv2Consumer

def main():
    vrf_contract = VRFv2Consumer[-1]
    try:
        print("EL numero aleatorio solicitado a chainlink es :",vrf_contract.s_randomWords(0))
        print("Tu num de la suerte es:",(vrf_contract.s_randomWords(0) % 20)+1)
        print("-----------------------------------------------------")
        print("EL numero aleatorio solicitado a chainlink es :",vrf_contract.s_randomWords(1))
        print("Tu num de la suerte es:",(vrf_contract.s_randomWords(1) % 20)+1)
    except:
        print("esperate wey")