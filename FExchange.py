from AssetPrice import AssetPrice


class FExchange:
    """
    This is the main class that performs
    the function of simulating the processes
    of selling and buying shares on a financial exchange.
    """
    def __init__(self):
        self.__e_cash = 0  # The value of the financial portfolio
        self.__fin_p = {a.name: 0 for a in AssetPrice}  # Stocks in the financial portfolio

    def e_cash_show(self):
        """
        :return:Displays the value of all shares in the portfolio
        """
        self.__capital_calcul()
        print(self.__e_cash)

    def buy_shares(self):
        """
        The function performs the process of buying shares from the available.
        :return:
        """
        for i in AssetPrice:
            print(f"You have  {i} shares of {self.__fin_p[i]} ")
        for x in AssetPrice:
            print("You can to buy :", "\n", f"Company: {x.name}, coast: {x.value}")

    def sell_shares(self):
        """
        The function performs the process of selling shares
        from a financial portfolio.
        :return:
        """
        f_abil = False  # The possibility of selling something
        for i in AssetPrice:
            print(f"You have  {i} shares of {self.__fin_p[i]} ")
            if not f_abil:
                if self.__fin_p[i] > 0:
                    f_abil = True
        if not f_abil:
            print("You don't have any shares")

    def __capital_calcul(self):
        """
        The function calculates the sum of all the shares
         in the financial portfolio.
        :return: Current value of the financial portfolio.
        """
        for i in AssetPrice:
            self.__e_cash += self.__fin_p[i] * i.value
