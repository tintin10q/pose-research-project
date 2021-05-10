import matplotlib.pyplot as plt
import numpy as np
import os

def plot(csv):
    fig, ax = plt.subplots(figsize=(15, 10))

    plt.title("Train and Test scores with K in KNN", fontsize='24')
    K = []
    score_train = []
    score_test = []
    score_cros_val = []
    with open(csv, "r+") as inp:
        for index, line in enumerate(inp):
            if index == 0:
                continue
            line = line.strip().split(",")
            K.append(line[0])
            score_test.append(float(line[1]))
            score_train.append(float(line[2]))
            score_cros_val.append(np.mean([float(score) for score in line[3:7]]))
        print(score_test,"\n", score_train)
        '''
        k = [i for i in range(len([index for index, line in enumerate(inp)])//2)];inp.seek(0)
        score_train = [float(line[-5:]) for index, line in enumerate(inp) if not index % 2];inp.seek(0)
        score_test = [float(line[-5:]) for index, line in enumerate(inp) if index % 2]
        '''
    # print(K[:3], score_train[:3], score_test[:3])

    plt.xlabel("K", fontsize='20')  # adds a label in the x axis
    plt.ylabel("Score", fontsize='20')
    ax.plot(K, score_train, label="Train")
    ax.plot(K, score_test, label="Test")
    ax.plot(K, score_cros_val, label="Mean Cross validation")
    plt.xticks([k for index, k in enumerate(K) if index % 10 == 0], [k for index, k in enumerate(K) if index % 10 == 0],  fontsize = '20')
    plt.yticks(fontsize='20')
    plt.rc('xtick', labelsize=40)
    plt.rc('ytick', labelsize=40)
    ax.legend(fontsize=20)  # creates a legend to identify the plot
    # plt.show()
    import os

    n = 1
    path = f"KNN_results_from_{csv}_{n}.png"
    while os.path.exists(path):
        n += 1
        path = f"KNN_results_from_{csv}_{n}.png"

    plt.savefig(path)
    print(f"Saved plot to {path}")


def plotCNN(csv):
    fig, ax = plt.subplots(figsize=(15, 10))

    plt.title("Train and Test scores with alpha in NN", fontsize='20')
    A = []
    score_train = []
    score_cros_val = []
    score_test = []
    with open(csv, "r+") as inp:
        for index, line in enumerate(inp):
            if index == 0:
                continue
            line = line.strip().split(",")
            A.append(line[0])
            score_test.append(float(line[1]))
            score_train.append(float(line[2]))
            score_cros_val.append(np.mean([float(score) for score in line[5:len(line) - 1]]))
        '''
        k = [i for i in range(len([index for index, line in enumerate(inp)])//2)];inp.seek(0)
        score_train = [float(line[-5:]) for index, line in enumerate(inp) if not index % 2];inp.seek(0)
        score_test = [float(line[-5:]) for index, line in enumerate(inp) if index % 2]
        '''
    # print(K[:3], score_train[:3], score_test[:3])

    plt.xlabel("Alpha", fontsize='20')  # adds a label in the x axis
    plt.ylabel("Score", fontsize='20')
    ax.plot(A, score_train, label="Train")
    ax.plot(A, score_test, label="Test")
    ax.plot(A, score_cros_val, label="Mean Cross validation")
    plt.ylim((0.97, 1))
    plt.xticks(fontsize='20')
    plt.yticks(fontsize='20')
    ax.legend(fontsize='20')  # creates a legend to identify the plot
    # plt.show()
    import os

    n = 1
    path = f"CNN_results_from_{csv}_{n}.png"
    while os.path.exists(path):
        n += 1
        path = f"CNN_results_from_{csv}_{n}.png"

    plt.savefig(path)
    print(f"Saved plot to {path}")

def is_num(potential_num):
    try:
        int(potential_num)
    except:
        return False
    return True

def plotNN(csv):
    with open(csv) as csv_lines:
        runs = [[[], []]]
        result_index = 0
        for index, line in enumerate(csv_lines):
            if index <= 0:
                continue
            line = line.strip().split(",")
            runs[result_index][0].append(line[1])
            runs[result_index][1].append(line[2])
            # print(line)
            if index % 19 == 0:
                runs.append([[], []])
                result_index += 1
    runs = runs[:len(runs)-1]

    fig, ax = plt.subplots(figsize=(15, 10))

    plt.title("Test scores with different nodes and layers in NN",  fontsize='24')
    plt.xlabel("Nodes in layers",  fontsize='20')  # adds a label in the x axis
    plt.ylabel("Score", fontsize='20')
    plt.ylim((0.92, 1))
    plt.xticks(fontsize='20')
    plt.yticks(fontsize='20')
    nodes = [i for i in range(10, 200, 10)]

    for index, run in enumerate(runs):
        index += 1
        ax.plot(nodes, [float(r) for r in run[0]], label=f"Test_{index}_layers")
        # ax.plot(nodes, run[0], label=f"Train_{index}_layers")
    ax.legend( fontsize='20')  # creates a legend to identify the plot
    # line =

    n = 1
    path = f"NN_results_from_{csv}_{n}.png"
    while os.path.exists(path):
        n += 1
        path = f"NN_results_from_{csv}_{n}.png"

    plt.savefig(path)
    print(f"Saved plot to {path}")

    fig, ax = plt.subplots(figsize=(15, 10))

    plt.title("Train scores with different nodes and layers in NN", fontsize='24')
    plt.xlabel("Nodes in layers", fontsize='20')  # adds a label in the x axis
    plt.ylabel("Score", fontsize='20')
    plt.ylim((0.92, 1))
    plt.xticks(fontsize='20')
    plt.yticks(fontsize='20')
    nodes = [i for i in range(10, 200, 10)]

    for index, run in enumerate(runs):
        index += 1
        ax.plot(nodes, [float(r) for r in run[1]], label=f"Train_{index}_layers")
        # ax.plot(nodes, run[0], label=f"Train_{index}_layers")
    ax.legend(fontsize='20')  # creates a legend to identify the plot
    # line =

    n = 1
    path = f"NN_results_from_{csv}_{n}.png"
    while os.path.exists(path):
        n += 1
        path = f"NN_results_from_{csv}_{n}.png"

    plt.savefig(path)
    print(f"Saved plot to {path}")

# plot("Knncrossvalidation_13.csv")
# plotCNN("NeuralNet_1.csv")

def plotNN2(csv):
    with open(csv) as csv_lines:
        layers = {}
        for index, line in enumerate(csv_lines):
            if index <= 0:
                continue
            line = line.strip().split(",")
            if line[-1] not in layers.keys():
                layers[line[-1]] = []
                layers[line[-1] + "nodes"] = []
            layers[line[-1]].append(line[1])
            layers[line[-1] + "nodes"].append(line[-2])

    fig, ax = plt.subplots(figsize=(15, 10))

    plt.title("Train and Test scores with differnt nodes and layers in NN", fontsize='24')
    plt.xlabel("Nodes in layers", fontsize='20')  # adds a label in the x axis
    plt.ylabel("Score", fontsize='20')
    plt.ylim((0.97, 1))
    nodes = [i for i in range(10, 200, 10)]
    print(layers)
    ax.plot([float(i) for i in layers[" 4nodes"]], [float(i) for i in layers[" 4"]], label=f"4_layers")
        # ax.plot(nodes, run[0], label=f"Train_{index}_layers")
    ax.legend()  # creates a legend to identify the plot
    # line =

    n = 1
    path = f"NN_results_from_{csv}_{n}.png"
    while os.path.exists(path):
        n += 1
        path = f"NN_results_from_{csv}_{n}.png"

    plt.savefig(path)
    print(f"Saved plot to {path}")
plot("Knncrossvalidation_13.csv")
# plotNN2("NeuralNet_6.csv")
# plotCNN("NeuralNet_1.csv")
# plotNN("NeuralNet_4Big.csv")