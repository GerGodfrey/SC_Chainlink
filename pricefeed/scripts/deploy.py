from brownie import PriceConsumerV3, accounts, config

def main():
    account = accounts.add(config["wallets"]["from_key"])
    priceconsumer = PriceConsumerV3.deploy({"from":account})
    return priceconsumer