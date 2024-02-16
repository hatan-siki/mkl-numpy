from timeit import default_timer as timer
from IPython.display import HTML
from sklearn import metrics
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
x, y = fetch_openml('mnist_784', version=1, return_X_y=True)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

## sklearnexあり
from sklearnex import patch_sklearn
patch_sklearn()
from sklearn.svm import SVC
params = {"C": 100.0, "kernel": "rbf", "gamma": "scale"}
start = timer()
classifier = SVC(**params).fit(x_train, y_train)
train_patched = timer() - start
print(f"Intel® extension for Scikit-learn time: {train_patched:.2f} s")

## 標準sklearn
from sklearnex import unpatch_sklearn
unpatch_sklearn()
from sklearn.svm import SVC
start = timer()
classifier = SVC(**params).fit(x_train, y_train)
train_unpatched = timer() - start
print(f"Original Scikit-learn time: {train_unpatched:.2f} s")

print(f"Get speedup in {(train_unpatched/train_patched):.1f}times")
