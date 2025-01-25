public class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = prices[0];
        int maxProfit = 0;
        
        for (int price : prices) {
            if(price < minPrice) minPrice = price;
            int currentProfit = price - minPrice;
            if(currentProfit > maxProfit) maxProfit = currentProfit;
        }

        return maxProfit;
    }
}