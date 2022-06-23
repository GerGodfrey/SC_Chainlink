from brownie import PriceConsumerV3

def read():
    price_consumer = PriceConsumerV3[-1]
    price_consumer = round(price_consumer.getLatestPrice()/1e8,2)
    print(f"El precio de BNB/USD es {price_consumer}")

def main():
    read()

# brownie compile
# brownie run scripts/deploy.py --network rinkeby