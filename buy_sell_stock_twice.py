def buy_sell_stock(arr):
    maximum_till_now = arr[0]
    maximum_profit = 0
    iteration = 0
    for i in range(1, len(arr)-1):
        if arr[i] > maximum_till_now:
            maximum_profit = max(maximum_profit,arr[i]-maximum_till_now)
        else:
            iteration = i
            maximum_till_now = arr[i]
    if arr[-1] - maximum_till_now > maximum_profit:
        iteration = len(arr) - 1
        maximum_profit = arr[-1] - maximum_till_now
    return maximum_profit, iteration


arr = [7, 7, 7, 9, 9, 9, 5, 8, 6]
maximum_profit_first, item_to_remove = buy_sell_stock(arr)
arr.pop(item_to_remove)
maximum_profit_second,item_to_remove = buy_sell_stock(arr)
print(maximum_profit_first,maximum_profit_second)