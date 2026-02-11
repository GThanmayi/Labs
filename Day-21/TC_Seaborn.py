import seaborn as sns
import matplotlib.pyplot as plt
marks=[50,60,40,89,89]

sns.set_style("whitegrid")
sns.histplot(marks,bins=5)
plt.title("Marks")
plt.show()