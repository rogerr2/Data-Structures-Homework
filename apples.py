#Roger Robinson

def peaches():
    Price = [14,6,9,7,8,10,3,9]
    Limit = 100
    a = 0
    b = 0

    for i in range(len(Price)):
        apples = 100/Price[i]
        if (i < 7):
            profit = apples * Price[i + 1]
            a = profit
            if (a > b):
                a = b
                c = Price[i]
                d = Price[i + 1]

            print(profit)

        print("best possible profit is", b, "if you buy at", c, "and sell at", d)
peaches()
