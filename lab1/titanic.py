# Dependencies

import inline as inline
import matplotlib
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt

# Load the train and test data sets to create two DataFrames

train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train = pd.read_csv(train_url)
test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test = pd.read_csv(test_url)

# Print a part of the data set
print("***** Train_Set *****")
print(train.head())
print("\n")
print("***** Test_Set *****")
print(test.head())

# Get some initial statistics of both the train and test DataFrames
print("***** Train_Set *****")
print(train.describe())
print("\n")
print("***** Test_Set *****")
print(test.describe())

# List of the feature names
print(train.columns.values)

# See the missing data for the train set
train.isna().head()

# See the missing data for the test set
test.isna().head()

# Total number of missing values in both data sets
print("*****In the train set*****")
print(train.isna().sum())
print("\n")
print("*****In the test set*****")
print(test.isna().sum())

# Fill missing values with mean column values in the train set
train.fillna(train.mean(), inplace=True)

# Fill missing values with mean column values in the test set
test.fillna(test.mean(), inplace=True)

# See if the data set still has any missing values for the training set
print(train.isna().sum())

# See if the data set still has any missing values for the test set
print(test.isna().sum())

# Sample values
print('Print ticket sample')
print(train['Ticket'].head())

print('Print cabin sample')
print(train['Cabin'].head())

# Survival count with respect to Pclass
print(train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False))

# Survival count with respect to Sex
print(train[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False))

# Survival count with respect to SibSp
print(train[["SibSp", "Survived"]].groupby(['SibSp'], as_index=False).mean().sort_values(by='Survived', ascending=False))

# Plot the graph of "Age vs. Survived"
g = sns.FacetGrid(train, col='Survived')
g.map(plt.hist, 'Age', bins=20)
