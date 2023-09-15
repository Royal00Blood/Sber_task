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
        self.__f_abil = False  # The possibility of selling something

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
            print(f"-----------> You have  {i.name} shares of {self.__fin_p[i.name]} ")
        print("You can to buy :")
        for x in AssetPrice:
            print(f"-----------> Company: {x.name}, coast: {x.value}")
        self.__action_shares()

    def sell_shares(self):
        """
        The function performs the process of selling shares from a financial portfolio.
        :return:
        """
        for i in AssetPrice:
            if not self.__f_abil:
                if self.__fin_p[i.name] > 0:
                    self.__f_abil = True
                    print(f"You have  {i.name} shares of {self.__fin_p[i.name]} ")
        if not self.__f_abil:
            print("You don't have any shares")
        else:
            self.__action_shares(incr=False)

    def __action_shares(self, incr=True):
        """
        Function for changing the values of stocks in the financial portfolio.
        :param incr: А logical variable that determines the increase or decrease of a block of shares.
        :return:
        """
        while 1:
            n_promotion = input('Enter name of the promotion: ')
            if n_promotion in self.__fin_p:
                break
            else:
                print("Enter again. You have  mistake. (Example: SBER)")
        while 1:
            try:
                c_promotion = int(input('Enter the number of shares to buy: '))
            except ValueError:
                print("Enter again")
            else:
                break
        if incr:
            self.__fin_p[n_promotion] += c_promotion
        else:
            self.__fin_p[n_promotion] -= c_promotion

    def __capital_calcul(self):
        """
        The function calculates the sum of all the shares in the financial portfolio.
        :return: Current value of the financial portfolio.
        """
        for i in AssetPrice:
            self.__e_cash += self.__fin_p[i.name] * i.value
