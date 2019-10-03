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
print('\n Print ticket sample')
print(train['Ticket'].head())

print('\n Print cabin sample')
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
#<sns.axisgrid.FacetGrid at 0x7fa990f87080>

# See how the Pclass and Survived features are related to eachother with a graph
grid = sns.FacetGrid(train, col='Survived', row='Pclass', height=2.2, aspect=1.6)
grid.map(plt.hist, 'Age', alpha=.5, bins=20)
grid.add_legend();

plt.show()

# Data types of different features that you have
print('\n Train info:')
train.info()

# Drop values with no impact
train = train.drop(['Name','Ticket', 'Cabin','Embarked'], axis=1)
test = test.drop(['Name','Ticket', 'Cabin','Embarked'], axis=1)

# Convert "sex" feature to a numerical one
labelEncoder = LabelEncoder()
labelEncoder.fit(train['Sex'])
labelEncoder.fit(test['Sex'])
train['Sex'] = labelEncoder.transform(train['Sex'])
test['Sex'] = labelEncoder.transform(test['Sex'])

# Let's investigate if you have non-numeric data left
print('\n Updated train with non-numeric data left:')
train.info()

# Let's investigate if you have non-numeric data left
print('\n Updated test with non-numeric data left:')
test.info()

# Drop the survival column from the data with drop() function
X = np.array(train.drop(['Survived'], 1).astype(float))
y = np.array(train['Survived'])

# View all features we are going to feed to the algorithm with train.info()
print('\n HÄR VISAR DEN 8 KOLUMNER')
train.info() # Den visar 8 columner men den borde visa 7

# Building K-Means model
kmeans = KMeans(n_clusters=2) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(X)

KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
    n_clusters=2, n_init=10, n_jobs=1, precompute_distances='auto',
    random_state=None, tol=0.0001, verbose=0)

correct = 0
for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = kmeans.predict(predict_me)
    if prediction[0] == y[i]:
        correct += 1

print('Accurency of our model:')
print(correct/len(X)) # får inte samma värde som de får

# Tweaked values of the parameters above
kmeans = kmeans = KMeans(n_clusters=2, max_iter=600, algorithm = 'auto')
kmeans.fit(X)

KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=600,
    n_clusters=2, n_init=10, n_jobs=1, precompute_distances='auto',
    random_state=None, tol=0.0001, verbose=0)

correct = 0
for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = kmeans.predict(predict_me)
    if prediction[0] == y[i]:
        correct += 1

print('Tweaked value accurency of our model:')
print(correct/len(X)) # Blir olika värden varje gång

# Take 0-1 as the uniform value range across all the features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

kmeans.fit(X_scaled)

KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=600,
    n_clusters=2, n_init=10, n_jobs=1, precompute_distances='auto',
    random_state=None, tol=0.0001, verbose=0)

correct = 0
for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = kmeans.predict(predict_me)
    if prediction[0] == y[i]:
        correct += 1

print('12% increase in the score')
print(correct/len(X))



