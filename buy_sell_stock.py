def buy_sell_stock(arr):
    max_profit = 0
    maximum_till = arr[0]
    for i in range(1, len(arr)):
        if maximum_till >= arr[i]:
            maximum_till = arr[i]
        else:
            max_profit = max(max_profit, arr[i] - maximum_till)
    return max_profit


print(buy_sell_stock([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
