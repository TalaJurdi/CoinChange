def main():   
    from datetime import datetime
    start_time = datetime.now()
    coins = [5,2,1,0.5,0.2,0.1,0.05]
    target = 12.35
    
    def coinCombinations(coins, idx, target,text):
        if target == 0:
            return 1
        ways = 0
        for i in range(idx, len(coins)):
            if target - coins[i] >= 0:
                ways += coinCombinations(coins, i, round(target-coins[i],2))
        return ways
    print('Coin change combinations are:')
    res = coinCombinations(coins, 0, target)
    print("Total combinations are", res)
    end_time = datetime.now()
    print('Execution Time: {}'.format(end_time - start_time))
    
main()