"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #11 - Stonks (stonks.py)


Author: Chris Lai

Difficulty Level: 8/10

Background: Paul recently got a nice bonus from work and wanted to invest it into the 
stock market. In order to maximize his profit, Paul analyzed some data from recent 
transactions in order to find out which combination of buying and selling stocks would 
net the highest earnings.

Prompt: Given a list of prices (prices[i]) collected throughout the day, find the highest 
profit that Paul can earn if he buys the stock during any hour of the day and then sells 
it during the same day. In total, Paul may buy/sell a total of two times per day, with 
the condition that he must sell everything before buying again.

Constraints: The number of prices “n” in the list are constrained to 24 >= n > 0 and 
the prices “i” must be constrained to 10^5 >= i >= 0.

Test Cases:
Input: [1, 2, 3, 4, 5, 0], Output: 4
Buy during hour 1 (price = 1), sell during hour 5 (price = 5), net profit = 5 - 1 = 4

Input: [7, 5, 3, 2, 1], Output: 0
DO NOT BUY (declining prices, no profit possible)

Input: [1, 3, 3, 5, 4, 0, 3, 8, 5, 5], Output: 12
Buy during hour 1 (price = 1), sell during hour 4 (price = 5), net profit = 5 - 1 = 4. 
Then, buy during hour 6 (price = 0), sell during hour 8 (price = 8), net profit = 8 - 0 = 8. 
Total profit = 4 + 8 = 12.
"""

class Solution:
    def stonks(self, prices):
        # profit = 0
        # startindex = 0
        # for i in range(0, len(prices)-1):
        #     if i+1 < i or i+1 == len(prices)-1:
        #         print(prices[i] - prices[startindex])
        #         if prices[i] - prices[startindex] > 0:
        #             profit+=(prices[i] - prices[startindex])
        #         startindex = i+1
        # return profit

        profit = 0
        list1 = []
        list2 = []

        min = 100000
        max1 = 0
        for x in prices:
            if x < min:
                min = x
            if max1 < x - min:
                max1 = x - min
            list1.append(max1)

        maxi = -1
        max2 = 0
        for x in prices[::-1]:
            if x > maxi:
                maxi = x
            if max2 < maxi - x:
                max2 = maxi - x
            list2.append(max2)

        list2 = list2[::-1]
        vals = [a + b for a, b in zip(list1, list2)]
        return max(vals)


def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.stonks(array)
    print(ans)

if __name__ == "__main__":
    main()