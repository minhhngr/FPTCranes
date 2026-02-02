import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

scores = [45, 78, 88, 56, 90, 67, 72, 85, 94, 81]
sns.histplot(scores, bins=5, kde=True, color='skyblue')
plt.title("Histogram of Student Scores")
plt.xlabel("Scores")
plt.ylabel("Number of Students")
plt.savefig("histogram_student_scores.png")