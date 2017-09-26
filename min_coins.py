import sys

# determine the minimum 
# number of coins needed 
# to sum to total_value
total_value = 11
coins_list = [1, 3, 5]
min_coins = []
for i in range(total_value+1):
	min_coins.append(sys.maxint)

min_coins[0] = 0

S = total_value + 1
N = len(coins_list)
for i in range(1, S):
	for j in range(0, N):
		v_j = coins_list[j]
		if v_j <= i and min_coins[i-v_j] + 1 < min_coins[i]:
			min_coins[i] = min_coins[i-v_j] + 1

print min_coins[9]