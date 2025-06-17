from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix,  ConfusionMatrixDisplay
import matplotlib.pyplot as plt

iris=load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

model = SVC(kernel='rbf')
model.fit(X_train, y_train)
y_pred=model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:", cm)

cm_display= ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['0','1','2'])

cm_display.plot()
plt.show()



