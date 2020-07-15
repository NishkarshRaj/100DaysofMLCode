# Eclat

Eclat algorithm can be used to **mine itemsets that occur frequently** i.e to identify sets of products that are frequently 
bought together. The alogrithm uses simple intersection operations for equivalence class clustering with bottom-up lattice traversal.

>aims at finding regularities in the shopping behavior of supermarket and online store customers. 


# Data Preprocessing


# install.packages('arules')

```sh

$ library(arules)

$ dataset = read.csv('Market_Basket_Optimisation.csv')

$ dataset = read.transactions('Market_Basket_Optimisation.csv', sep = ',', rm.duplicates = TRUE)

$ summary(dataset)

$ itemFrequencyPlot(dataset, topN = 10)

```


# Training Eclat on the dataset

```sh

rules = eclat(data = dataset, parameter = list(support = 0.003, minlen = 2))

```

# Visualising the results

```sh

inspect(sort(rules, by = 'support')[1:10])

```
