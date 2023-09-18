from datetime import datetime
start_time = datetime.now()

m=12.35
L=[5,2,1,0.5,0.2,0.1,0.05]

for coin in L:
    while m >= coin and m!=0:
        txt = str(int(m/coin)) + " coins of "+str(coin)+" Euros"
        with open('greedy_output.txt', 'a') as f:
            f.write(txt)
        print(txt)
        m = m % coin
        m=round(m,2)
        
print('Coin change combinations are:')
print("Total combinations are", 1)
end_time = datetime.now()
print('Execution Time: {}'.format(end_time - start_time))