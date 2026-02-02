import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "Math": np.random.randint(60, 100, 50),
        "Physics": np.random.randint(55, 95, 50),
        "Chemistry": np.random.randint(65, 100, 50),
    }
)

corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Heatmap of Subject Correlations")
plt.savefig("heatmap_subject_correlations.png")
