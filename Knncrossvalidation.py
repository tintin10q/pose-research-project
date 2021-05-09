import pandas as pd
import numpy as np
from sklearn.model_selection import cross_validate
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import time
import os

df = pd.read_csv('ShakeFive2.metadata.csv')

''' This is to show where s0 action and s1 action are the same we remove the ones where it s1 is None because this is almost all of the ones where they don't match
b = df.S1ActionName == df.S0ActionName
print(list(b).count(False))
print(list(b).count(True))
'''

df = df.drop(["FrameID", "timestamp", "VideoName"], axis=1)  # remove those collums

df = df.mask(df.eq('None')).dropna()  # remove rows with None in them

y = df.S0ActionName  #subsetting only the action names (target labels)
X = df.drop(["S0ActionName", "S1ActionName"], axis=1)  # remove those y from x

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0) # split that boi

n = 1
path = f"Knncrossvalidation_{n}.csv"
while os.path.exists(path):
    n += 1
    path = f"Knncrossvalidation_{n}.csv"
print(f"Writing results to \"{path}\"")
with open(path, "w+") as output:
    output.write(f"k, final_result, train_result, traintime, crossval_time\n")
    for k in range(1, 250, 4):
        t0 = time.time()
        clf = KNeighborsClassifier(n_neighbors=k, n_jobs=-1)
        clf.fit(X_train, y_train)
        t1= time.time()

        cross_val_dic = cross_validate(clf, X_train, y_train, n_jobs=-1, return_estimator=True)
        t2 = time.time()

        scores = cross_val_dic['test_score']
        best_model = cross_val_dic['estimator'][np.argmax(scores)]
        final_result = best_model.score(X_test, y_test)
        train_result = best_model.score(X_train,y_train)
        total1 = t2 - t0
        total = t1 - t0
        print(f'K={k} gave {final_result}% accuracy in testing with the best cross-validated split')
        output.write(f"{k}, {final_result}, {train_result}, {total},{total1}\n")


        print(f"KNN Run-time without cross-val: {total}, run-time with cross-val: {total1}")

'''K=1 gave [0.6291834  0.59404284 0.67804552 0.64156627 0.68373494 0.70304653
 0.60863743 0.61031135 0.61834617 0.56143288]% accuracy with a standard deviation of 0.04
KNN Run-time without cross-val: 0.7939393520355225, run-time with cross-val: 15.53118634223938
K=5 gave [0.6352075  0.63487282 0.6710174  0.64524766 0.68139224 0.71275527
 0.6260462  0.62236358 0.62537663 0.57114161]% accuracy with a standard deviation of 0.04
KNN Run-time without cross-val: 0.8183467388153076, run-time with cross-val: 14.720701932907104
K=9 gave [0.6398929  0.63085676 0.68842035 0.66298527 0.69243641 0.71074657
 0.6324071  0.63307667 0.64111148 0.55942417]% accuracy with a standard deviation of 0.04
KNN Run-time without cross-val: 0.8018796443939209, run-time with cross-val: 14.863538980484009
K=25 gave [0.63888889 0.66365462 0.73159304 0.67570281 0.67570281 0.72380315
 0.69300301 0.64245062 0.65215936 0.56176766]% accuracy with a standard deviation of 0.05
KNN Run-time without cross-val: 0.791815996170044, run-time with cross-val: 16.18725848197937
'''
