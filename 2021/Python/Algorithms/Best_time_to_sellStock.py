    def maxProfit(self, prices: List[int]) -> int:
        minn=prices[0]
        profit=0
        Maxprofit=0
        
        for i in range(len(prices)):
            if minn>prices[i]:
                minn=prices[i]
            
            elif minn<prices[i]:
                profit=prices[i]-minn
                if profit>Maxprofit:
                    Maxprofit=profit
        return(Maxprofit) 
