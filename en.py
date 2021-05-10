
import statistics
with open("Knncrossvalidation_13.csv") as knn:
    # for index, line in enumerate(knn):
    #     # print(line.strip().split(",")[-2])
    times = [float(line.strip().split(",")[-2]) for index, line in enumerate(knn) if index > 0]

print(f"Mean training time for knn was {statistics.mean(times)} with std: {round(statistics.stdev(times), 2)}")

with open("NeuralNet_4Big.csv") as nn:
    # for index, line in enumerate(knn):
    #     # print(line.strip().split(",")[-2])
    times = [float(line.strip().split(",")[3]) for index, line in enumerate(nn) if index > 0]

print(f"Mean training time for nn was {statistics.mean(times)} with std: {round(statistics.stdev(times), 2)}")
