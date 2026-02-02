import seaborn as sns
import matplotlib.pyplot as plt

scores = [88, 92, 79, 93, 85, 91, 87, 95, 90, 89, 95]
sns.boxplot(y=scores)

plt.title('Box Plot of Scores')
plt.ylabel('Scores')
plt.savefig('box_plot_scores.png')
