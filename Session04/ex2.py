prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}

stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
}
total = 0
for i in prices.keys():
    print(i)
    print('price',':',prices[i])
    print('stock',':',stock[i])
    p = prices[i] * stock[i]
    print(p)
    total = total + p
print("Total money you would make if you sold all of your food is:",total)




