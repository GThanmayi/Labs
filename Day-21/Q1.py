import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

# Create line plot
plt.plot(months, sales, marker='o', linestyle='-', color='blue')

# Add title and labels
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

# Add grid lines
plt.grid(True)

# Show plot
plt.show()

df = pd.DataFrame({"Month": months, "Sales": sales})

sns.set_style("whitegrid")   
sns.barplot(x="Month", y="Sales", data=df, palette="viridis")

# Customize
plt.title("Monthly Sales Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")

# Show plot
plt.show()
#plt.savefig(report2.png)
#plt.show()
