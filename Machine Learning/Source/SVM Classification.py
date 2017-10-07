from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import train_test_split
from sklearn import svm

gnb = GaussianNB()

irisdataset=datasets.load_iris()
x=irisdataset.data
y=irisdataset.target

print('x and y shape is: ',x.shape,y.shape)

y_pred = gnb.fit(irisdataset.data, irisdataset.target).predict(irisdataset.data)
print('ypred shape is: ',y_pred.shape)
print("Number of mislabeled points out of a total %d points : %d"
      % (irisdataset.data.shape[0],(irisdataset.target != y_pred).sum()))
a,b = irisdataset.data.shape[0],(irisdataset.target != y_pred).sum()
print('accuracy in Naive Bayes is: ',1-(b/a))


#Splitting the data into train and test data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

print('xtrain and ytrain shapes: ',x_train.shape,y_train.shape)
print('xtest and ytest shapes: ',x_test.shape,y_test.shape)

clf = svm.SVC(kernel='linear', C=1).fit(x_train, y_train)
score=clf.score(x_test, y_test)
print('%d',score)