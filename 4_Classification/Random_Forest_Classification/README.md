
## Random Forest Classification

  

Random Forest is a learning algorithm that is suitable for both Regression as well as Classification. Like a forest is comprised of trees, random forest contains various decision trees on a randomly selected data samples. It then retrieves predictions from each tree and obtains the best prediction by voting.

**What is Random Forest Classification?**
In layman's terms, when we make decisions, we try to search some information regarding the decision. Let's say for buying a television, we search the internet, ask our friends regarding the latest models or visit stores and seek their advice regarding the topic. 
Now we try to finalize all their advices and make a list of all the recommended televisions. This is the first part of Random Forest Algorithm.
Later, we create a voting mechanism in which we ask all the above advisors to vote the recommended television from the list we created earlier. This is the second part of Random Forest Algorithm. This is called ensembling.

**How does it work?**
Random Forest Classification works with the help of following steps:

- Select Random samples from the dataset
- Construct a decision tree for each sample and get prediction result from each tree
- Perform vote for the predictions
- Select the most voted prediction as the final result 

**Example**
In the given Dataset, the CSV contains certain columns as features which are *UserID*,*Gender*, *Age*, *Estimated Salary* and the outcome is categorical column, *Purchased*.
The dataset is split into Train and Test sets in the ratio of 0.75:0.25 using the CrossValidation module and normalized accordingly using ScikitLearn StandardScalar module.
A Random Forest Classifier is then generated with N = 10 trees and using *entropy* as the quality measure of the splits. 
The classifier is then fit to the Training dataset and predictions are then made on the Test dataset.


