scores = [0, 6, 7, 8, 9, 10]

# ============================================
# BOX PLOT TUTORIAL - Complete Guide
# ============================================

"""
WHAT IS A BOX PLOT?
A box plot (box-and-whisker plot) visualizes data distribution using 5 key statistics:
1. Minimum (lowest value, excluding outliers)
2. Q1 (First Quartile) - 25th percentile
3. Median (Q2) - 50th percentile (middle value)
4. Q3 (Third Quartile) - 75th percentile
5. Maximum (highest value, excluding outliers)

BOX PLOT STRUCTURE:
    |
    |---- (whisker extends to minimum)
    |
  ┌─┴─┐
  │   │  <- Box from Q1 to Q3 (Interquartile Range - IQR)
  ├───┤  <- Line at median (Q2)
  │   │
  └─┬─┘
    |
    |---- (whisker extends to maximum)
    |
    *    <- Outliers (if any)

KEY FORMULAS:
- Q1 position = (n + 1) * 0.25, where n = number of data points
- Q2 position (Median) = (n + 1) * 0.50
- Q3 position = (n + 1) * 0.75
- IQR (Interquartile Range) = Q3 - Q1
- Lower fence (outlier threshold) = Q1 - 1.5 * IQR
- Upper fence (outlier threshold) = Q3 + 1.5 * IQR
"""

# ============================================
# METHOD 1: Manual Calculation (Understanding the Math)
# ============================================

print("=" * 60)
print("METHOD 1: MANUAL CALCULATION - STEP BY STEP")
print("=" * 60)

# Step 1: Sort the data (REQUIRED for quartile calculation)
sorted_scores = sorted(scores)
print(f"\nOriginal scores: {scores}")
print(f"Sorted scores: {sorted_scores}")
print(f"Number of data points (n): {len(sorted_scores)}")

# Step 2: Find Minimum
minimum = sorted_scores[0]
print(f"\nMinimum: {minimum}")

# Step 3: Find Maximum
maximum = sorted_scores[-1]
print(f"Maximum: {maximum}")

# Step 4: Calculate Median (Q2)
# Formula: If n is odd, median is the middle value
#          If n is even, median is the average of two middle values
n = len(sorted_scores)
if n % 2 == 1:
    # Odd number of elements
    median_index = n // 2
    median = sorted_scores[median_index]
    print(f"\nMedian (Q2) - Odd count:")
    print(f"  Position: {median_index + 1} (index {median_index})")
    print(f"  Value: {median}")
else:
    # Even number of elements
    mid1 = n // 2 - 1
    mid2 = n // 2
    median = (sorted_scores[mid1] + sorted_scores[mid2]) / 2
    print(f"\nMedian (Q2) - Even count:")
    print(f"  Average of positions {mid1 + 1} and {mid2 + 1}")
    print(f"  Values: {sorted_scores[mid1]} and {sorted_scores[mid2]}")
    print(f"  Median = ({sorted_scores[mid1]} + {sorted_scores[mid2]}) / 2 = {median}")

# Step 5: Calculate Q1 (First Quartile)
# Q1 is the median of the lower half (excluding the overall median if n is odd)
lower_half = sorted_scores[:n // 2]
if len(lower_half) % 2 == 1:
    q1 = lower_half[len(lower_half) // 2]
else:
    mid = len(lower_half) // 2
    q1 = (lower_half[mid - 1] + lower_half[mid]) / 2
print(f"\nQ1 (First Quartile - 25th percentile):")
print(f"  Lower half: {lower_half}")
print(f"  Q1 = {q1}")

# Step 6: Calculate Q3 (Third Quartile)
# Q3 is the median of the upper half (excluding the overall median if n is odd)
upper_half = sorted_scores[(n + 1) // 2:] if n % 2 == 1 else sorted_scores[n // 2:]
if len(upper_half) % 2 == 1:
    q3 = upper_half[len(upper_half) // 2]
else:
    mid = len(upper_half) // 2
    q3 = (upper_half[mid - 1] + upper_half[mid]) / 2
print(f"\nQ3 (Third Quartile - 75th percentile):")
print(f"  Upper half: {upper_half}")
print(f"  Q3 = {q3}")

# Step 7: Calculate IQR (Interquartile Range)
# IQR = Q3 - Q1 (represents the middle 50% of data)
iqr = q3 - q1
print(f"\nIQR (Interquartile Range) = Q3 - Q1")
print(f"  IQR = {q3} - {q1} = {iqr}")
print(f"  → This means 50% of data falls within {iqr} units")

# Step 8: Calculate outlier boundaries
# Values beyond these boundaries are considered outliers
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr
print(f"\nOutlier Detection:")
print(f"  Lower fence = Q1 - 1.5 × IQR = {q1} - 1.5 × {iqr} = {lower_fence}")
print(f"  Upper fence = Q3 + 1.5 × IQR = {q3} + 1.5 × {iqr} = {upper_fence}")

# Step 9: Identify outliers
outliers = [x for x in scores if x < lower_fence or x > upper_fence]
print(f"  Outliers: {outliers if outliers else 'None'}")

# Step 10: Box-plot whisker minimum and maximum (Tukey definition)
# ---------------------------------------------------------------
# IMPORTANT:
# - Data minimum  = smallest value in the array
# - Data maximum  = largest value in the array
# - Box-plot min  = smallest value that is >= lower_fence
# - Box-plot max  = largest value that is <= upper_fence
#   (Values outside fences are plotted as outliers, not whiskers.)

inlier_values = [x for x in sorted_scores if lower_fence <= x <= upper_fence]
if inlier_values:
    boxplot_min = inlier_values[0]
    boxplot_max = inlier_values[-1]
else:
    # Fallback: if everything is an outlier (very rare),
    # use data min/max so code does not crash.
    boxplot_min = minimum
    boxplot_max = maximum

print("\nBox-plot whisker values (Tukey definition):")
print(f"  Data minimum (array min):        {minimum}")
print(f"  Data maximum (array max):        {maximum}")
print(f"  Box-plot minimum (lower whisker): {boxplot_min}")
print(f"  Box-plot maximum (upper whisker): {boxplot_max}")

# Summary
print("\n" + "=" * 60)
print("SUMMARY - Five Number Summary:")
print("=" * 60)
print(f"Minimum:  {minimum}")
print(f"Q1:       {q1}  (25% of data is below this)")
print(f"Median:   {median}  (50% of data is below this)")
print(f"Q3:       {q3}  (75% of data is below this)")
print(f"Maximum:  {maximum}")
print(f"IQR:      {iqr}")


# ============================================
# METHOD 2: Using NumPy (Efficient & Standard)
# ============================================

print("\n\n" + "=" * 60)
print("METHOD 2: USING NUMPY LIBRARY")
print("=" * 60)

import numpy as np

# Calculate all statistics using NumPy
q1_np = np.percentile(scores, 25)  # 25th percentile
median_np = np.percentile(scores, 50)  # 50th percentile
q3_np = np.percentile(scores, 75)  # 75th percentile
iqr_np = q3_np - q1_np

print(f"\nNumPy calculations:")
print(f"  Min:    {np.min(scores)}")
print(f"  Q1:     {q1_np}")
print(f"  Median: {median_np}")
print(f"  Q3:     {q3_np}")
print(f"  Max:    {np.max(scores)}")
print(f"  IQR:    {iqr_np}")

# Using NumPy results to compute fences and whisker ends (box-plot min/max)
lower_fence_np = q1_np - 1.5 * iqr_np
upper_fence_np = q3_np + 1.5 * iqr_np

# Values that are inside the fences (NumPy-based inliers)
inlier_values_np = sorted(x for x in scores if lower_fence_np <= x <= upper_fence_np)
if inlier_values_np:
    boxplot_min_np = inlier_values_np[0]
    boxplot_max_np = inlier_values_np[-1]
else:
    boxplot_min_np = np.min(scores)
    boxplot_max_np = np.max(scores)

print("\nNumPy-based box-plot whisker values:")
print(f"  Data minimum (array min):        {np.min(scores)}")
print(f"  Data maximum (array max):        {np.max(scores)}")
print(f"  Lower fence (NumPy):             {lower_fence_np}")
print(f"  Upper fence (NumPy):             {upper_fence_np}")
print(f"  Box-plot minimum (lower whisker): {boxplot_min_np}")
print(f"  Box-plot maximum (upper whisker): {boxplot_max_np}")


# ============================================
# METHOD 3: Creating Visual Box Plot with Matplotlib
# ============================================

print("\n\n" + "=" * 60)
print("METHOD 3: CREATING VISUAL BOX PLOT")
print("=" * 60)

import matplotlib.pyplot as plt

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: Basic box plot
bp1 = ax1.boxplot(scores, 
                   vert=True,  # Vertical orientation
                   patch_artist=True,  # Fill with color
                   showmeans=True,  # Show mean as well
                   meanline=True)  # Mean as a line

# Customize colors
bp1['boxes'][0].set_facecolor('lightblue')
bp1['boxes'][0].set_edgecolor('blue')
bp1['medians'][0].set_color('red')
bp1['medians'][0].set_linewidth(2)
bp1['means'][0].set_color('green')
bp1['means'][0].set_linewidth(2)

ax1.set_ylabel('Score Values', fontsize=12)
ax1.set_title('Box Plot of Scores\n(Basic)', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)

# Add text annotations showing the five-number summary
ax1.text(1.15, minimum, f'Min: {minimum}', fontsize=10, va='center')
ax1.text(1.15, q1_np, f'Q1: {q1_np}', fontsize=10, va='center', color='blue')
ax1.text(1.15, median_np, f'Median: {median_np}', fontsize=10, va='center', color='red')
ax1.text(1.15, q3_np, f'Q3: {q3_np}', fontsize=10, va='center', color='blue')
ax1.text(1.15, maximum, f'Max: {maximum}', fontsize=10, va='center')

# Subplot 2: Horizontal box plot with all data points shown
bp2 = ax2.boxplot(scores, 
                   vert=False,  # Horizontal orientation
                   patch_artist=True,
                   showfliers=True,  # Show outliers
                   showmeans=True)

bp2['boxes'][0].set_facecolor('lightgreen')
bp2['boxes'][0].set_edgecolor('darkgreen')
bp2['medians'][0].set_color('red')
bp2['medians'][0].set_linewidth(2)

# Overlay actual data points
ax2.scatter(scores, [1] * len(scores), color='orange', s=100, 
            zorder=3, alpha=0.6, label='Actual data points')

ax2.set_xlabel('Score Values', fontsize=12)
ax2.set_title('Box Plot of Scores\n(Horizontal with Data Points)', 
              fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()
plt.savefig('/workspaces/FPTCranes/day5/boxplot_scores.png', dpi=150, bbox_inches='tight')
print("\n✓ Box plot saved as 'boxplot_scores.png'")
plt.show()

# ============================================
# HOW TO INTERPRET A BOX PLOT
# ============================================

print("\n\n" + "=" * 60)
print("HOW TO INTERPRET A BOX PLOT")
print("=" * 60)

print("""
1. CENTER (Central Tendency):
   - The median (red line) shows the center of the data
   - If median is closer to Q1: data is right-skewed (has high outliers)
   - If median is closer to Q3: data is left-skewed (has low outliers)
   - If median is in middle of box: data is roughly symmetric

2. SPREAD (Variability):
   - IQR (box height/width) shows spread of middle 50% of data
   - Larger IQR = more variability
   - Whisker length shows overall range

3. SKEWNESS:
   - Symmetric: median in center, whiskers equal length
   - Right-skewed: median closer to Q1, upper whisker longer
   - Left-skewed: median closer to Q3, lower whisker longer

4. OUTLIERS:
   - Points outside whiskers (marked with circles/dots)
   - Any value < Q1 - 1.5×IQR or > Q3 + 1.5×IQR

YOUR DATA INTERPRETATION:
""")

# Analyze the data
if median < (q1_np + q3_np) / 2:
    skew = "slightly left-skewed"
elif median > (q1_np + q3_np) / 2:
    skew = "slightly right-skewed"
else:
    skew = "symmetric"

print(f"- Center: Median = {median}")
print(f"- Spread: IQR = {iqr_np} (50% of data spans {iqr_np} units)")
print(f"- Shape: The data appears {skew}")
print(f"- Range: Data spans from {minimum} to {maximum} ({maximum - minimum} units)")
if outliers:
    print(f"- Outliers: {len(outliers)} outlier(s) detected: {outliers}")
else:
    print(f"- Outliers: No outliers detected")

print("\n" + "=" * 60)
print("COMPLETE! You now understand box plots.")
print("=" * 60)


# ============================================
# EXTRA NOTES: METHOD 1 vs METHOD 2 + FORMULAS
# ============================================

print("\n" + "=" * 60)
print("EXTRA NOTES: MANUAL vs NUMPY")
print("=" * 60)

print("""
WHY METHOD 1 (MANUAL) AND METHOD 2 (NUMPY) CAN DIFFER
----------------------------------------------------

There are several VALID definitions of quartiles (Q1, Q2, Q3). For small samples,
different definitions give slightly different numbers.

In this file we use two common approaches:

1) METHOD 1 (Manual, "median of halves")
    - Sort the data.
    - Q2 (median): middle value (or mean of two middle values if n is even).
    - Lower half = all values below the median.
    - Upper half = all values above the median.
    - Q1 = median of lower half.
    - Q3 = median of upper half.

2) METHOD 2 (NumPy, percentile-based)
    - Uses np.percentile(..., 25), np.percentile(..., 50), np.percentile(..., 75).
    - Concept: find the "25th percent", "50th percent", "75th percent" positions
      on a number line between data points.
    - NumPy uses an interpolation method for percentiles, so Q1 and Q3 can fall
      BETWEEN two data points (not necessarily exactly one of the values).

RESULT:
 - Q1_manual and Q1_numpy can differ slightly.
 - Q3_manual and Q3_numpy can differ slightly.
 - Therefore IQR and fences may also differ slightly.
 - This is NORMAL: both methods are mathematically correct, just defined differently.

In your specific example, both methods still agree on:
 - General center (median around 7.5)
 - Shape of distribution
 - Which points are outliers (if any)
 - Box-plot whisker ends, because they are chosen from ACTUAL data values.
""")

print("\n" + "=" * 60)
print("FORMULA RECAP (BOX PLOT)")
print("=" * 60)

print("""
Given sorted data x1 <= x2 <= ... <= xn:

1) MEDIAN (Q2):
    - If n is odd:  Q2 = middle value.
    - If n is even: Q2 = (x_{n/2} + x_{n/2 + 1}) / 2.

2) Q1 and Q3 (one common manual way):
    - Q1 = median of the lower half (values below Q2).
    - Q3 = median of the upper half (values above Q2).

3) INTERQUARTILE RANGE (IQR):
    IQR = Q3 - Q1

4) OUTLIER FENCES (Tukey):
    Lower fence = Q1 - 1.5 × IQR
    Upper fence = Q3 + 1.5 × IQR

5) BOX-PLOT WHISKERS:
    - Box-plot minimum (lower whisker) = smallest value >= Lower fence.
    - Box-plot maximum (upper whisker) = largest value <= Upper fence.
    - Any value < Lower fence or > Upper fence is plotted as an outlier point.

REMEMBER:
 - "Array min/max" are just the smallest/largest raw data values.
 - "Box-plot min/max" are the ends of the whiskers, based on fences.
 - Several quartile definitions exist; always check which one your software uses.
""")
