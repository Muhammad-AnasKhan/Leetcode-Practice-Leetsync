public class Solution {
    public int MaxProfit(int[] prices) {
        int maxProfit = 0;
        int buy = 0;
        int sell = 1;
        while (buy < sell && sell < prices.Length){
            if (prices[buy]<prices[sell]){
                if (maxProfit < (prices[sell] - prices[buy]))
                    maxProfit = prices[sell] - prices[buy];
            }
            else{
                buy = sell;
            }
            sell++;
        }
        return maxProfit;
    }
}