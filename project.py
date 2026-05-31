import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv("Zomato-data-.csv")

def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

dataframe['rate'] = dataframe['rate'].apply(handleRate)

print(dataframe.head())
print(dataframe.info())
print(dataframe.isnull().sum())

sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")
plt.show()

grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()

plt.plot(grouped_data.index, grouped_data.values,
         c='green', marker='o')

plt.xlabel('Type of restaurant')
plt.ylabel('Votes')
plt.show()

sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of Restaurant")
plt.show()

grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()

plt.figure(figsize=(8,5))
plt.plot(grouped_data.index,
         grouped_data.values,
         c='green',
         marker='o')

plt.xlabel("Type of Restaurant")
plt.ylabel("Votes")
plt.title("Votes by Restaurant Type")
plt.show()

max_votes = dataframe['votes'].max()

restaurant_with_max_votes = dataframe.loc[
    dataframe['votes'] == max_votes,
    'name'
]

print("Restaurant(s) with maximum votes:")
print(restaurant_with_max_votes)

sns.countplot(x=dataframe['online_order'])
plt.title("Online Order Availability")
plt.show()

plt.hist(dataframe['rate'], bins=5)
plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Restaurants")
plt.show()

couple_data = dataframe['approx_cost(for two people)']

sns.countplot(x=couple_data)
plt.title("Approximate Cost for Two People")
plt.show()

plt.figure(figsize=(6,6))
sns.boxplot(x='online_order', y='rate', data=dataframe)

plt.title("Ratings: Online vs Offline Orders")
plt.show()

pivot_table = dataframe.pivot_table(
    index='listed_in(type)',
    columns='online_order',
    aggfunc='size',
    fill_value=0
)

sns.heatmap(
    pivot_table,
    annot=True,
    cmap='YlGnBu',
    fmt='d'
)

plt.title('Heatmap')
plt.xlabel('Online Order')
plt.ylabel('Restaurant Type')
plt.show()

top10 = dataframe.sort_values(by='votes', ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x='votes', y='name', data=top10)

plt.title("Top 10 Restaurants by Votes")
plt.show()

plt.figure(figsize=(8,5))

plt.hist(dataframe['rate'], bins=5)
plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Restaurants")

plt.savefig("ratings_distribution.png", bbox_inches="tight")
plt.show()
