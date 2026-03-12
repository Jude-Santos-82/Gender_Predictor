from sklearn import tree

#[height (cm), weight (kilos), shoe size]
X = [[181,80,44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 33], [171, 75, 42], [181, 85, 43]]

#gender for each element of lists in previous variable
Y = ['male', 'female',  'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male',]

#stores decision tree classifier
clf = tree.DecisionTreeClassifier()

#trains decision tree on how each variable relates to each other where
#first list of info correlates to a male, second list correlates to a female q
clf = clf.fit(X,Y)

#uses example dataset to predict gender based on info given
prediction = clf.predict([[190, 70, 43]])

print(prediction)
