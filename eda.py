import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the scraped dataset
df = pd.read_csv("books_dataset.csv")
print(df.head())