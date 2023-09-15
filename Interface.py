from FExchange import FExchange


def interface():
    exchange = FExchange()
    do = 0

    print("1 - Sell \n",
          "2 - Buy \n",
          "3 -Show the value of the financial portfolio ",
          "4 - exit")

    while 1:

        try:
            do = int(input("Enter 1, 2 or 3"))
        except TypeError:
            print("Sorry! You enter no number!")

        if do == 1:
            exchange.sell_shares()

        elif do == 2:
            exchange.buy_shares()