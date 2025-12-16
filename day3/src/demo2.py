import statistics


btc = [12, -8, 5, 18, -15, 22, 7, -10, 14, 9, -6 , 20]
eth = [10, -5, 6, 15, -10, 18, 5, -8, 12, 7, -4, 16]

#% lợi nhuận in 12 month

mean_btc = statistics.mean(btc)
mean_eth = statistics.mean(eth)

print(f"Mean BTC: {mean_btc:.2f}")
print(f"Mean ETH: {mean_eth:.2f}")

median_btc = statistics.median(btc)
median_eth = statistics.median(eth)

print(f"Median BTC: {median_btc:.2f}")
print(f"Median ETH: {median_eth:.2f}")

population_std_btc = statistics.pstdev(btc)
population_std_eth = statistics.pstdev(eth)

print(f"Population Std Dev BTC: {population_std_btc:.2f}")
print(f"Population Std Dev ETH: {population_std_eth:.2f}")

variance_btc = statistics.variance(btc)
variance_eth = statistics.variance(eth)

print(f"Variance BTC: {variance_btc:.2f}")
print(f"Variance ETH: {variance_eth:.2f}")

print(f"{population_std_btc/mean_btc * 100:.2f}% > < {population_std_eth/mean_eth * 100:.2f}%")