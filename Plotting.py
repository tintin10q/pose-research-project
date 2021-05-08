import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(15,10))

plt.title("Train and Test scores with K", fontsize='16')
K= []
score_train = []
score_test = []
with open("Knncrossvalidation.txt", "r+") as inp:
    values = inp.read()
    values = values.replace('\n', ", ")
    values = values.split(', ')

    for i in range (0, len(values)-2, 3):
        K.append(int(values[i]))
        score_test.append(float(values[i+1]))
        score_train.append(float(values[i+2]))

    '''
    k = [i for i in range(len([index for index, line in enumerate(inp)])//2)];inp.seek(0)
    score_train = [float(line[-5:]) for index, line in enumerate(inp) if not index % 2];inp.seek(0)
    score_test = [float(line[-5:]) for index, line in enumerate(inp) if index % 2]
    '''
print(K[:3], score_train[:3], score_test[:3])

plt.xlabel("K",fontsize='13')	#adds a label in the x axis
plt.ylabel("Score",fontsize='13')
ax.plot(K, score_train, label="Train")
ax.plot(K, score_test, label="Test")

ax.legend()	#creates a legend to identify the plot
plt.show()
