import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 4]

plt.bar(categories, values, color='skyblue')
plt.title("Simple Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.savefig("simple_bar_chart.png")

# Phù hợp data dạng category (Số lượng sinh viên theo lớp, doanh số theo sp)