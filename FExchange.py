from AssetPrice import AssetPrice
from decimal import Decimal
import numpy as np
import pandas as pd


class FExchange:
    def __init__(self):
        self.__e_cash = 0  # The value of the financial portfolio

    def e_cash_show(self):
        print(self.__e_cash)

    def buy_shares(self):
        '''Реализовать графический интерфейс с гиф-котом (может быть музыкой)'''
        pass

    def sell_shares(self):
        pass


# for x in AssetPrice:
#     print(x.name, x.value)
# >>  LKOH 5896
# >>  SBER 250