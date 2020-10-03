# Classification  Comparison

# Importing the libraries
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


def main():
    # Importing the dataset
    dataset = pd.read_csv('Social_Network_Ads.csv')

    # Convert gender into numeric
    labelEncoder_gender = LabelEncoder()
    dataset.iloc[:, 1] = labelEncoder_gender.fit_transform(dataset.iloc[:, 1])

    # creating dependent and independent variables
    X = dataset.iloc[:, 1:4].values
    y = dataset.iloc[:, 4].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    #### Fitting different classifiers to the Training set ###
    ###########################################################

    classifiers = {
        "Decision Tree": DecisionTreeClassifier(criterion='entropy', random_state=0),
        "K Nearest Neighbors": KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2),
        "Kernel SVM": SVC(kernel='rbf', random_state=0),
        "Logistic Regression": LogisticRegression(random_state=0, solver='lbfgs'),
        "Naive Bayes": GaussianNB(),
        "Random Forest": RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0),
        "Support Vector Machine": SVC(kernel='linear', random_state=0)
    }

    adict = {}

    # Fitting classifiers to the Training set
    for key in classifiers:
        classifiers[key].fit(X_train, y_train)
        # Predicting the Test set results
        y_pred = classifiers[key].predict(X_test)
        # Making the Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        TP = cm[1, 1]
        TN = cm[0, 0]
        FP = cm[0, 1]
        FN = cm[1, 0]
        accuracy = accuracy_score(y_test, y_pred)
        error = 1 - accuracy
        Sensitivity = recall_score(y_test, y_pred)
        Specificity = TN / (TN + FP)
        False_Positive_Rate = 1 - Specificity
        Precision = precision_score(y_test, y_pred)
        adict[key] = [accuracy, round(Precision, 3), round(Sensitivity, 3), round(Specificity, 3), round(error, 4),
                      round(False_Positive_Rate, 3)]

    print(pd.DataFrame.from_dict(adict, orient='index',
                                 columns=['Accuracy', 'Precision', 'Sensitivity', 'Specificity', 'Error',
                                          'False_Positive_Rate']))


if __name__ == '__main__':
    main()
