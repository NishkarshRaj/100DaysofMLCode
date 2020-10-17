# Naive Bayes

Naive Bayes is a supervised Machine Learning technique, which is used for classification, most commonly for the purpose of text classification. The classification is made based on a probabilistic approach, which means that it uses probabilities to make predictions. Typical use cases would be e.g. to classsify emails as spam or not based on the text content, classify good or bad reviews, etc. 


## The Naive Bayes Rule
Naive Bayes defines a prior probability and a posterior probability. The posterior probability can be inferred by a test event, here the sensibility and the specificity are introduced. Usually, this is explained by a medical example as calculating the probabilty of having cancer vs. not having cancer after a positive test. However, let's try to describe the function along with a more practical example: How to find out if your email is spam or not based on a certain word.

The situation is:

- the prior probability of receiving spam is 30%
```
P(S) = 30%
```

- the prior probability of not receiving spam is 70%
```
P(nS) = 70%
```

- looking at the word "bitcoin", the probability that it appears in spam mails is 90%, i.e. the *sensitivity* is 90%
```
P(bit|S) = 90%
```

- but there are 10% of spam mails without this word (in medical terms also *false-negative* rate)
```
P(nbit|S) = 10%
```

- usually, in normal emails the word "bitcoin" does not appear, the probability that it appears in normal emails is 5% (*false-positive* in med terms)
```
P(bit|nS) = 5%
```

-  hence 95% of normal emails are free of the word "bitcoin" (also called the *specificity*)
```
P(nbit|nS) = 95%
```

And now the question is: If you receive an email with the word "bitcoin" in it, what is the probability that this is a spam email?
```
P(S|bit) = ?
```

To solve this, add the probability getting a "bitcoin" mention in spam mails and the probability of getting a "bitcoin" mention in normal mails:

```
P(S) * P(bit|S) = 30% * 90% = 0,27
P(nS) * P(bit|nS) = 70% * 5% = 0,035
```

The next step is to normalize, i.e. to compute the sum of both to have a summed probability of getting the word "bitcoin":
```
P(bit) = 0,27 + 0,035 = 0,305
```

Now the posterior probability can be computed:

```
P(S|bit) = 0,27 / 0,305 = 0,89 = 89%
P(nS|bit) = 0,035 / 0,305 = 0,11 = 11%
```

Et voila: We have a probability of 89% that the email you received which contains the word "bitcoin" is actually spam, hence your algorithm would classify this email most likely as spam. However, usually we do not know the exact prior probabilities. This is why our agorithms learn and update their calculations with every new email.


## Coding with Naive Bayes in Python

Import and create the classifier from [sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html). Then fit the model with the datasets for training data and labels.

```
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(data_train, labels_train)
```

Based on this, you can use the model to make predictions:

```
print(clf.predict(data_test))
```

You may also compute the accuracy of your model:

```
print(clf.score(data_test, labels_test))
```


## Resources

[An Intuitive (and Short) Explanation of Bayes' Theorem](https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/)
[Unfolding Naive Bayes from Scratch](https://towardsdatascience.com/unfolding-na%C3%AFve-bayes-from-scratch-2e86dcae4b01)
[Udacity Intro to ML Course](https://classroom.udacity.com/courses/ud120/lessons/2254358555/concepts/30127485730923)
[Sklearn Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html)
