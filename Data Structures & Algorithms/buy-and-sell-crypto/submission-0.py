class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Understand- Return the maximum profit by choosing a single day to buy and
                    choosing a day in the future to sell
        Plan- 
            max_profit = 0
            set min_price to a really high number 

            Loop through prices:
                if price is less then min_price:
                    min_price = price
                
                then calculate profit

                set max_profit 

            return max_profit
        Implement-
        '''

        max_profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            max_profit = max(max_profit, profit)

        
        return max_profit