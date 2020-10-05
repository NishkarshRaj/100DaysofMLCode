""" Random Selection
"""

# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
import random


def main():
    # Importing the dataset
    dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

    # Implementing Random Selection
    N = 10000
    d = 10
    ads_selected = []
    total_reward = 0
    for n in range(0, N):
        ad = random.randrange(d)
        ads_selected.append(ad)
        reward = dataset.values[n, ad]
        total_reward = total_reward + reward

    # Visualising the results
    plt.hist(ads_selected)
    plt.title('Histogram of ads selections')
    plt.xlabel('Ads')
    plt.ylabel('Number of times each ad was selected')
    plt.show()


if __name__ == '__main__':
    main()
