import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('ShakeFive2.metadata.csv')

''' This is to show where s0 action and s1 action are the same we remove the ones where it s1 is None because this is almost all of the ones where they don't match
b = df.S1ActionName == df.S0ActionName
print(list(b).count(False))
print(list(b).count(True))
'''


df = df.drop(["FrameID","timestamp","VideoName"], axis=1) # remove those collums

df = df.mask(df.eq('None')).dropna() # remove rows with None in them



y = df.S0ActionName # remove x from y hahah thats not correct
X = df.drop(["S0ActionName", "S1ActionName"], axis=1) # remove those y from x


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0) # split that boi


# k = 173 was sqaure root, Train set accuracy: 0.73, Test set accuracy: 0.72 so we are unfitting underfitting
# k = 201 , Train set accuracy: 0.72, Test set accuracy: 0.71 it went down 😢
# k = 173*3-1 to keep it uneven, Train set accuracy: 0.68, Test set accuracy: 0.68 so we are unfitting underfitting
# k = 11 oh yeah it was lower the k the more complex haha lol forgot, Train set accuracy: 0.96, Test set accuracy: 0.93 so that looks much better! but it looks like it is a tiny bit overfitting but yes at this point we are just greedy 93 is pretty good
# now we are doing


with open("scores.txt","a+") as output:
    for k in range(1, 150,2):
        clf = KNeighborsClassifier(n_neighbors=k)
        clf.fit(X_train, y_train)
        train_score = "Train set accuracy: {:.2f}".format(clf.score(X_train, y_train))
        test_score = "Test set accuracy: {:.2f}".format(clf.score(X_test, y_test))
        output_text = train_score+"\n"+ test_score+"\n"
        print(output_text)
        output.write(output_text)

