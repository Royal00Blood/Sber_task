from FExchange import FExchange


def interface():
    exchange = FExchange()
    action = None

    print(" 1 - Sell \n",
          "2 - Buy \n",
          "3 - Show the value of the financial portfolio ",
          "4 - exit")

    while 1:

        try:
            action = int(input("Enter 1, 2, 3 or 4: "))
        except ValueError:
            print("Sorry! You enter no number!")

        if action == 1:
            exchange.sell_shares()

        elif action == 2:
            exchange.buy_shares()

        elif action == 3:
            exchange.e_cash_show()

        elif action == 4:
            exit()
