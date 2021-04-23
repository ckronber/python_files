import pandas as pd
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import seaborn as sns

gradebook = pd.read_csv("gradebook.csv")
print(gradebook)
assignment1 = gradebook[gradebook.assignment_name == "Assignment 1"]
print(assignment1)

asn1_median = np.median(assignment1.grade)
print('Median grade = {}'.format(asn1_median))

gradebook = pd.read_csv("gradebook.csv")

sns.barplot(data=gradebook, x="assignment_name", y="grade")

plt.show()
