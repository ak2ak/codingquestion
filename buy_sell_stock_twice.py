def buy_sell_stock(nums):
    profit_so_far = [0] * len(nums)
    maximum_profit_till_now = 0
    min_price = float('inf')
    for i, price in enumerate(nums):
        min_price = min(min_price, price)
        maximum_profit_till_now = max(
            maximum_profit_till_now,
            price-min_price
        )
        profit_so_far[i] = maximum_profit_till_now
    maximum_profit = float('-inf')
    for i, price in reversed(list(enumerate(nums[1:], 1))):
        maximum_profit = max(maximum_profit, price)
        maximum_profit_till_now = max(
            maximum_profit_till_now,
            maximum_profit - price + profit_so_far[i-1]
        )
    return maximum_profit_till_now


arr = [12, 11, 13, 9, 12, 8, 14, 13, 15]
print(buy_sell_stock(arr))
