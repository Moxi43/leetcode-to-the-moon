// Link to the problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

function maxProfit(prices: number[]): number {
    var minprice = prices[0];
    var maxprice = 0;
    for (var i=0; i<prices.length; i++) {
        if (minprice > prices[i]) {
            minprice = prices[i];
        }
        else if (prices[i] - minprice > maxprice) {
            maxprice = prices[i] - minprice;
        }
    }
    return maxprice;
};