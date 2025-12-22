import numpy as np
import matplotlib.pyplot as plt

y2023 = np.array([20, 22, 25, 27, 30, 32, 35, 33, 36, 38, 40, 42])
y2024 = np.array([25, 28, 30, 33, 35, 38, 40, 42, 45, 47, 48, 50])

months = np.arange(1, 13)

# Compare revenue distributions using two box plots
# Analyze the median, IQR, and outliers
# Draw a line chart to compare the trends
# Draw conclusions


# ---------- Solution 1: Pure Python (no NumPy helper functions) ----------


def compute_median_and_iqr_python(data: list[float]) -> tuple[float, float]:
    """Compute median and IQR using only basic Python operations.

    Steps:
    1. Sort the list.
    2. Find the middle value(s) for the median.
    3. Find Q1 and Q3 (25% and 75% positions) manually.
    4. IQR = Q3 - Q1.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)

    # Step 2: median
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        middle1 = sorted_data[n // 2 - 1]
        middle2 = sorted_data[n // 2]
        median = (middle1 + middle2) / 2

    # Step 3: Q1 and Q3 using positions
    q1_index = int(0.25 * (n - 1))
    q3_index = int(0.75 * (n - 1))
    q1 = sorted_data[q1_index]
    q3 = sorted_data[q3_index]
    iqr = q3 - q1
    return float(median), float(iqr)


def run_python_solution() -> None:
    """Handle the requirements using pure Python lists.

    Step 1: Convert NumPy arrays to Python lists.
    Step 2: Compute median and IQR with compute_median_and_iqr_python.
    Step 3: Print month‑by‑month comparison using basic loops.
    Step 4: Print a simple text conclusion.
    """
    # Step 1: convert to pure Python lists
    y2023_list = [float(x) for x in y2023]
    y2024_list = [float(x) for x in y2024]
    months_list = [int(m) for m in months]

    print("Monthly revenue 2023 (Python list):", y2023_list)
    print("Monthly revenue 2024 (Python list):", y2024_list)

    # Step 2: compute statistics with our pure‑Python function
    median_2023, iqr_2023 = compute_median_and_iqr_python(y2023_list)
    median_2024, iqr_2024 = compute_median_and_iqr_python(y2024_list)

    print("\n[Python] --- Summary statistics ---")
    print("Median 2023:", median_2023)
    print("Median 2024:", median_2024)
    print("IQR 2023:", iqr_2023)
    print("IQR 2024:", iqr_2024)

    # Step 3: month‑by‑month comparison with a for loop
    print("\n[Python] --- Month‑by‑month comparison ---")
    for m, v23, v24 in zip(months_list, y2023_list, y2024_list):
        diff = v24 - v23
        print(f"Month {m:2d}: 2023 = {v23}, 2024 = {v24}, difference = {diff}")

    # Step 4: simple text conclusion (still using Python values)
    print("\n[Python] Conclusion:")
    if median_2024 > median_2023:
        print("On average, 2024 has higher monthly revenue than 2023.")
    elif median_2024 < median_2023:
        print("On average, 2023 has higher monthly revenue than 2024.")
    else:
        print("On average, monthly revenue is the same in 2023 and 2024.")

    if iqr_2024 > iqr_2023:
        print("Revenue in 2024 is more variable (larger IQR) than in 2023.")
    elif iqr_2024 < iqr_2023:
        print("Revenue in 2023 is more variable (larger IQR) than in 2024.")
    else:
        print("Revenue variability (IQR) is similar in both years.")


def compute_median_and_iqr(data: np.ndarray) -> tuple[float, float]:
    """Return median and IQR (Q3 - Q1) of a 1D NumPy array."""
    median = float(np.median(data))
    q1 = float(np.percentile(data, 25))
    q3 = float(np.percentile(data, 75))
    iqr = q3 - q1
    return median, iqr


def print_monthly_comparison(
    months_array: np.ndarray,
    y_first: np.ndarray,
    y_second: np.ndarray,
    year_first: int,
    year_second: int,
) -> None:
    """Print month‑by‑month values and differences between two years."""
    print("\n--- Month‑by‑month comparison ---")
    for m, v_first, v_second in zip(months_array, y_first, y_second):
        diff = v_second - v_first
        print(
            f"Month {m:2d}: {year_first} = {v_first}, {year_second} = {v_second}, "
            f"difference = {diff}"
        )


def print_conclusion(
    median_2023: float, median_2024: float, iqr_2023: float, iqr_2024: float
) -> None:
    """Print a short text conclusion based on the statistics."""
    print("\nConclusion:")
    if median_2024 > median_2023:
        print("On average, 2024 has higher monthly revenue than 2023.")
    elif median_2024 < median_2023:
        print("On average, 2023 has higher monthly revenue than 2024.")
    else:
        print("On average, monthly revenue is the same in 2023 and 2024.")

    if iqr_2024 > iqr_2023:
        print("Revenue in 2024 is more variable (larger IQR) than in 2023.")
    elif iqr_2024 < iqr_2023:
        print("Revenue in 2023 is more variable (larger IQR) than in 2024.")
    else:
        print("Revenue variability (IQR) is similar in both years.")


def draw_visualizations() -> None:
    """Create box plots and line chart using matplotlib.

    Step 1: Use y2023 and y2024 to draw a box plot
            → compare revenue distribution for the two years.
    Step 2: Use months, y2023, y2024 to draw a line chart
            → compare revenue trend over months.
    """
    # Step 1: box plot comparison
    plt.figure(figsize=(8, 5))
    plt.boxplot([y2023, y2024], labels=["2023", "2024"])
    plt.title("Revenue Distribution: 2023 vs 2024")
    plt.ylabel("Revenue")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.savefig("revenue_boxplot.png", dpi=300, bbox_inches="tight")
    plt.show()

    # Step 2: line chart comparison
    plt.figure(figsize=(10, 5))
    plt.plot(months, y2023, marker="o", label="2023")
    plt.plot(months, y2024, marker="o", label="2024")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(months)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.savefig("revenue_line_chart.png", dpi=300, bbox_inches="tight")
    plt.show()


def run_numpy_solution() -> None:
    """Handle the requirements using NumPy helper functions.

    Step 1: Use compute_median_and_iqr (NumPy) for statistics.
    Step 2: Use print_monthly_comparison (NumPy arrays + zip).
    Step 3: Use print_conclusion to summarize.
    """
    print("Monthly revenue 2023 (NumPy array):", y2023)
    print("Monthly revenue 2024 (NumPy array):", y2024)

    # Step 1: statistics with NumPy
    median_2023, iqr_2023 = compute_median_and_iqr(y2023)
    median_2024, iqr_2024 = compute_median_and_iqr(y2024)

    print("\n[NumPy] --- Summary statistics ---")
    print("Median 2023:", median_2023)
    print("Median 2024:", median_2024)
    print("IQR 2023:", iqr_2023)
    print("IQR 2024:", iqr_2024)

    # Step 2: month‑by‑month comparison (still using NumPy arrays)
    print_monthly_comparison(months, y2023, y2024, 2023, 2024)

    # Step 3: text conclusion based on NumPy results
    print_conclusion(median_2023, median_2024, iqr_2023, iqr_2024)


if __name__ == "__main__":
    print("=== Solution 1: Pure Python ===")
    run_python_solution()

    print("\n\n=== Solution 2: NumPy ===")
    run_numpy_solution()

    print("\n\n=== Visualization with Matplotlib ===")
    draw_visualizations()
