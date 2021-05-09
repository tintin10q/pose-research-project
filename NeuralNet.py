from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
import time
import numpy as np
import os
import sys

if len(sys.argv) > 1:
    assert int(sys.argv[1]), "Amount of cores is not a number"
    cores = int(sys.argv[1])
    assert cores <= os.cpu_count(), "Cores given"
else:
    cores = os.get_cpu() * 2
print(f"Running with {cores} cores")

df = pd.read_csv('ShakeFive2.metadata.csv')
df = df.drop(["FrameID", "timestamp", "VideoName"], axis=1)  # remove those collums

df = df.mask(df.eq('None')).dropna()  # remove rows with None in them

y = df.S0ActionName  # subsetting only the action names (target labels)
X = df.drop(["S0ActionName", "S1ActionName"], axis=1)  # remove those y from x

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)  # split that boi

scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
scaler = preprocessing.StandardScaler().fit(X_test)
X_test = scaler.transform(X_test)

# We tried to do 6 7 8 7 6 but we 34 so not so good
# We then tried 100,100,100,100,100,100,100,100,100,100,100,100 we got train 78 test 78
# We then tried  20 20 20 20 20 20 20 20 20 20  this gave us 65 train and 64 test
# We then treid [85,85,85,85,85,85,85,85,85,85,85,85] with alpha 0.0005 we got 0.77 0.76

# plt.figure(1)
# mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3)
# mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
# plt.xlabel("Feature 0")
# plt.ylabel("Feature 1")

n = 1
path = f"NeuralNet_{n}.csv"
while os.path.exists(path):
    n += 1
    path = f"NeuralNet_{n}.csv"

with open(path, "a+") as output:
    output.write("alpha, final_result, train_result,time,total1\n")
    for alpha in [0.0001, 0.0005, 0.001, 0.005, 0.01]:
        t0 = time.time()
        mlp = MLPClassifier(solver='adam', early_stopping=True, verbose=True, random_state=0, hidden_layer_sizes=[100, 100, 100, 100], alpha=alpha, max_iter=9000).fit(
            X_train, y_train)
        t1 = time.time()

        cross_val_dic = cross_validate(mlp, X_train, y_train, n_jobs=cores, return_estimator=True)
        t2 = time.time()
        scores = cross_val_dic['test_score']
        best_model = cross_val_dic['estimator'][np.argmax(scores)]
        final_result = best_model.score(X_test, y_test)
        train_result = best_model.score(X_train, y_train)

        print(f"{final_result}% accuracy in testing (unseen data) with alpha: {alpha}")

        print("Accuracy on training set: {:.2f}".format(train_result))
        print("Accuracy on test set: {:.2f}".format(final_result))

        total1 = round(t2 - t0, 2)
        total = round(t1 - t0, 2)

        print(f"Run-time without cross-val: {total}, run-time with cross-val: {total1}")
        
        output.write(f"{alpha}, {final_result}, {train_result} {total} {total1}\n")
