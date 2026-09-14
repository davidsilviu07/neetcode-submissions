class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]   # minimul de până acum 
        best = 0                # output

        for price in prices:
            # actualizez minimul dacă găsesc un preț mai mic
            if price < min_price:
                min_price = price
            #  verific ce profit aș face vânzând azi
            else:
                best = max(best, price - min_price)

        return best