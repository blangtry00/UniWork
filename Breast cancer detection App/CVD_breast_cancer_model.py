import sklearn
import matplotlib.pyplot as pyplot
import pandas as pd
from sklearn import preprocessing
# Load libraries
from matplotlib import pyplot as plt
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('breast-cancer.csv')
print(df.head)

le = preprocessing.LabelEncoder()
id =le.fit_transform(list(df['id']))
diagnosis = le.fit_transform(list(df['diagnosis']))
radius_m = le.fit_transform(list(df['radius_mean']))
texture_m =le.fit_transform(list(df['texture_mean']))
perimeter_m = le.fit_transform(list(df['perimeter_mean']))
area_m=le.fit_transform(list(df['area_mean']))
smoothness_m = le.fit_transform(list(df['smoothness_mean']))
compactness_m = le.fit_transform(list(df['compactness_mean']))
concavity_m = le.fit_transform(list(df['concavity_mean']))
concave_m = le.fit_transform(list(df['concave points_mean']))
symmetry_m = le.fit_transform(list(df['symmetry_mean']))
frac_dim_m = le.fit_transform(list(df['fractal_dimension_mean']))

radius_se= le.fit_transform(list(df['radius_se']))
texture_se = le.fit_transform(list(df['texture_se']))
perimeter_se = le.fit_transform(list(df['perimeter_se']))
area_se= le.fit_transform(list(df['area_se']))
smoothness_se = le.fit_transform(list(df['smoothness_se']))
compactness_se= le.fit_transform(list(df['compactness_se']))
concavity_se= le.fit_transform(list(df['concavity_se']))
concave_point_se= le.fit_transform(list(df['concave points_se']))
symmetry_se = le.fit_transform(list(df['symmetry_se']))
frac_dim_se = le.fit_transform(list(df['fractal_dimension_se']))

radius_worst= le.fit_transform(list(df['radius_worst']))
texture_worst = le.fit_transform(list(df['texture_worst']))
perimeter_worst= le.fit_transform(list(df['perimeter_worst']))
area_worst = le.fit_transform(list(df['area_worst']))
smoothness_worst= le.fit_transform(list(df['smoothness_worst']))
compactness_worst= le.fit_transform(list(df['compactness_worst']))
concavity_worst= le.fit_transform(list(df['concavity_worst']))
concave_point_worst= le.fit_transform(list(df['concave points_worst']))
symmetry_worst= le.fit_transform(list(df['symmetry_worst']))
frac_dim_worst= le.fit_transform(list(df['fractal_dimension_worst']))



x = list(zip(radius_m,texture_m,perimeter_m,area_m,smoothness_m,compactness_m,concave_m,concavity_m,symmetry_m,
			 frac_dim_m,radius_se, texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,
			 concave_point_se,symmetry_se,frac_dim_se, radius_worst,texture_worst,perimeter_worst,area_worst,
			 smoothness_worst,compactness_worst,concavity_worst,concave_point_worst,symmetry_worst,frac_dim_worst))
y = list(diagnosis)

seed = 7

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.20, random_state=seed)
#Check with  different Scikit-learn classification algorithms
models = []
models.append(('DT', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
models.append(('GBM', GradientBoostingClassifier()))
models.append(('RF', RandomForestClassifier()))


results = []
names = []
num_folds = 5

scoring = 'accuracy'
# evaluate each model in turn
for name, model in models:
	kfold = KFold(n_splits=num_folds,shuffle=True,random_state=seed)
	cv_results = cross_val_score(model, x_train, y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	msg += '\n'
	print(msg)



# Comparing Algorithms Performance
fig = pyplot.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklabels(names)
pyplot.show()


# Make predictions on validation/test dataset
dt = DecisionTreeClassifier()
nb = GaussianNB()
gb = GradientBoostingClassifier()
rf = RandomForestClassifier()
svc =SVC()

best_model = rf
best_model.fit(x_train, y_train)
y_pred = best_model.predict(x_test)
model_accuracy = accuracy_score(y_test, y_pred)
print("Best Model Accuracy Score on Test Set:", model_accuracy)

# #Model Evaluation Metric 1
print(classification_report(y_test, y_pred))

#Model Evaluation Metric 2
#Confusion matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()

#Model Evaluation Metric 3
#reciever operating characteristic
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

best_model = rf
best_model.fit(x_train, y_train)
rf_roc_auc = roc_auc_score(y_test,best_model.predict(x_test))
fpr,tpr,thresholds = roc_curve(y_test, best_model.predict_proba(x_test)[:,1])

plt.figure()
plt.plot(fpr,tpr,label = 'Random Forest(area = %0.2f)'% rf_roc_auc)
plt.plot([0,1],[0,1],'r--')
plt.xlim([0.0,1.0])
plt.ylim([0.0,1.05])
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc='lower right')
plt.savefig('LOC_ROC')
plt.show()

#Check actual/ground truth vs predicted diagnosis
for x in range(len(y_pred)):
	print("Predicted: ", y_pred[x], "Actual: ", y_test[x], "Data: ", x_test[x],)

#Reference
#Author: Unknown
#Date: Trimester 1 2023
#Title: Program called Heart Disease Predictor Capstone Project
#Version 1
#Source Code
#Template used from https://uclearn.canberra.edu.au/courses/14056/pages/week-10-project-assignment-workshop?module_item_id=1064187
