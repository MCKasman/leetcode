class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

        Algorithm
        
        [7,1,5,3,6,4] --> i = 0, j = 1, loop until j is index 5

        1. Traverse through array, i is left pointer and j is right pointer
        2. If value of j is greater than value of i, find the difference between the two and           add to max profit
        3. Return maxprofit
        """
        i = 0
        j = 1
        maxprofit = 0
        length = len(prices)

        while(j < length):
            if(prices[j] > prices[i]):
                maxprofit += prices[j] - prices[i]

            i+=1
            j+=1

        return maxprofit
