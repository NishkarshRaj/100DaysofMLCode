## Data Pre-processing

Data pre-processing is the pre-requisite to successful running of machine learning algorithms.

## Download Data sets

Link to [data set](https://www.superdatascience.com/pages/machine-learning).

**Note: Data sets are generally .csv files (Comma separated files).** 
Generally, .csv files first row consists of variables (attributes).
There are two types of attributes:

**1. Independent variables**
**2. Dependent variables**

We are presented with data values for independent variables and using our Machine learning algorithms, we have to predict the dependent variables.

## Importing Libraries
Libraries consists of pre-built functions that take user input and give desired output.

## 1. Importing Libraries in Python

Three essential libraries:

**1. numpy:** For mathematical functions
**2. matplotlib.pyplot:** Creating charts for visualization
**3. pandas:** to import and manage data sets

**How to import library in python**
```python
import libary as alias;
```

## 2. Importing Libraries in R

Can be imported via GUI package explorer in RStudio. Generally all basic libraries we need are automatically imported.

## Importing Datasets

## 1. Importing Data sets in Python using Pandas library

```python
dataset = pd.read_csv('filename.csv') #pd is the alias set for pandas libarary
```

**Note: For imported CSV Files**
1. They can be accessed directly by Spyder IDE using the **variable explorer**
2. Python assigns **index** or row number to each row. Index starts from 0
3. Null values are defined by **NaN** keyword
4. By default, numbers are in scientific notation (%0.3g) but can be changed to float (%0.f).

**Creating Matrix of Independent variables and dependent variables**
```python
variable_name = dataset.iloc[x:y, a:b].values
```

Here, first input x:y is for rows and second input a:b is for columns where y and b are exclusive.

## 2. Importing Data sets in R Programming

1. Go to package explorer -> browse data set location -> More -> set as working directory
2. Write a code

```R
variablename = read.csv('filename.csv')
```

**Note: In R programming, data sets are index from 1 and not 0**

## Handling Veracity in Data Sets

The biggest issues in Data sets for machine learning algorithms is that they may have **incompleteness**, many cells of data might be missing, left out, unknown etc.
This makes it difficult to program because it decreases the **accuracy** of our algorithms.

**Note: We cannot delete the entire tuple of data to remove inconsistency because the data might be valuable.**
Here, we assume that the missing data is only of numeric form (float or integer) and we replace all missing values of the **column/variable** with the mean of the values of column.

## 1. Missing Data Management in Python



