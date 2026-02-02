import matplotlib.pyplot as plt

scores = [45, 78, 88, 92, 67, 54, 81, 73, 95, 60]

plt.hist(scores, bins=10, edgecolor='black')
plt.title('Histogram Demo')
plt.xlabel('Scores')
plt.ylabel('Freqancy')

# phù hợp: phân bố điểm, tuổi, thu nhập

plt.savefig('histogram_demo.png')