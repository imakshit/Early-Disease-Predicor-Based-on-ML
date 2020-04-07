# Heart Attack Prediction Data Analysis


**About Dataset**

The _dataset_ consists of 303 individuals data. There are 14 columns in the dataset, which are described below.

1. Age: displays the age of the individual.
2. Sex: displays the gender of the individual using the following format : 1 = male 0 = female
3. Chest-pain type: displays the type of chest-pain experienced by the individual using the following format : 

1 = typical angina

2 = atypical angina

3 = non — anginal pain 

4 = asymptotic

4. Resting Blood Pressure: displays the resting blood pressure value of an individual in mmHg (unit)
5. Serum Cholestrol: displays the serum cholesterol in mg/dl (unit)
6. Fasting Blood Sugar: compares the fasting blood sugar value of an individual with 120mg/dl. If fasting blood sugar > 120mg/dl then : 1 (true) else : 0 (false)
7. Resting ECG : displays resting electrocardiographic results 0 = normal 1 = having ST-T wave abnormality 2 = left ventricular hyperthrophy
8. Max heart rate achieved : displays the max heart rate achieved by an individual.
9. Exercise induced angina : 1 = yes 0 = no ST depression induced by exercise relative to rest: displays the value which is an integer or float.
10. Peak exercise ST segment : 1 = upsloping 2 = flat 3 = downsloping Number of major vessels (0–3) colored by flourosopy : displays the value as integer or float.
11. Thal : displays the thalassemia : 3 = normal 6 = fixed defect 7 = reversible defect
12. Diagnosis of heart disease : Displays whether the individual is suffering from heart disease or not : 0 = absence 1, 2, 3, 4 = present.


**DATA VISUALIZATION**

1. _variation of age_ : 


![Image of age_variation](https://camo.githubusercontent.com/86cff8647cfc2d54ad15d118f79ce1517f446e3e/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f6d61782f313633322f312a6a325971715362306737556a7970584a766d33397a772e706e67)



**analysis** - We see that most people who are suffering are of the age of 58, followed by 57. Majorly, people belonging to the age group 50+ are suffering from the disease.


**MODELS**
1. SVM :

Accuracy for training set for svm = 0.91701244813278

Accuracy for test set for svm = 0.8360655737704918


2. NAIVE BAYES :

Accuracy for training set for Naive Bayes = 0.8547717842323651

Accuracy for test set for Naive Bayes = 0.8524590163934426


3. LOGISTIC REGRESSION :

Accuracy for training set for Logistic Regression = 0.8547717842323651

Accuracy for test set for Logistic Regression = 0.8852459016393442


4. DECISION TREE :

Accuracy for training set for Decision Tree = 1.0

Accuracy for test set for Decision Tree = 0.7213114754098361


5. RANDOM FOREST :

Accuracy for training set for Random Forest = 0.991701244813278

Accuracy for test set for Random Forest = 0.8032786885245902


6. LIGHT GBM :

Accuracy for training set for LightGBM = 0.983402489626556

Accuracy for test set for LightGBM = 0.8688524590163934


7. XGBOOST :

Accuracy for training set for XGBoost = 0.970954356846473

Accuracy for test set for XGBoost = 0.8524590163934426


# CONCLUSION

Heart Disease is one of the major concerns for society today. It is difficult to manually determine the odds of getting heart disease based on risk factors. However, machine learning techniques are useful to predict the output from existing data.

From the above analysis, we observe that - Logistic Regression is the best model as all other models give a high accuracy on training dataset but on test dataset the accuracy is less, also known as overfitting




