# time limit exceeded!  --> Solution2
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # indices local extreme values
        local_min = [0]                     # check first index
        local_max = [] 
        # ind : 1 to len(prices)-2
        for ind in range(1, len(prices)-1):
            # local maximum
            if prices[ind-1] < prices[ind] and prices[ind+1] <= prices[ind]:
                local_max.append(ind)
            # local minimum
            if prices[ind-1] > prices[ind] and prices[ind+1] >= prices[ind]:
                local_min.append(ind)
        local_max.append(len(prices)-1)     # check last index

        max_profit = 0
        for local_min_ind in local_min:
             for local_max_ind in local_max:
                 if local_min_ind < local_max_ind \
                    and prices[local_max_ind] - prices[local_min_ind] > max_profit:
                    max_profit = prices[local_max_ind] - prices[local_min_ind]

        return max_profit


# tracking local profits..
class Solution2:
    def maxProfit(self, prices: list[int]) -> int:
        local_min, local_max = prices[0], prices[0]
        profits = []
        for price in prices:
            # reset tracking
            if price < local_min:
                profits.append(local_max - local_min)
                local_min, local_max = price, price
                continue

            if price > local_max:
                local_max = price
        # append last (max - min)
        profits.append(local_max - local_min)
        # consider last price
        profits.append(prices[-1] - local_min)

        return max(profits)


# solutino in Book
class Solution3:
    def maxProfit(self, prices: list[int]) -> int:
        import sys
        profit = 0
        min_price = sys.maxsize

        # update min, profit 
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit
prices = [7,1,5,3,6,4]
print(Solution2().maxProfit(prices))