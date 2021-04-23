import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

df = pd.read_csv('NP10_Repeatability.csv')
print(df.info())
print(df.describe())

answer = input("Would  you like to continue the program?")
