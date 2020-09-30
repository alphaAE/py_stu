
moneyStr = input("in money(Num $/￥):")

if moneyStr[-1] == '$':
    out = 6 * eval(moneyStr[0:-1])
    print("to ￥: {:.2f}￥".format(out))
elif moneyStr[-1] == '￥':
    out = eval(moneyStr[0:-1]) / 6
    print("to $: {:.2f}￥".format(out))
else:
    print("Err: temp type error!")