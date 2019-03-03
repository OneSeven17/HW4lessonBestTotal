def best_total(shops_list):
    sales_sum = []
    for shop in shops_list:
        sales_sum.append(sum(shop))

    max_sale = max(sales_sum)
    sales_sum_index = []
    index = 0
    for sale in sales_sum:
        if sale == max_sale:
            sales_sum_index.append(index)
            sales_sum_index.append(sale)

        index += 1


    return sales_sum_index

shops = [
    [1000, 2000, 3000, 4000, 5000, 6000, 9000],
    [1000, 2000, 3000, 4000, 5000, 6000, 7000],
    [1000, 2000, 3000, 4000, 5000, 6000, 9000],

]

print(best_total(shops))

