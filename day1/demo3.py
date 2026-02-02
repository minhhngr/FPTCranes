import matplotlib.pyplot as plt

# scatter plot

x = [1,2,3,4,5]
y = [2,4,1,3,7]

plt.scatter(x, y, color='red', marker='o')
plt.title("Simple Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.savefig("simple_scatter_plot.png")
# Phù hợp data dạng số liên tục (Chiều cao vs cân nặng, điểm thi vs thời gian học)
# Xét quan hệ giữa 2 biến số liên tục