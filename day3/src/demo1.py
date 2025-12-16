import statistics

# vinhonmes
vhm_2023 = [48, 49, 50, 50, 51, 52, 53, 54, 55, 56, 58, 60]

# mean, median
# standard deviation

# Compute both population and sample standard deviation for clarity.
mean = statistics.mean(vhm_2023)
median = statistics.median(vhm_2023)
population_std = statistics.pstdev(vhm_2023)
sample_std = statistics.stdev(vhm_2023)

print("VHM")
print("mean", mean)
print("median", median)
print(f"Population standard deviation of vhm_2023: {population_std:.2f}")
print(f"Sample standard deviation of vhm_2023: {sample_std:.2f}")
print(f"-> varicent: {population_std/mean* 100}")
# FLC
flc = [3.2, 3.5, 4.0, 5.5, 7.0, 9.5, 6.0, 4.5, 3.8, 3.2]


mean_flc = statistics.mean(flc)
median_flc = statistics.median(flc)
population_std_flc = statistics.pstdev(flc)
sample_std_flc = statistics.stdev(flc)

print()
print("FLC")
print("mean", mean_flc)
print("median", median_flc)
print(f"Population standard deviation of flc: {population_std_flc:.2f}")
print(f"Sample standard deviation of flc: {sample_std_flc:.2f}")
print(f"-> varicent: {population_std_flc/mean_flc* 100}")

# Should be choose?
