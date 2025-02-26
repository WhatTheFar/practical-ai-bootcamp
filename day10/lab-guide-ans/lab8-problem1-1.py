import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat
from sklearn.svm import SVC


'''
Step 0: Load the data from './data/lab8data1.mat'
'''

dataset = loadmat('data/lab8data1.mat')
print(dataset.keys())

X = dataset["X"]
y = dataset["y"]

print("Dimension of X: {}".format(X.shape))
print("Dimension of y: {}".format(y.shape))

number_of_row = X.shape[0]

positives = (y == 1).reshape(number_of_row, 1)
negatives = (y == 0).reshape(number_of_row, 1)

print('\n')


'''
Step 1: Instantiate a 'linear' SVM classifier with C = 1
'''

classifier1 = SVC(kernel="linear") # By default, C = 1
classifier1.fit(X, np.ravel(y))


'''
Step 2: Visualizing the training set result 
'''

plt.figure(1)
plt.scatter(X[positives[:, 0], 0], X[positives[:, 0], 1], c="r", marker="+", s=50)
plt.scatter(X[negatives[:, 0], 0], X[negatives[:, 0], 1], c="y", marker="o", s=50)

# plotting the decision boundary
X1, X2 = np.meshgrid(np.linspace(X[:, 0].min(), X[:, 0].max(), num=300),
                     np.linspace(X[:, 1].min(), X[:, 1].max(), num=300))

plt.contour(X1, X2, classifier1.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), colors="b")


'''
Step 3: Instantiate a 'linear' SVM classifier with C = 100 and
plot the decision boundary
'''

classifier2 = SVC(kernel="linear", C=100) # By default, C = 1
classifier2.fit(X, np.ravel(y))

plt.figure(2)
plt.scatter(X[positives[:, 0], 0], X[positives[:, 0], 1], c="r", marker="+", s=50)
plt.scatter(X[negatives[:, 0], 0], X[negatives[:, 0], 1], c="y", marker="o", s=50)

# plotting the decision boundary
X1, X2 = np.meshgrid(np.linspace(X[:, 0].min(), X[:, 0].max(), num=300),
                     np.linspace(X[:, 1].min(), X[:, 1].max(), num=300))

plt.contour(X1, X2, classifier2.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), colors="b")

