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

```python
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[a:b, x:y])
X[a:b, x:y] = imputer.transform(X[a:b, x:y])
```

* Line 1: Configure Scikit Pre-processor Library and import its Imputer function
* Line 2: Create an object **imputer** of Imputer Class and pass three parameters to parameterized constructor.
  1. missing_values = 'NaN' -> Tells to work upon Null values
  2. strategy -> Tells what to replace the null values with. It can be mean, median, etc.
  3. axis -> Tells to work on rows (1) or columns (0)
* Line 3: Fit the imputer object on the matrix it has to work upon. This matrix must contain only those rows or columns that contain NaN keyword. 
**Remember: b and y are exclusive**
* Line 4: Transform the Data matrix and store it in the data matrix.

## 2. Missing Data Management in R

```R
dataset$column = ifelse(is.na(dataset$column),
                     ave(dataset$column, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$column)
```

* Logic: Scan entire row, if the data is missing, replace with average else replace with old content.
* To access all element column wise: PointerToDataSet$column
* ifelse: Three parameters -> Condition, If True, If false

## Encoding Categorical Data

Categorical variables are those which take only particular set of values as input.
For example: Variable taking values in form of only Yes/No.

For sake of ease in programming, we want to use equations in our algorithm in only Numeric form. 
So, there is a need to encode categorical data into numerical form.

**Problem** There is problem for encoding strings into number for **Independent** variables.
On encoding, the first value type is assigned 0, next is assigned as 1 and so on but the machine on execution might think that these data sets are related and 1>0 and so on.

This problem is solved by using the concept of **Dummy variables** after encoding has been done.

Suppose we choose a variable **purchased** with values **Yes/No** where Yes is encoded as 1 and No is encoded as 0
Then, purchased variable is broken into two variables Yes and No which contain values that are not related to each other.

If the values is Yes, 1 is assigned in Yes column and 0 is assigned in No and vice-versa.

## 1. Encoding Categorical Data in Python

```python
# Encode 1 variable at a time
# Encoding independent variable -> Encode then convert to Dummy variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0]) # All rows and column number 0
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
# Encode dependent variable -> only encode
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
```

## 2. Encoding Categorical Data in R Programming

Here, we use Factor function which automatically creates different factors for each value type in independent categorical variables thus there is no need to create dummy variables using OneHotEncoder.

```R
# Encoding categorical data
dataset$columnname = factor(dataset$columnname,
                         levels = c('Value 1', 'Value 2', 'Value 3'),
                         labels = c(1, 2, 3)) # encoded values can be anything
```

## Splitting the Data Set into Train Data and Test Data

**Analogy:** A student learns about some subject and gets a training in it (Train Data) and gives an examination to check his understanding in it (Test data).
**Machine Learning:** A machine learns about a certain domain and gets trained using the test data and its **accuracy** and **performance** (speed) are tested on a similar yet difference test data set.
A good machine learning algorithm in one that performs similarly for both test and train data sets.

Generally if same data set is split into train and test data, we assign small portion to test data, approx 0.5 or less (50 percent or less).

## 1. Splitting Data in Python

```Python
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
```

* **Library:** sklearn.cross_validation
* **Class:** train_test_split
* Create 4 variables -> 2 for test and 2 for train for both dependent and independent variables
* Argument of train_test_split ->
1. All the arrays -> variables matrix
2. test_size (between 0 and 1 exclusive denoting percent of dataset to be assigned)
3. random_state -> to remove randomness and get same split always

## 2. Splitting Data in R Programming

```R
install.packages('caTools') # Install the caTools library
library(caTools) # Include the library in our build path
set.seed(123) # Analogous to Python random_state to remove randomness 
split = sample.split(dataset$DependentVariable, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)
```

**Note:** Different seeds for different users means different result but same seed for same data set for different users will give same result

* split is a programming variable not a pre-built function
* Arguments of sample.split:
1. Dependent variable matrix
2. SplitRatio (for Training set)
**Note:** sample.split function is divided into two parts after SplitRatio is specified, TRUE and FALSE

Assign TRUE values to training_set and test_set, both of which are not keywords and just programming variables.
