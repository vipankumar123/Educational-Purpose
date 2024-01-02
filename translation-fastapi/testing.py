class CoinPurse:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.total_value = 0
    
    def add_coin(self, coin_value):
        self.total_value += coin_value
    
    def print_information(self):
        print(f"{self.owner_name} has {self.total_value} cents")

name = input('Enter owner name: ')
purse = CoinPurse(name)
while True:
    value = int(input('Enter coin value (cents): '))
    if value <= 0:
        break
    purse.add_coin(value)
purse.print_information()
