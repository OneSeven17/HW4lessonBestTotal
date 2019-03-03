
def top_3(shops_list):
    top_3_sales = []
    index = 0
    for shop in shops_list:
        top_3_sales.append(index)
        top_3_sales.append(sorted(shop)[4:7])

        index += 1


    return top_3_sales

shops = [
    [10000, 2000, 3000, 4000, 5000, 6000, 9000],
    [1000, 20000, 3000, 4000, 5000, 6000, 7000],
    [1000, 2000, 3000, 4000, 5000, 6000, 9000],

]

print(top_3(shops))

