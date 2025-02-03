import time
import random
def StockPriceManipulator(baseprice, volatility, steps):
    price = baseprice
    
    for _ in range(steps):
        change_percentage = random.uniform(-volatility, volatility)
        price *= (1 + change_percentage)
        print(f"Stock Price: {price:.2f}")
        time.sleep(1)
StockPriceManipulator(500,0.1,10)