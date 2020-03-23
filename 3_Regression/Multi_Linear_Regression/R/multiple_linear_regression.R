# Multiple Linear Regression

# Importing the dataset
dataset = read.csv('50_Startups.csv')

# Encoding categorical data
dataset$State = factor(dataset$State,
                       levels = c('New York', 'California', 'Florida'),
                       labels = c(1, 2, 3))

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

# Fitting Multiple Linear Regression to the Training set
regressor = lm(formula = Profit ~ .,
               data = training_set)

# Predicting the Test set results
y_pred = predict(regressor, newdata = test_set)

# Building the optimal model using Backward Elimination
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
               data = dataset)
summary(regressor)
# Optional Step: Remove State2 only (as opposed to removing State directly)
# regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + factor(State, exclude = 2),
#                data = dataset)
# summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
               data = dataset)
summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend + Marketing.Spend,
               data = dataset)
summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend,
               data = dataset)
summary(regressor)

# Regression subset selection including exhaustive search
library(leaps)
#Perform all subset regression, and choose “nbest” model(s) for each number of predictors
leaps<-regsubsets(Profit ~ .,data=training_set, nbest=1, method = "exhaustive")

# view results and best model at each variable number
summary(leaps)

# Graphical table of best subsets, models are ordered by the selection statistic
plot(leaps,scale="r2")

# plot statistic by subset size
subsets(leaps, statistic="adjr2", legend = FALSE)

# Mallow Cp is used to decide on the number of predictors to include
subsets(leaps, statistic="cp", legend = FALSE)